from abc import ABC, abstractmethod
import os 
import mysql.connector
from config import HOST, PORT, USER, PASSWORD, DATABASE

class Database(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError("Constructor not implemented.")
    
    @abstractmethod
    def get_connection(self):
        raise NotImplementedError("get_connection not implemented.")
    
class MySQL(Database):
    def __init__(self):
        conn = self.get_connection()
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

    def get_connection(self):
        return mysql.connector.connect(
            host = HOST,
            port = PORT,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )
    
if __name__ == "__main__":
    db = MySQL()
        