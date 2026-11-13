#!/usr/bin/env bash
# 环境自检：把本机版本、端口、依赖连通性一次打出来，供 E1-1 截图
set +e
echo "== 采集时间 =="; date '+%F %T %Z'
echo; echo "== 版本 =="
java -version 2>&1 | head -3
mvn -v 2>/dev/null | head -2
node -v 2>/dev/null; npm -v 2>/dev/null
python3 -V
psql --version 2>/dev/null
redis-cli --version 2>/dev/null
docker --version 2>/dev/null
echo; echo "== 端口 =="
for p in 8081 8083 8084 5432 6379; do
  (echo >/dev/tcp/127.0.0.1/$p) >/dev/null 2>&1 && echo "port $p  open" || echo "port $p  closed"
done
echo; echo "== 依赖连通 =="
redis-cli -h 127.0.0.1 -p 6379 ping 2>/dev/null || echo "redis 未连通"
psql "postgresql://aigis:aigis@127.0.0.1:15432/aigis" -c "select 1 as ok" 2>/dev/null || echo "postgres 未连通"
