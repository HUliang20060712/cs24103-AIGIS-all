"""AIGIS 语义分割桌面端入口"""
import argparse
import sys
import os

# 将项目根目录加入 path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def parse_args():
    parser = argparse.ArgumentParser(description="AIGIS 遥感影像语义分割桌面端")
    parser.add_argument("--env", default="dev", choices=["dev", "test", "prod"],
                        help="运行环境（默认 dev）")
    parser.add_argument("--cli", action="store_true",
                        help="命令行模式（不启动 GUI，用于测试与 CI）")
    parser.add_argument("--image", type=str, help="CLI 模式下待分割的遥感影像路径")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"[AIGIS-Segmenter] 启动，环境={args.env}")

    if args.cli:
        # CLI 模式：加载模型对单张影像做分割（实验四实现）
        from src.core.segmenter import Segmenter
        seg = Segmenter(env=args.env)
        if args.image:
            result = seg.predict(args.image)
            print(f"分割完成，结果已保存至: {result.output_path}")
        else:
            print("CLI 模式需指定 --image")
    else:
        # GUI 模式（实验四实现）
        from src.ui.main_window import MainWindow
        app = MainWindow(env=args.env)
        app.run()


if __name__ == "__main__":
    main()
