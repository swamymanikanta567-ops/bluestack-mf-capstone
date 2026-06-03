import pandas as pd
import requests

funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, amfi_code in funds.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    filename = f"data/raw/{fund_name}_nav.csv"

    nav_df.to_csv(filename, index=False)

    print(f"Saved: {filename}")