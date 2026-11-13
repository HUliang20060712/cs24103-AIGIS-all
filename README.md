# AIGIS 整体源码（cs24103 · P03 AI 智能地理信息系统）

实验一交付：五条业务线的一体化仓库，一套代码、三套环境配置。

| 业务线 | 目录 | 负责人 | 代码状态 |
|---|---|---|---|
| A 对话（Web 前端，React + SSE + Markdown） | `web/` | 何汪瑞 2024210544 | 骨架（页面与 SSE 调用可跑，RAG 待接） |
| B 推荐（Web 后端，Spring Boot） | `services/reco/` | 胡德伟 2024210548 | 完整骨架，6 接口 + 缓存降级 + 离线评测 |
| C 识别（Web 后端，Spring Boot + 异步队列） | `services/vision/` | 黄德淳 2024210549 | 骨架（上传/任务查询接口，推理待接） |
| D 语义分割（桌面端，Python + PyTorch + OpenCV） | `desktop/` | 胡亮 2024210546 | 已提交的实作代码（原样并入） |
| E 微服务协调（Spring Cloud + Nacos） | `services/gateway/` | 江蝶 | 骨架（路由与降级，Nacos 接入待补） |

## 1 目录

```
cs24103-AIGIS-all/
├── web/                 # A 前端
├── services/reco/       # B 推荐（含 contracts、sql、docs/ai-log、周报）
├── services/vision/     # C 识别
├── services/gateway/    # E 网关
├── desktop/             # D 桌面端（原样）
├── scripts/             # 一键启动与环境检查
├── doc/                 # 组级文档
├── docker-compose.yml
└── .gitee/workflows/ci.yml
```

## 2 一键启动

```bash
./scripts/dev-up.sh        # 依赖 + 建表 + 各服务
./scripts/env-check.sh     # 版本与端口自检（E1-1 截图用）
```

| 服务 | 端口 |
|---|---|
| 网关 gateway | 8081(dev) / 8082(test) / 80(prod) |
| 推荐 reco | 8083 |
| 识别 vision | 8084 |
| 前端 web | 5173（开发） |

## 3 说明

- 各服务 README 写明负责人与交付边界；标“骨架”的模块只保证接口与启动，业务逻辑待对应负责人补。
- 桌面端代码署名胡亮（2024210546），未改动，仅放入 `desktop/`。
- 实验一只交付原型：能起、能调、能演示主流程，不承诺效果指标。
