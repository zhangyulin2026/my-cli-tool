# my-cli-tool

一个最简单的 Python CLI 入门骨架，clone 下来装好就能跑。

## 项目结构

```
my-cli-tool/
├── pyproject.toml              # 项目配置（依赖、命令入口都在这里）
├── src/
│   └── my_cli_tool/
│       ├── __init__.py         # 包信息（版本号）
│       └── __main__.py         # 命令行入口（argparse 示例）
├── .gitignore
└── LICENSE
```

## 快速开始

### 1. 克隆到本地

```bash
git clone https://github.com/zhangyulin2026/my-cli-tool.git
cd my-cli-tool
```

### 2.（可选）建个虚拟环境

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. 以「可编辑模式」安装

```bash
pip install -e .
```

这一步会读 `pyproject.toml`，把 `my-cli-tool` 这个命令注册到你的系统里。

### 4. 跑起来

```bash
# 直接敲命令
my-cli-tool
# 输出：你好，世界！这是 my-cli-tool 👋

# 带参数
my-cli-tool --name 豆豆
# 输出：你好，豆豆！这是 my-cli-tool 👋

# 看帮助
my-cli-tool --help

# 看版本
my-cli-tool --version
```

不想安装也能跑：

```bash
python -m my_cli_tool
```

## 接下来可以学什么

- 改 `src/my_cli_tool/__main__.py`，加新的命令行参数
- 在 `pyproject.toml` 的 `dependencies` 里加第三方库（比如 `click`、`rich`）
- 拆分子命令（`my-cli-tool add ...` / `my-cli-tool list ...`）
- 加测试：新建 `tests/` 目录，用 `pytest`

## License

MIT
