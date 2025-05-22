# core/trade_executor.py

import csv
import os
from datetime import datetime
import random

def simulate_trade(settings):
    # Prosta symulacja — losowy wynik
    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "success": random.choice([True, False]),
        "profit_usd": round(random.uniform(-1, 1), 2),
    }

    os.makedirs("data", exist_ok=True)
    file_path = "data/memory.csv"
    write_header = not os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=result.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(result)

    print(f"💾 Zapisano wynik: {result}")