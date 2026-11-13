"""训练数据集管理：遥感影像样本导入、划分、加载"""
import os
import glob


class SegDataset:
    """语义分割数据集，管理遥感影像与对应标注掩码。

    目录结构约定：
        sample_dir/
            images/   # 原始遥感影像（.tif/.png/.jpg）
            masks/    # 标注掩码（同名 .png，像素值=类别索引）
    """

    CLASS_NAMES = ["建筑", "植被", "水体", "道路", "裸地", "其他"]

    def __init__(self, sample_dir: str):
        self.sample_dir = sample_dir
        self.image_dir = os.path.join(sample_dir, "images")
        self.mask_dir = os.path.join(sample_dir, "masks")
        self.images = []
        self.masks = []

    def scan(self):
        """扫描样本目录，返回 (image_path, mask_path) 对列表。"""
        if not os.path.isdir(self.image_dir):
            return []
        exts = ("*.tif", "*.tiff", "*.png", "*.jpg", "*.jpeg")
        pairs = []
        for ext in exts:
            for img_path in sorted(glob.glob(os.path.join(self.image_dir, ext))):
                base = os.path.splitext(os.path.basename(img_path))[0]
                mask_path = os.path.join(self.mask_dir, base + ".png")
                if os.path.exists(mask_path):
                    pairs.append((img_path, mask_path))
        self.images = [p[0] for p in pairs]
        self.masks = [p[1] for p in pairs]
        return pairs

    def split(self, val_ratio: float = 0.2):
        """按比例划分训练/验证集。"""
        pairs = self.scan()
        n = len(pairs)
        if n == 0:
            return [], []
        n_val = max(1, int(n * val_ratio))
        return pairs[n_val:], pairs[:n_val]

    def __len__(self):
        return len(self.images)
