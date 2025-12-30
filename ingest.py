from data_loader import load_transactions_df
from database import MySQL as Database
from config import INGEST_BATCH_SIZE
import pandas as pd



def ingest_to_db():
    df = load_transactions_df()

    db = Database()
    conn = db.get_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT IGNORE INTO transactions
    (InvoiceNo, StockCode, Description, Quantity, InvoiceDate,
     UnitPrice, CustomerID, Country)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    rows = []
    total_inserted = 0

    for _, row in df.iterrows():
        rows.append((
            row["InvoiceNo"],
            row["StockCode"],
            row["Description"] if pd.notna(row["Description"]) else None,
            int(row["Quantity"]),
            row["InvoiceDate"] if pd.notna(row["InvoiceDate"]) else None,
            float(row["UnitPrice"]),
            int(row["CustomerID"]) if pd.notna(row["CustomerID"]) else None,
            row["Country"] if pd.notna(row["Country"]) else None,
        ))

        if len(rows) == INGEST_BATCH_SIZE:
            cursor.executemany(insert_query, rows)
            conn.commit()
            total_inserted += len(rows)
            print(f"Inserted {total_inserted} rows...")
            rows = []

    if rows:
        cursor.executemany(insert_query, rows)
        conn.commit()
        total_inserted += len(rows)

    print(f"Ingestion is complete. Total rows inserted: {total_inserted}")

    cursor.close()
    conn.close()
