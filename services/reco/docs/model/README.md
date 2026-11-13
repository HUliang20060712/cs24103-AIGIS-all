# EA 模型入库说明（E3-1）

模型工程 `model/AIGIS.eapx` 随仓库入库，Package 与课程阶段一一对应：

| Package | 内容 | 责任人 |
|---|---|---|
| 01_计划 | 用例图、活动图 | 何汪瑞、胡亮 |
| 02_设计 | 部署图、组件图 | 胡德伟 |
| 03_实现 | 类图 | 黄德淳 |
| 04_测试 | 无 | — |

我的两张图：部署图（Nacos、Redis、PostgreSQL 节点与端口）、组件图（Controller→Service→DAO→Redis 四层）。
统一用 EA 17 手工绘制，导出 PNG 存 `docs/model/`。
