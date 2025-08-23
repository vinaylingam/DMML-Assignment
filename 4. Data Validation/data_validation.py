import os
import pandas as pd
from logger import Logger
from datetime import datetime
from validate_and_report import validate_and_report
from clean_data import clean_data

# Assuming Logger class + validate_and_report already defined above

logger = Logger('4. Data Validation/data_validation.log')

today = datetime.today().strftime("%Y\\%m\\%d")

# HuggingFace CSV path & report
huggingface_csv = fr"3. Raw Data Storage\HuggingFace\{today}\customer_churn_dataset.csv"
huggingface_report = fr"4. Data Validation\HuggingFace\{today}"

# Kaggle CSV path & report
kaggle_csv = fr"3. Raw Data Storage\Kaggle\{today}\customer_churn_dataset.csv"
kaggle_report = fr"4. Data Validation\Kaggle\{today}"

def data_validator(input_csv, report_dir):
    try:
        logger.log(f"Pipeline started for {input_csv}")

        # 1. Load CSV
        df = pd.read_csv(input_csv)
        logger.log(f"Loaded CSV with shape {df.shape}")

        # 2. Generate validation report
        report_path = os.path.join(report_dir, "validation_report.xlsx")
        validate_and_report(df, report_path, logger)
        df_cleaned = clean_data(df, logger)

        # 3. Save cleaned CSV back (optional, only if you want to keep a cleaned copy)
        cleaned_path = os.path.join(report_dir, "cleaned.csv")
        df_cleaned.to_csv(cleaned_path, index=False)
        logger.log(f"Cleaned CSV saved to {cleaned_path}")

        logger.log("Pipeline completed successfully")

    except Exception as e:
        logger.log(f"Pipeline failed: {e}")
        raise

data_validator(huggingface_csv, huggingface_report)
data_validator(kaggle_csv, kaggle_report)