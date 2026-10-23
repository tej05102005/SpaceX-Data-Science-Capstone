"""Download SpaceX API launch records and save a raw JSON snapshot and CSV."""
from pathlib import Path
import json
import requests
import pandas as pd

OUT = Path("data")
OUT.mkdir(exist_ok=True)
URL = "https://api.spacexdata.com/v4/launches/past"

def main():
    response = requests.get(URL, timeout=45)
    response.raise_for_status()
    records = response.json()
    (OUT / "launches_past_raw.json").write_text(
        json.dumps(records, indent=2), encoding="utf-8"
    )
    df = pd.json_normalize(records)
    df.to_csv(OUT / "launches_past_normalized.csv", index=False)
    print("Retrieved records:", len(df))
    print("Columns:", list(df.columns))
    print("Saved data/launches_past_raw.json and data/launches_past_normalized.csv")

if __name__ == "__main__":
    main()
