# ecom-synth
This project demonstrates a complete mini data pipeline using synthetic e-commerce data.
It includes data generation, database ingestion, and a multi-table join query—all following an AI-SDLC workflow inside Cursor.
ecom-synth/
│
├── generate_data.py      # Generates 5 synthetic e-commerce CSV files
├── ingest_sqlite.py      # Loads CSVs into SQLite database ecom.db
├── run_query.py          # Executes the SQL join query and prints output
├── query.sql             # Multi-table SQL join query
│
└── data/                 # Folder containing synthetic CSV data
    ├── customers.csv
    ├── products.csv
    ├── orders.csv
    ├── order_items.csv
    └── payments.csv
    
1.Synthetic Data Generation
The script generate_data.py creates 5 CSV files with realistic e-commerce data:
customers.csv – customer profile information
products.csv – product catalog
orders.csv – customer orders
order_items.csv – individual items purchased
payments.csv – payment details per order
The dataset includes:
200 customers
100 products
300 orders

2.Load Data into SQLite
ingest_sqlite.py reads the 5 CSVs and loads them into a SQLite database ecom.db.
Auto-calculated total order amounts

Randomized but realistic fields (names, prices, categories, dates)

3. Multi-Table SQL Query
The file query.sql contains a join across 4 different tables to generate:
customer_name
product_name
category
quantity
total_spent
order_date

4.Requirements
Python 3.8+
pandas
sqlite3
faker
