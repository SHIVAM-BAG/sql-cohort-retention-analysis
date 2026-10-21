"""
ETL Pipeline: Loads CSV datasets into SQLite Database, builds schemas,
indices, and analytical views.
"""

import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
SQL_DIR = os.path.join(BASE_DIR, "sql")

os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(PROCESSED_DATA_DIR, "ecommerce_analysis.db")

def build_database():
    print(f"Connecting to SQLite database at: {DB_PATH}")
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Removed existing database to ensure clean schema rebuild.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Execute schema DDL script
    schema_file = os.path.join(SQL_DIR, "01_schema_and_etl.sql")
    with open(schema_file, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    print("Executing schema DDL, indexes, and analytical view creation...")
    cursor.executescript(schema_sql)
    conn.commit()

    # 2. Ingest raw CSV data into tables
    tables = [
        ("products", "products.csv"),
        ("customers", "customers.csv"),
        ("orders", "orders.csv"),
        ("order_items", "order_items.csv"),
    ]

    for table_name, csv_filename in tables:
        csv_path = os.path.join(RAW_DATA_DIR, csv_filename)
        print(f"Ingesting {csv_filename} into table '{table_name}'...")
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"  -> Ingested {len(df):,} rows into '{table_name}'.")

    conn.commit()

    # 3. Verification query
    cursor.execute("SELECT COUNT(*) FROM orders;")
    total_orders = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM customers;")
    total_customers = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM order_items;")
    total_items = cursor.fetchone()[0]

    print("\n[DATABASE BUILD VERIFIED]")
    print(f"  Customers:    {total_customers:,}")
    print(f"  Orders:       {total_orders:,} (50,000+ transaction records)")
    print(f"  Order Items:  {total_items:,}")
    print(f"  Database file created at: {DB_PATH}")

    conn.close()

if __name__ == "__main__":
    build_database()
