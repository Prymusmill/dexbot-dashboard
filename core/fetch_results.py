# core/fetch_results.py

import requests
import os
import pandas as pd

DEXBOT_WORKER_URL = "https://dexbot-worker-production.up.railway.app/results/"

def fetch_latest_csv():
    try:
        response = requests.get(DEXBOT_WORKER_URL)
        if response.status_code != 200:
            return None

        # Znajdź nazwę najnowszego pliku
        lines = response.text.splitlines()
        csv_files = [line for line in lines if '.csv' in line]
        if not csv_files:
            return None
        latest_file = csv_files[-1].strip()

        file_url = DEXBOT_WORKER_URL + latest_file
        csv_response = requests.get(file_url)

        if csv_response.status_code == 200:
            csv_path = os.path.join("data", "memory.csv")
            with open(csv_path, "wb") as f:
                f.write(csv_response.content)
            return csv_path
        return None
    except Exception as e:
        print("❌ Błąd podczas pobierania:", e)
        return None