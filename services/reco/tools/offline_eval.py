#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B-推荐模块离线评测：Recall@20。

数据：tools/sample_interactions.csv（1,200 条隐式反馈）
切分：按时间 8:2 训练/测试
基线：全热度榜
本方案：物品-物品协同过滤 + 类别内容相似度补位
"""
import csv
import json
import math
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "sample_interactions.csv")
OUT = os.path.join(HERE, "eval_report.json")

TOP_N = 20
HALF_LIFE_DAYS = 30.0


def load():
    rows = []
    with open(DATA, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "user": int(r["user_id"]),
                "item": int(r["item_id"]),
                "category": r["category"],
                "ts": int(r["ts"]),
            })
    rows.sort(key=lambda x: x["ts"])
    cut = int(len(rows) * 0.8)
    return rows[:cut], rows[cut:]


def build_profile(train):
    user_items = defaultdict(set)
    item_users = defaultdict(set)
    item_cat = {}
    latest = 0
    for r in train:
        user_items[r["user"]].add(r["item"])
        item_users[r["item"]].add(r["user"])
        item_cat[r["item"]] = r["category"]
        latest = max(latest, r["ts"])
    return user_items, item_users, item_cat, latest


def recommend(user, user_items, item_users, item_cat, seen, k=TOP_N):
    scores = defaultdict(float)
    cat_weight = defaultdict(float)
    for item in user_items.get(user, set()):
        for other in item_users[item]:
            if other == user:
                continue
            for cand in user_items[other]:
                if cand in seen:
                    continue
                scores[cand] += 1.0 / math.log(2 + len(user_items[other]))
        cat_weight[item_cat[item]] += 1.0
    for item, cat in item_cat.items():
        if item in seen:
            continue
        scores[item] += 0.15 * cat_weight.get(cat, 0.0)
    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    return [i for i, _ in ranked[:k]]


def evaluate():
    train, test = load()
    user_items, item_users, item_cat, latest = build_profile(train)
    truth = defaultdict(set)
    for r in test:
        truth[r["user"]].add(r["item"])

    users = [u for u in truth if u in user_items]
    hits, total = 0, 0
    for u in users:
        rec = recommend(u, user_items, item_users, item_cat, user_items[u])
        total += len(truth[u])
        hits += len(set(rec) & truth[u])
    recall = hits / total if total else 0.0

    pop = defaultdict(int)
    for r in train:
        pop[r["item"]] += 1
    top_hot = [i for i, _ in sorted(pop.items(), key=lambda kv: -kv[1])[:TOP_N]]
    hot_hits = sum(len(set(top_hot) & truth[u]) for u in users)
    hot_recall = hot_hits / total if total else 0.0

    report = {
        "train_rows": len(train),
        "test_rows": len(test),
        "users_evaluated": len(users),
        "k": TOP_N,
        "recall_at_20": round(recall, 4),
        "baseline_hot_recall_at_20": round(hot_recall, 4),
        "delta": round(recall - hot_recall, 4),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    report = evaluate()
    assert report["recall_at_20"] >= 0.15, "Recall@20 未达 0.15 验收线"
