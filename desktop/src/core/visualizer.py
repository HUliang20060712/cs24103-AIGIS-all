"""分割结果可视化：类别叠加、图例导出、面积统计"""
import os


# 6 类地物的 BGR 配色（与 dataset.CLASS_NAMES 对应）
CLASS_COLORS = {
    0: (0, 0, 255),      # 建筑 - 红
    1: (0, 255, 0),      # 植被 - 绿
    2: (255, 0, 0),      # 水体 - 蓝
    3: (0, 255, 255),    # 道路 - 黄
    4: (139, 69, 19),    # 裸地 - 棕
    5: (128, 128, 128),  # 其他 - 灰
}


class Visualizer:
    """分割结果可视化工具。"""

    @staticmethod
    def overlay(image, mask, alpha: float = 0.5):
        """将分割掩码以半透明叠加到原图上（实验四用 OpenCV 实现）。"""
        print("[Visualizer] 生成叠加图（实验四实现）")
        return image

    @staticmethod
    def compute_area_ratio(mask):
        """统计各地物类别像素占比。"""
        # 实验四：numpy 统计每类像素数 / 总像素
        return {i: 0.0 for i in range(6)}

    @staticmethod
    def export_legend(output_path: str):
        """导出类别图例 PNG。"""
        print(f"[Visualizer] 图例导出至: {output_path}")
