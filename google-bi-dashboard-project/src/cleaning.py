"""
cleaning.py
Common cleaning functions used by notebooks and scripts.
"""
import pandas as pd
import numpy as np

def report_missing(df):
    return df.isnull().sum()

def drop_duplicates(df, subset=None):
    before = len(df)
    df2 = df.drop_duplicates(subset=subset)
    after = len(df2)
    return df2, before-after

def fill_numeric_with_median(df, cols):
    for c in cols:
        if c in df.columns:
            df[c] = df[c].fillna(df[c].median())
    return df

def cap_outliers_iqr(df, col, factor=1.5):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    low = q1 - factor * iqr
    high = q3 + factor * iqr
    df[col] = df[col].clip(lower=low, upper=high)
    return df
