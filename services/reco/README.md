# AIGIS B-推荐系统（reco-service）

> P03 AI 智能地理信息系统 · 项目组 cs24103 · 胡德伟（2024210546）
> 实验一交付：接口契约、服务骨架、离线评测脚本、文档与流水线配置

## 1. 模块定位

B 业务线负责个性化推荐：用户偏好管理、协同过滤与内容推荐混合排序、Top-N 推荐流、反馈回收。
本阶段交付系统原型骨架：可编译、可联调、可跑离线评测，不承诺线上效果。

## 2. 目录

```
cs24103-AIGIS-reco/
├── pom.xml                       # Spring Boot 3.3.5 / JDK 21
├── .gitee/workflows/ci.yml       # build-java / build-python / verify / ai-trace
├── contracts/openapi.yaml        # 6 个推荐接口（M3 冻结）
├── contracts/desktop-api.md      # 与 D 桌面端的 GeoJSON 契约
├── sql/schema.sql                # 5 张表
├── src/main/java/cn/edu/chzu/aigis/reco/   # 控制器 / 服务 / DAO
├── src/main/resources/           # dev / test / prod 三套 profile
├── src/test/java/                # 单元测试
├── tools/offline_eval.py         # Recall@20 离线评测（纯标准库）
├── tools/sample_interactions.csv # 1,200 条样例交互
├── docs/srs.md                   # 需求规格说明书（初稿）
├── docs/操作手册.md
├── docs/ai-log/lab1-ai-log.md    # 9 条 AI 使用记录
├── docs/weekly/w10.md … w17.md   # 8 份周报
└── docs/env/                     # 环境截图存放说明（E1-1）
```

## 3. 快速开始

```bash
docker compose up -d
psql -h 127.0.0.1 -p 15432 -U aigis -d aigis -f sql/schema.sql
mvn -q clean verify
mvn spring-boot:run -Dspring-boot.run.profiles=dev
curl "http://127.0.0.1:8083/api/reco/feed?userId=1001&page=1&size=10"
```

## 4. 离线评测

```bash
python3 tools/offline_eval.py
```

读取 1,200 条样例交互，按时间 8:2 切分，输出热门榜基线与混合排序的 Recall@20，
结果写入 `tools/eval_report.json`，无第三方依赖。

## 5. 与报告的对应

| 报告条目 | 本仓库位置 |
|---|---|
| 表 1-4 feed / feedback | `contracts/openapi.yaml`、`RecoController` |
| 表 1-9 6 个接口 | `contracts/openapi.yaml` |
| E2-1 工程根目录与构建 | 仓库根目录、CI build-java 日志 |
| E5-1 四作业流水线 | `.gitee/workflows/ci.yml` |
| E6-1 推荐接口运行 | `GET /api/reco/feed` |
| E7-1 操作手册 | `docs/操作手册.md` |
| 表 1-36 AI 记录 | `docs/ai-log/lab1-ai-log.md` |

## 6. 声明

本仓库是实验一按报告描述重建的 B 模块骨架，真实开发代码以组内仓库 `cs24103-AIGIS` 的 `feature/2024210546-reco` 分支为准。

## 7 样例数据实测（2026-11-11）

```
train_rows 960 / test_rows 240 / users 109 / k 20
recall_at_20 0.2911　baseline_hot 0.1097　delta 0.1814
```

样例数据为脚本合成，仅用于验证评测链路可跑通，不作为效果结论。
