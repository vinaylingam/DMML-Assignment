import pandas as pd
import os
from logger import Logger

def validate_and_report(df: pd.DataFrame, report_path: str, logger: Logger):
    try:
        logger.log("Starting data validation")

        # Missing values
        missing = df.isnull().sum()

        # Data types
        data_types = df.dtypes

        # Negative values check (only for numeric columns)
        negative_values = {}
        for col in df.select_dtypes(include=["int64", "float64"]).columns:
            negative_values[col] = (df[col] < 0).sum()
        negative_series = pd.Series(negative_values)

        # Duplicate rows
        duplicate_count = df.duplicated().sum()

        # Build report DataFrame
        report = pd.DataFrame({
            "missing_values": missing,
            "data_types": data_types,
            "negative_values": negative_series
        }).fillna(0)

        # Add duplicate info (same for all rows)
        report["duplicate_rows"] = duplicate_count

        # Save to Excel
        report_dir = os.path.dirname(report_path)
        os.makedirs(report_dir, exist_ok=True)
        report.to_excel(report_path, index=True)
        logger.log(f"Validation report saved to {report_path}")

    except Exception as e:
        logger.log(f"Validation failed: {e}")
        raise