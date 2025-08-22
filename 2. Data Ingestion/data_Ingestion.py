from kaggleWrapper import download_kaggle_dataset
from huggingfaceWrapper import download_hf_dataset
from logger import log_message

if __name__ == "__main__":
    log_message("--------------------------- Kaggle -------------------------------------------")
    try:
        csv_path = download_kaggle_dataset("blastchar/telco-customer-churn")
        log_message(f"Kaggle churn CSV saved at: {csv_path}")
        print(f"Kaggle churn CSV available at: {csv_path}")
    except Exception as e:
        log_message(f"❌ Error downloading from Kaggle: {e}")
        print(f"Error downloading from Kaggle: {e}")

    log_message("--------------------------- Hugging Face -------------------------------------")
    try:
        csv_path = download_hf_dataset()
        log_message(f"Hugging Face churn CSV saved at: {csv_path}")
        print(f"Hugging Face churn CSV available at: {csv_path}")
    except Exception as e:
        log_message(f"❌ Error downloading from Hugging Face: {e}")
        print(f"Error downloading from Hugging Face: {e}")
