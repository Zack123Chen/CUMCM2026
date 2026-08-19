from sklearn.linear_model import LinearRegression


def fit_linear_regression(X_train, y_train):
    """
    训练线性回归模型。

    Parameters
    ----------
    X_train : DataFrame
        训练集自变量。
    y_train : Series
        训练集因变量。

    Returns
    -------
    model : LinearRegression
        已完成拟合的线性回归模型。
    """

    # 1. 创建线性回归模型
    model = LinearRegression()

    # 2. 使用训练数据拟合模型
    model.fit(X_train, y_train)

    # 3. 返回训练完成的模型
    return model
