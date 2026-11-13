#!/usr/bin/env bash
# 一条命令起依赖与建表；服务另开窗口按 README 启动
set -e
cd "$(dirname "$0")/.."
docker compose up -d postgres redis
echo "等待数据库就绪..."
for i in $(seq 1 30); do
  docker exec "$(docker compose ps -q postgres)" pg_isready -U aigis >/dev/null 2>&1 && break
  sleep 1
done
PGPASSWORD=aigis psql -h 127.0.0.1 -p 15432 -U aigis -d aigis -f services/reco/sql/schema.sql
echo "依赖已就绪：PostgreSQL 15432 / Redis 6379"
