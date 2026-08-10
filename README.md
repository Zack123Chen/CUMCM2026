
# CUMCM 2026 数学建模工作区

用于 2026 数学建模训练及比赛。

## 项目结构

```text
cumcm2026/
├── data/
│   ├── raw/          # 原始数据
│   └── processed/    # 处理后的数据
├── src/              # Python 源代码
├── figures/          # 论文图片
├── tables/           # 表格
├── outputs/          # 模型输出结果
├── paper/            # LaTeX 论文
├── requirements.txt  # Python 依赖
└── README.md
```

## Python 环境

创建虚拟环境：

```bash
python3 -m venv .venv
```

激活环境：

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

验证 Python：

```bash
python -c "import sys; print(sys.executable)"
```

## Jupyter

VS Code 中选择解释器：

```text
cumcm2026/.venv/bin/python
```

测试 Notebook：

```text
test_environment.ipynb
```

运行后应能够：

- 使用 NumPy / Pandas
- 进行描述性统计
- 导出 Excel
- 生成 Matplotlib 图片

## LaTeX

进入论文目录：

```bash
cd paper
```

使用 XeLaTeX 编译：

```bash
xelatex test.tex
```

输出：

```text
test.pdf
```

