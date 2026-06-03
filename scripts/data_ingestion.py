import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

csv_files = list(raw_path.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 50)
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")