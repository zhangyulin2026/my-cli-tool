"""my-cli-tool 命令行入口。

运行方式：
    python -m my_cli_tool            # 模块方式（未安装也能跑）
    my-cli-tool                      # 安装后命令方式
    my-cli-tool --name 世界          # 带参数
    my-cli-tool --version            # 查看版本
"""
import argparse

from . import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="my-cli-tool",
        description="一个最简单的 Python CLI 入门示例",
    )
    parser.add_argument(
        "--name",
        default="世界",
        help="要打招呼的名字（默认：世界）",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    args = parser.parse_args()

    print(f"你好，{args.name}！这是 my-cli-tool 👋")


if __name__ == "__main__":
    main()
