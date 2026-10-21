# micrograd 伴学

视频：[The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0)。
官方课程：[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)。

## 环境

在仓库根目录执行：

```bash
uv sync
uv run jupyter lab
```

打开 `study/01_derivatives.ipynb`。依赖由 `pyproject.toml` 管理，`uv.lock` 锁定版本；uv 将本地 micrograd 以可编辑方式安装，因此在 notebook 中也能导入。VS Code 可选择本仓库 `.venv/bin/python` 作为 notebook 内核。

`demo.ipynb` 使用 NumPy、Matplotlib、scikit-learn；`trace_graph.ipynb` 使用 Graphviz。Python 的 `graphviz` 包由 uv 安装，渲染还需要系统 `dot` 命令，macOS 可执行 `brew install graphviz`。

```bash
uv run pytest -q
```

原仓库测试用 PyTorch 验证 micrograd 的数值及梯度。micrograd 本身是纯 Python 标量引擎，不需要 GPU。

## 学习顺序

| 阶段 | 动手目标 | 对照源码 |
| --- | --- | --- |
| 1. 导数与偏导数 | 预测方向，再用有限差分验证 | `study/01_derivatives.ipynb` |
| 2. 计算图 | 自己写 `Value` 的加法与乘法，记录父节点 | `micrograd/engine.py` |
| 3. 链式法则 | 手算梯度，再实现局部 `_backward` | `micrograd/engine.py` |
| 4. 自动反向传播 | 理解拓扑排序和共享节点的梯度累加 | `Value.backward` |
| 5. 神经网络 | 从神经元组装 Layer 和 MLP | `micrograd/nn.py` |
| 6. 训练 | 前向、损失、清零、反向、更新参数 | `demo.ipynb` |

每次学习一小段：解释直觉 → 手算 → 运行 → 修改实验 → 回答一个问题。当前仓库的激活函数是 ReLU，视频过程中的 tanh 示例与最终代码存在差异。

先完成第一课，再按理解情况创建后续练习。
