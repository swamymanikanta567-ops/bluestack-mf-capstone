import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

for file in raw_path.glob("*.csv"):

    df = pd.read_csv(file)

    df = df.drop_duplicates()

    df.columns = df.columns.str.strip()

    df.to_csv(
        processed_path / file.name,
        index=False
    )

    print(f"Cleaned: {file.name}")

print("Done!")