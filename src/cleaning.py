from __future__ import annotations

import pandas as pd
import numpy as np


def report_missing(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum().sort_values(ascending=False)


def drop_duplicates(df: pd.DataFrame, subset: list[str] | None = None) -> tuple[pd.DataFrame, int]:
    before = len(df)
    cleaned = df.drop_duplicates(subset=subset).reset_index(drop=True)
    return cleaned, before - len(cleaned)


def fix_numeric_types(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    cleaned = df.copy()
    for column in columns:
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors='coerce')
    return cleaned


def fill_numeric_with_median(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    cleaned = df.copy()
    for column in cols:
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].fillna(cleaned[column].median())
    return cleaned


def cap_outliers_iqr(df: pd.DataFrame, col: str, factor: float = 1.5) -> pd.DataFrame:
    cleaned = df.copy()
    q1 = cleaned[col].quantile(0.25)
    q3 = cleaned[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - factor * iqr
    upper = q3 + factor * iqr
    cleaned[col] = cleaned[col].clip(lower=lower, upper=upper)
    return cleaned
