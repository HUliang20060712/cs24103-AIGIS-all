# 环境验证截图（E1-1）

存放三套环境的启动与版本输出截图：`env-dev.png`、`env-test.png`、`env-prod.png`。
每张需含启动命令、监听端口、JDK/Node/Python 版本、数据库或缓存连通性、时间戳。

| 环境 | 网关入口 | 推荐服务 | 数据库 | Redis |
|---|---|---|---|---|
| dev | 8081 | 8083 | 5432/aigis | 6379/0 |
| test | 8082 | 8083 | 15432/aigis_test | 6380/2 |
| prod | 80 | 8083 | postgres:5432/aigis | redis:6379 |
