# logger.py
import os
from datetime import datetime

def log_message(message: str, log_file="../2. Data Ingestion/data_ingestion.log"):
    """Append log messages with timestamp to a log file. Creates directory/file if missing."""
    
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Append log entry
    with open(log_file, "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")
