import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# -----------------------
# NAV HISTORY
# -----------------------

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaned")

# -----------------------
# INVESTOR TRANSACTIONS
# -----------------------

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = txn[
    "transaction_type"
].str.title()

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

# -----------------------
# SCHEME PERFORMANCE
# -----------------------

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")

print("All cleaning completed")