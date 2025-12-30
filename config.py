import os

DATA_CSV_PATH = os.getenv("DATA_CSV_PATH", "data/online_retail.csv")
INGEST_BATCH_SIZE = int(os.getenv("INGEST_BATCH_SIZE", "1000"))

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_NAME")