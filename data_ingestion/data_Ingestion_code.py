from .kaggleWrapper import download_kaggle_dataset
from .huggingfaceWrapper import download_hf_dataset
from .logger import Logger

logger = Logger("Data_Ingestion/data_ingestion.log")

def fetchData():
    logger.log("--------------------------- Kaggle -------------------------------------------")
    try:
        csv_path = download_kaggle_dataset("blastchar/telco-customer-churn", logger)
        logger.log(f"Kaggle churn CSV saved at: {csv_path}")
        print(f"Kaggle churn CSV available at: {csv_path}")
    except Exception as e:
        logger.log(f"❌ Error downloading from Kaggle: {e}")
        print(f"Error downloading from Kaggle: {e}")

    logger.log("--------------------------- Hugging Face -------------------------------------")
    try:
        # csv_path = download_hf_dataset(logger)
        csv_path = ''
        logger.log(f"Hugging Face churn CSV saved at: {csv_path}")
        print(f"Hugging Face churn CSV available at: {csv_path}")
    except Exception as e:
        logger.log(f"❌ Error downloading from Hugging Face: {e}")
        print(f"Error downloading from Hugging Face: {e}")