"""数据集管理单元测试"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.dataset import SegDataset


def test_scan_empty_dir():
    """空目录扫描应返回空列表。"""
    with tempfile.TemporaryDirectory() as tmp:
        ds = SegDataset(tmp)
        assert ds.scan() == []
        assert len(ds) == 0


def test_class_names():
    """类别名称应为 6 类地物。"""
    assert len(SegDataset.CLASS_NAMES) == 6
    assert "建筑" in SegDataset.CLASS_NAMES


def test_split_ratio():
    """数据集划分比例正确。"""
    with tempfile.TemporaryDirectory() as tmp:
        img_dir = os.path.join(tmp, "images")
        mask_dir = os.path.join(tmp, "masks")
        os.makedirs(img_dir)
        os.makedirs(mask_dir)
        # 造 10 个假样本
        for i in range(10):
            open(os.path.join(img_dir, f"img_{i:03d}.png"), "w").close()
            open(os.path.join(mask_dir, f"img_{i:03d}.png"), "w").close()
        ds = SegDataset(tmp)
        train, val = ds.split(val_ratio=0.2)
        assert len(train) == 8
        assert len(val) == 2
