import numpy as np


def standardize(X):
    """按列进行 Z-score 标准化。"""
    X = np.asarray(X, dtype=float)

    if X.ndim != 2:
        raise ValueError("X必须是二维数组")

    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)

    if np.any(np.isclose(std, 0)):
        raise ValueError("存在标准差为0的列，无法标准化")

    return (X - mean) / std