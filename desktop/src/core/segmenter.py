"""分割推理：加载模型，对单张/批量遥感影像执行地物分类"""
import os


class SegResult:
    """单张影像的分割结果。"""
    def __init__(self, image_path: str, output_path: str, class_counts: dict = None):
        self.image_path = image_path
        self.output_path = output_path
        self.class_counts = class_counts or {}


class Segmenter:
    """遥感影像语义分割推理器。

    实验四实现：加载 .pth 权重 → OpenCV 读图 → 预处理 → 模型推理 → 后处理 → 叠加可视化。
    CPU/GPU 自适应：检测不到 CUDA 时自动切换轻量 MobileNetV2 编码器。
    """

    def __init__(self, env: str = "dev", model_path: str = None):
        self.env = env
        self.model_path = model_path
        self.model = None
        self.device = "cpu"

    def load_model(self):
        """加载模型权重（实验四实现）。"""
        print(f"[Segmenter] 加载模型: {self.model_path} (env={self.env})")
        # 实验四：torch.load + .eval()
        # CUDA 检测：torch.cuda.is_available()
        # 无 GPU 时切换轻量分支（创新点 I-3）
        return self

    def predict(self, image_path: str) -> SegResult:
        """对单张遥感影像执行分割，返回 SegResult。"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"影像不存在: {image_path}")
        print(f"[Segmenter] 推理: {image_path}")
        # 实验四：
        #   img = cv2.imread(image_path)
        #   tensor = preprocess(img)
        #   logits = self.model(tensor)
        #   mask = postprocess(logits)
        #   overlay = blend(img, mask)
        #   cv2.imwrite(output_path, overlay)
        output_path = os.path.splitext(image_path)[0] + "_seg.png"
        return SegResult(image_path, output_path)

    def predict_batch(self, image_dir: str):
        """批量分割目录下所有影像。"""
        results = []
        for fname in sorted(os.listdir(image_dir)):
            if fname.lower().endswith((".png", ".tif", ".tiff", ".jpg")):
                results.append(self.predict(os.path.join(image_dir, fname)))
        return results
