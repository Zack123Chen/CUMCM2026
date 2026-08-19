import numpy as np

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
)


def regression_metrics(y_true, y_pred):
    """
    计算回归模型的常用评价指标。

    Parameters
    ----------
    y_true : array-like
        真实值。
    y_pred : array-like
        模型预测值。

    Returns
    -------
    metrics : dict
        包含 R²、MAE 和 RMSE。
    """

    # 1. 计算 R²
    r2 = r2_score(y_true, y_pred)

    # 2. 计算 MAE
    mae = mean_absolute_error(y_true, y_pred)

    # 3. 计算 RMSE
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    # 4. 将指标统一放入字典中返回
    return {
        "R2": r2,
        "MAE": mae,
        "RMSE": rmse,
    }
