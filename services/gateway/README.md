# E-微服务协调（gateway-service）

负责人：江蝶　状态：骨架

- 路由：`/api/reco/**` → reco-service:8083；`/api/vision/**` → vision-service:8084；`/api/chat/**` → dialog-service。
- 降级：`Retry` 过滤器对 5xx 重试 1 次；Nacos 服务发现待接入（当前为直连 uri）。
- dev 8081 / test 8082 / prod 80。
- 待补：Nacos 2.3.0 注册、限流、鉴权透传、熔断参数。
