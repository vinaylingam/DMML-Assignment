import os
import requests
import pandas as pd
from datetime import datetime
from logger import log_message   # your custom logger

def download_hf_dataset():
    url = "https://datasets-server.huggingface.co/rows"
    params = {
        "dataset": "aai510-group1/telco-customer-churn",
        "config": "default",
        "split": "train",
        "offset": 0,
        "length": 100  # batch size
    }

    all_rows = []
    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            log_message(f"Error: HTTP {response.status_code}")
            break

        data = response.json()

        # Stop if no rows returned
        if not data.get("rows"):
            break

        # Extract rows
        rows = [row["row"] for row in data["rows"]]
        all_rows.extend(rows)

        # Update offset for next batch
        params["offset"] += params["length"]

        log_message(f"Downloaded {len(all_rows)} rows so far...")

    if not all_rows:
        log_message("No data downloaded.")
        return None

    # Convert to DataFrame
    df = pd.DataFrame(all_rows)

    # Build save path
    today = datetime.now()
    base_dir = os.path.join(
        "..", "3. Raw Data Storage", "HuggingFace",
        today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")
    )
    os.makedirs(base_dir, exist_ok=True)

    csv_path = os.path.join(base_dir, "telco_customer_churn_full.csv")

    # Save to CSV
    df.to_csv(csv_path, index=False)
    log_message(f"Download complete! Total rows: {len(df)}. Saved to {csv_path}")

    return csv_path
