"""IO 工具：影像读写、配置加载、路径管理"""
import os
import yaml


def load_config(config_path: str = "config/config.yaml") -> dict:
    """加载 YAML 配置文件。"""
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_dir(path: str):
    """确保目录存在。"""
    os.makedirs(path, exist_ok=True)
    return path


def list_images(directory: str):
    """列出目录下所有影像文件。"""
    exts = (".png", ".jpg", ".jpeg", ".tif", ".tiff")
    return [
        os.path.join(directory, f)
        for f in sorted(os.listdir(directory))
        if f.lower().endswith(exts)
    ]
