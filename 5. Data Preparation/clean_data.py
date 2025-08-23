import pandas as pd
from logger import Logger

def clean_data(df: pd.DataFrame, logger: Logger) -> pd.DataFrame:
    try:
        logger.log("Starting data cleaning")

        cleaned_df = df.copy()

        # 1. Drop duplicate rows
        dup_count = cleaned_df.duplicated().sum()
        if dup_count > 0:
            cleaned_df = cleaned_df.drop_duplicates()
            logger.log(f"Removed {dup_count} duplicate rows")

        # 2. Handle missing values
        for col in cleaned_df.columns:
            if cleaned_df[col].isnull().sum() > 0:
                if cleaned_df[col].dtype in ["int64", "float64"]:
                    median_val = cleaned_df[col].median()
                    cleaned_df[col] = cleaned_df[col].fillna(median_val)
                    logger.log(f"Filled nulls in numeric column '{col}' with median ({median_val})")
                else:
                    mode_val = cleaned_df[col].mode()[0]
                    cleaned_df[col] = cleaned_df[col].fillna(mode_val)
                    logger.log(f"Filled nulls in categorical column '{col}' with mode ('{mode_val}')")

        # 3. Handle negative values (for numeric columns where negatives don't make sense)
        for col in cleaned_df.select_dtypes(include=["int64", "float64"]).columns:
            neg_count = (cleaned_df[col] < 0).sum()
            if neg_count > 0:
                cleaned_df.loc[cleaned_df[col] < 0, col] = 0
                logger.log(f"Replaced {neg_count} negative values in column '{col}' with 0")

        logger.log("Data cleaning completed successfully")
        return cleaned_df

    except Exception as e:
        logger.log(f"Data cleaning failed: {e}")
        raise
