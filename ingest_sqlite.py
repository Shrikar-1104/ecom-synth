import os
import sqlite3

import pandas as pd

DATA_DIR = "data"
DB_PATH = "ecom.db"
CSV_FILES = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "order_items.csv",
    "payments.csv",
]


def load_csvs_to_sqlite():
    conn = sqlite3.connect(DB_PATH)
    try:
        for csv_file in CSV_FILES:
            table_name = os.path.splitext(csv_file)[0]
            csv_path = os.path.join(DATA_DIR, csv_file)
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Loaded {table_name} into {DB_PATH}")
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    load_csvs_to_sqlite()

