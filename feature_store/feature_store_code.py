import sqlite3
import pandas as pd
import os
from .logger import Logger
from datetime import datetime

def saveData():
    conn = sqlite3.connect("feature_store.db")
    cursor = conn.cursor()

    preparedDataset_path = 'data_transformation'
    csvName = 'prepared_data.csv'
    logger = Logger(fr'feature_store\feature_store.log')

    today = datetime.today().strftime("%Y\\%m\\%d")
    path = os.path.join(preparedDataset_path, "master csv", today, csvName)
    df = pd.read_csv(path)
    logger.log(f"fetched perpared data from {path}")

    df.columns = (
        df.columns.str.strip()       # remove leading/trailing spaces
                .str.replace(" ", "_")  # replace spaces
                .str.replace(r"[()]", "", regex=True)  # remove parentheses
    )

    df.to_sql("feature_store", conn, if_exists="append", index=False)
    logger.log("successfully saved data to feature_store")

    # Commit & close
    conn.commit()
    conn.close()