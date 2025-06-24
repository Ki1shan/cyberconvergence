import json
import os
from datetime import datetime

RESULT_FILE = "scan_results.json"

def save_results(results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "results": results
    }

    # Load previous data if it exists and is valid
    if os.path.exists(RESULT_FILE):
        try:
            with open(RESULT_FILE, "r") as f:
                data = json.load(f)
            if not isinstance(data, list):
                print("[!] Warning: Corrupt log format. Overwriting.")
                data = []
        except Exception as e:
            print(f"[!] Error reading log file: {e}")
            data = []
    else:
        data = []

    # Append new entry and save
    data.append(log_entry)
    with open(RESULT_FILE, "w") as f:
        json.dump(data, f, indent=4)

