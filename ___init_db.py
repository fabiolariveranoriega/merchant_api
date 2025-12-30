from ___db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        InvoiceNo VARCHAR(20),
        StockCode VARCHAR(20),
        Description TEXT,
        Quantity INT,
        InvoiceDate DATETIME,
        UnitPrice FLOAT,
        CustomerID INT,
        Country VARCHAR(100),
        PRIMARY KEY (InvoiceNo, StockCode)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
