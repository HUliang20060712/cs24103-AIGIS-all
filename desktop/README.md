# AIGIS 桌面端 - D-语义分割模块

> P03 AI智能地理信息系统 · cs24103 · 胡亮（2024210548）

遥感影像语义分割桌面工具，负责训练数据管理、模型训练、分割推理与结果可视化。

## 功能

- **训练数据管理**：遥感影像样本导入、标注检查、数据集划分
- **模型训练**：U-Net 迁移学习训练流程，支持断点续训
- **分割任务**：单张/批量遥感影像地物分割推理
- **可视化**：分割结果叠加显示、类别图例导出

## 技术栈

- Python 3.12
- PyTorch 2.5（模型训练与推理）
- OpenCV 4.5（影像读写与预处理）
- PyQt5（桌面 GUI，实验四实现）

## 目录结构

```
aigis-desktop/
├── config/           # 配置文件
├── data/samples/     # 样例遥感影像（占位）
├── docs/
│   ├── ai-log/       # AI 使用记录
│   └── env/          # 环境验证截图
├── src/
│   ├── main.py       # 入口
│   ├── ui/           # GUI 层
│   ├── core/         # 业务逻辑（数据集/训练/推理/可视化）
│   ├── models/       # 模型定义（U-Net）
│   └── utils/        # 工具函数
├── tests/            # 单元测试
└── requirements.txt
```

## 快速开始

```bash
# 安装依赖（不随包提供第三方库，请自行 pip install）
pip install -r requirements.txt

# 运行
python -m src.main

# 测试
pytest tests/ -v
```

## 三套环境

| 环境 | 启动方式 | 用途 |
|------|---------|------|
| dev  | `python -m src.main --dev` | 日常开发调试 |
| test | `pytest tests/ -v` | CI 集成测试 |
| prod | `python -m src.main --prod` | 答辩演示 |
