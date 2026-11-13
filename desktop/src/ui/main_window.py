"""主窗口（实验四实现，当前为骨架）"""


class MainWindow:
    """桌面端主窗口，负责影像加载、分割任务触发与结果可视化。"""

    def __init__(self, env="dev"):
        self.env = env
        self.image_path = None
        self.model = None

    def load_image(self, path: str):
        """加载遥感影像。"""
        self.image_path = path
        print(f"[UI] 加载影像: {path}")

    def run_segmentation(self):
        """触发分割推理。"""
        if self.image_path is None:
            print("[UI] 请先加载影像")
            return
        print(f"[UI] 对 {self.image_path} 执行分割...")

    def run(self):
        """启动 GUI 事件循环。"""
        print(f"[UI] 主窗口启动（env={self.env}）")
        print("（GUI 实现见实验四：PyQt5 界面 + OpenCV 显示分割结果）")
