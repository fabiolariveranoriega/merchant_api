#!/bin/bash
set -e  # Exit if any command fails

echo "Waiting for MySQL to be ready..."

# Python-based wait loop
python - <<END
import os
import time
import mysql.connector

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

while True:
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        break
    except mysql.connector.Error:
        time.sleep(1)
END

echo "MySQL is up!"

# Initialize the database
echo "Initializing database tables..."
python database.py

# Ingest CSV data
echo "Ingesting CSV data..."
python ingest.py

# Start FastAPI
echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
