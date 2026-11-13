# 实验一 AI 使用记录（lab1-ai-log）

> 每条记录含四件套：① Prompt 原文 ② AI 输出摘要 ③ 人工修改说明 ④ 评审结论

## A-01　环境验证命令整理

- **Prompt**：列出校验 Python 3.12 + PyTorch + OpenCV + Git + Docker 环境的 Windows 命令
- **AI 输出摘要**：给出 python --version、torch.__version__、cv2.__version__、git --version、docker --version 等命令
- **人工修改**：补 docker ps --format 过滤；实际执行后把预期输出全部换成实测值
- **结论**：采纳（改后），命令输出以实跑为准

## A-02　WBS 初稿

- **Prompt**：对 AIGIS（AI对话/推荐/图像识别/语义分割/微服务协调 5模块）做 3 层 WBS，L3 任务 4~16 人时
- **AI 输出摘要**：22 项 L3 任务 + 工时估算
- **人工修改**：合并 2 项重复；把我（组长）初版 52 人时中的 3.1 架构转给组员E、2.5 SRS 转给胡德伟；删掉 AI 加的"区块链存证"
- **结论**：部分采纳，22 项最终保留

## A-03　CI 配置

- **Prompt**：写 GitHub Actions 的 Python 3.12 + pytest 流水线 yaml
- **AI 输出摘要**：build + verify 两 job
- **人工修改**：首版缺 setup-python，实跑报 python: command not found 后补上；加 ai-trace 门禁
- **结论**：采纳（改后）

## A-04　U-Net 结构参考

- **Prompt**：写一个 PyTorch U-Net，6 类输出，输入 512x512x3
- **AI 输出摘要**：完整 UNet 类含 DoubleConv、Encoder、Decoder
- **人工修改**：把 base_ch 从 32 改到 64（CPU 训练 32 太小收敛慢）；注释标明 skip connection 位置
- **结论**：采纳（改后）

## A-05　依赖核验

- **Prompt**：Python 遥感影像分割需要哪些 pip 包？
- **AI 输出摘要**：torch、torchvision、opencv-python、segmentation-models-pytorch、rasterio
- **人工修改**：核验后发现 segmentation-models-pytorch 可用但课程不鼓励额外重依赖，改用 torchvision.models.segmentation 内置的 deeplabv3 备选；rasterio 只在需要读 .tif 时再加
- **结论**：弃用 segmentation-models-pytorch，保留核心 4 个

## A-06　风险识别

- **Prompt**：遥感影像语义分割课程项目的主要风险有哪些？
- **AI 输出摘要**：GPU 不足、数据标注质量、过拟合、CPU 推理慢
- **人工修改**：把"GPU 不足"从概率3调到4（机房确实无 GPU）；补"AI 生成虚构依赖"风险（A-05 已验证存在）
- **结论**：采纳（改后）

## A-07　报告骨架

- **Prompt**：按实验任务/项目团队/我的实验过程结构写实验一报告骨架
- **AI 输出摘要**：章节清单
- **人工修改**：删掉评价标准和附录（老师明确说写给我看的）；补真实问题记录；逐条核对版本号
- **结论**：采纳（改后）

## A-08　成本估算

- **Prompt**：按 200 人时、学生 30 元/人时、大模型 API 按量计费估算成本
- **AI 输出摘要**：人力 6000 + API 80 = 6080 元
- **人工修改**：AI 建议的"云服务器 300 元"改为 0（本机 Docker）；补"零现金采购"原则
- **结论**：采纳（改后）

---

**四件套自查**：8 条 × 4 字段 = 32 项齐全；人工修改率 8/8 = 100%。
