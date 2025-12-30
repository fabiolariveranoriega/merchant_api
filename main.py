import pandas as pd
import numpy as np
from fastapi import FastAPI
from ingest import ingest_to_db
from data_loader import load_transactions_df
from data_validation import TransactionValidation as Validation

app = FastAPI(title="E-Commerce Transactions API")


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/transactions")
def transactions(
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int = 1000,
):
    df = load_transactions_df()
    data = df.copy()

    if start_date and end_date:
        start_dt = pd.to_datetime(start_date, dayfirst=True, errors="coerce")
        end_dt = pd.to_datetime(end_date, dayfirst=True, errors="coerce")

        data = data[
            (data["InvoiceDate"] >= start_dt)
            & (data["InvoiceDate"] <= end_dt)
        ]

    return Validation.validate(data.head(limit))


@app.post("/ingest")
def ingest(limit: int = 1000):
    ingest_to_db(limit)
    return {"status": "success", "rows_ingested": limit}
