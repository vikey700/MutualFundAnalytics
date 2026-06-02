import requests
import pandas as pd

codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in codes:

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])

    filename = f"data/raw/{code}.csv"

    df.to_csv(filename, index=False)

    print(f"{code} saved")