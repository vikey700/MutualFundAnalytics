-- 1. Top 5 funds by expense ratio

SELECT scheme_name, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 2. Average NAV

SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Total transaction amount

SELECT SUM(amount_inr) AS total_amount
FROM fact_transactions;

-- 4. Transactions by KYC status

SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- 5. Funds with expense ratio < 1%

SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 1 year return

SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 7. Top 5 funds by 5 year return

SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 8. Transaction count by state

SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 9. Highest NAV

SELECT MAX(nav)
FROM fact_nav;

-- 10. Lowest NAV

SELECT MIN(nav)
FROM fact_nav;