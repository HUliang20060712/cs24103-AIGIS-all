"""模型训练流程（实验四实现，当前为骨架）"""
import os


class Trainer:
    """U-Net 迁移学习训练器。

    负责：数据集加载 → 模型构建 → 训练循环 → 验证 → checkpoint 保存。
    支持断点续训：从 checkpoints/ 目录恢复最近权重。
    """

    def __init__(self, config: dict):
        self.config = config
        self.epochs = config.get("training", {}).get("epochs", 50)
        self.lr = config.get("training", {}).get("lr", 0.001)
        self.checkpoint_dir = config.get("training", {}).get("checkpoint_dir", "checkpoints/")

    def build_model(self):
        """构建分割模型（实验四接入 PyTorch）。"""
        print("[Trainer] 构建 U-Net 模型（实验四实现）")
        return None

    def train(self, train_dataset, val_dataset):
        """执行训练循环。"""
        print(f"[Trainer] 开始训练，epochs={self.epochs}，"
              f"train={len(train_dataset)}，val={len(val_dataset)}")
        for epoch in range(1, self.epochs + 1):
            # 实验四：loss/accuracy 记录
            if epoch % 10 == 0:
                print(f"  epoch {epoch}/{self.epochs}")
        print("[Trainer] 训练完成（骨架）")

    def save_checkpoint(self, path: str = None):
        """保存模型权重。"""
        path = path or os.path.join(self.checkpoint_dir, "last.pth")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(f"[Trainer] 保存 checkpoint: {path}")
