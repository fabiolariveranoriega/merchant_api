# data_loader.py
import pandas as pd
import numpy as np
from functools import lru_cache
from config import DATA_CSV_PATH


@lru_cache(maxsize=1)
def load_transactions_df() -> pd.DataFrame:
    df = pd.read_csv(
        DATA_CSV_PATH,
        encoding="ISO-8859-1"
    )

    df.columns = df.columns.str.strip()

    numeric_cols = ["Quantity", "UnitPrice"]

    df[numeric_cols] = df[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    )

    df[numeric_cols] = (
        df[numeric_cols]
        .replace([np.inf, -np.inf], np.nan)
        .fillna(0)
        .clip(lower=-10000, upper=10000)
        .astype(np.float32)
    )

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        format="%m/%d/%Y %H:%M",
        errors="coerce"
    )

    return df
