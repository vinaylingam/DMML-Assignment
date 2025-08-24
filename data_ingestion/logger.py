# logger.py
import os
from datetime import datetime

class Logger:
    def __init__(self, log_file="Data_Ingestion/data_ingestion.log"):
        """
        Initialize Logger with a log file path.
        Ensures directory exists.
        """
        self.log_file = log_file
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def log(self, message: str):
        """Append a log message with timestamp to the log file."""
        with open(self.log_file, "a", encoding="utf-8") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] {message}\n")
