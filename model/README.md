# 模型工程（Enterprise Architect 17）

本目录存放 AIGIS 的 EA 工程源文件。**所有模型图必须用 EA 17 手工绘制**，
禁止 PlantUML、SVG 脚本、AI 出图后转贴——否则按红线处理，建模部分不计分。

## 1 文件约定

| 文件 | 说明 |
|---|---|
| `AIGIS.qea` | 唯一模型源文件，答辩现场打开的就是它 |
| 不要提交 | `*.qea.bak`、`*.eapx`、EA 缓存目录、导出的临时图 |

新建工程：`File → New Project`，保存路径选本目录，文件名 `AIGIS`。
建完立刻 `Project → Auditing → Enable Auditing`，留下建模时间线。

## 2 包结构（与课程阶段一一对应）

```
AIGIS
├── 01 项目计划
│   ├── 项目管理        （WBS、风险、变更控制）
│   ├── A 对话
│   ├── B 推荐
│   ├── C 识别
│   ├── D 语义分割
│   └── E 微服务协调
├── 02 需求模型
├── 03 设计模型
└── 04 测试与部署
```

## 3 图清单

| 图号 | 名称 | EA 图类型 | 导出文件 |
|---|---|---|---|
| DG-01 | 模型仓库结构图 | UML Structural → Package | `docs/model/img/DG-01-Package.png` |
| DG-02 | WBS 工作分解结构图 | Project Management → Work Breakdown Structure | `docs/model/img/DG-02-WBS.png` |
| DG-03 | 三环境部署图 | UML Structural → Deployment | `docs/model/img/DG-03-Deploy.png` |
| DG-04 | 系统组件图 | UML Structural → Component | `docs/model/img/DG-04-Component.png` |

图注模板见 `docs/model/img/README.md`。

## 4 提交前自检

- [ ] `model/AIGIS.qea` 已入库，从仓库克隆后可直接打开
- [ ] 四张图齐全，图内无 `TODO`、`xxx`、`待补充`
- [ ] 中文无方块（字体统一 Microsoft YaHei 9pt）
- [ ] 图号、图注与报告正文一致
- [ ] WBS 图中的任务数与报告任务表一致（23 项 / 198 人时）
- [ ] 审计已开启，修改时间线可查
- [ ] 每张 PNG 宽度 ≥1600px，未压缩变形
