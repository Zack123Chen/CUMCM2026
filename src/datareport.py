import numpy as np
import pandas as pd

def data_check(df):
    report = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_rate": df.isna().mean(),
        "unique_count": df.nunique()
    })
    
    numeric_cols = df.select_dtypes(include="number").columns
    
    report.loc[numeric_cols, "mean"] = df[numeric_cols].mean()
    report.loc[numeric_cols, "std"] = df[numeric_cols].std()
    report.loc[numeric_cols, "min"] = df[numeric_cols].min()
    report.loc[numeric_cols, "max"] = df[numeric_cols].max()
    
    report["missing_rate"] = report["missing_rate"].round(4)
    
    duplicate_count = df.duplicated().sum()
    
    return report, duplicate_count

    