import requests
import json
import zipfile
import os
import pandas as pd
from datetime import datetime
from logger import log_message   # ✅ import from logger.py

def get_kaggle_json_path(kaggle_json_path=None):
    """
    Return the path to kaggle.json. 
    Falls back to project Data Ingestion/kaggle/kaggle.json if not provided.
    """
    if kaggle_json_path is None:
        kaggle_json_path = os.path.join(
            os.path.dirname(__file__),  # folder where this script lives
            "kaggle",
            "kaggle.json"
        )
    return kaggle_json_path

def download_kaggle_dataset(dataset: str, kaggle_json_path=None, base_dir="../3. Raw Data Storage/Kaggle"):
    try:
        kaggle_json_path = get_kaggle_json_path()

        with open(kaggle_json_path) as f:
            creds = json.load(f)
        username, key = creds["username"], creds["key"]

        url = f"https://www.kaggle.com/api/v1/datasets/download/{dataset}"
        log_message(f"Starting download for dataset: {dataset}")

        response = requests.get(url, auth=(username, key), stream=True)
        if response.status_code != 200:
            error_msg = f"Failed to download {dataset}. Status {response.status_code}: {response.text}"
            log_message(error_msg)
            raise Exception(error_msg)

        today = datetime.today()
        datedir = os.path.join(base_dir, str(today.year), f"{today.month:02d}", f"{today.day:02d}")
        os.makedirs(datedir, exist_ok=True)

        zip_path = os.path.join(datedir, "dataset.zip")

        with open(zip_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        log_message(f"Downloaded ZIP file to {zip_path}")

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(datedir)

        csv_files = [f for f in os.listdir(datedir) if f.endswith(".csv")]
        if not csv_files:
            error_msg = f"No CSV file found in dataset {dataset}"
            log_message(error_msg)
            raise Exception(error_msg)

        csv_path = os.path.join(datedir, csv_files[0])
        log_message(f"CSV extracted and saved at {csv_path}")

        return csv_path

    except Exception as e:
        log_message(f"Error occurred: {e}")
        raise
