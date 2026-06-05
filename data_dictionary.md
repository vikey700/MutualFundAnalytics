# Mutual Fund Analytics Data Dictionary

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | INTEGER | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund code |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | KYC verification status |

---

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund code |
| scheme_name | TEXT | Fund name |
| fund_house | TEXT | AMC name |
| return_1yr_pct | REAL | 1 year return |
| return_3yr_pct | REAL | 3 year return |
| return_5yr_pct | REAL | 5 year return |
| expense_ratio_pct | REAL | Expense ratio |
| risk_grade | TEXT | Risk category |