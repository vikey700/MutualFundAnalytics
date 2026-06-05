import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully")

conn.close()