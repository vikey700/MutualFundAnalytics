import pandas as pd

scheme = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

risk = input(
    "Enter Risk (Low/Moderate/High): "
)

result = scheme[
    scheme["risk_grade"] == risk
]

result = result.sort_values(
    "sharpe_ratio",
    ascending=False
)

print(
    result[
        ["scheme_name","sharpe_ratio"]
    ].head(3)
)