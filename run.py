import sqlite3

import pandas as pd

DB_PATH = "ecom.db"
QUERY_FILE = "query.sql"


def run_query():
    with open(QUERY_FILE, "r", encoding="utf-8") as file:
        sql = file.read()

    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query(sql, conn)
        print(df.head(20).to_string(index=False))
    finally:
        conn.close()


if __name__ == "__main__":
    run_query()

