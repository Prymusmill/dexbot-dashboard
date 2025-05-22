# streamlit_app/Dashboard.py

import streamlit as st
import json
import os
import time
import sys
import importlib.util

# 🔧 Dynamiczne importy z plików w innych folderach
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# config/settings.json loader
def load_settings():
    try:
        with open(os.path.join(BASE_DIR, "config/settings.json"), "r") as f:
            return json.load(f)
    except Exception as e:
        return {"error": str(e)}

# trade_executor.py
spec_trade = importlib.util.spec_from_file_location(
    "trade_executor", os.path.join(BASE_DIR, "core/trade_executor.py"))
trade_module = importlib.util.module_from_spec(spec_trade)
spec_trade.loader.exec_module(trade_module)
simulate_trade = trade_module.simulate_trade

# performance.py
spec_perf = importlib.util.spec_from_file_location(
    "performance", os.path.join(BASE_DIR, "core/performance.py"))
perf_module = importlib.util.module_from_spec(spec_perf)
spec_perf.loader.exec_module(perf_module)
show_performance = perf_module.show_performance

# 📄 Ścieżka do ustawień
CONFIG_PATH = os.path.join(BASE_DIR, "config/settings.json")

def load_settings_local():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Nie udało się załadować ustawień: {e}")
        return {}

def main():
    st.set_page_config(page_title="DEXBot AI", layout="centered")
    st.title("🤖 DEXBot AI – Dashboard")

    settings = load_settings_local()
    if settings:
        st.subheader("🔧 Ustawienia bota")
        st.json(settings)

        st.subheader("📊 Stan bota")
        st.write("Tryb działania:", settings.get("mode", "brak"))
        st.write("Maks. transakcji/min:", settings.get("max_trades_per_minute", "n/d"))
        st.write("Wielkość transakcji (USD):", settings.get("trade_amount_usd", "n/d"))

        st.subheader("🚦 Status:")
        st.success("Bot działa w trybie ciągłym. Uczenie trwa...")

        # 📊 Wizualizacja skuteczności
        show_performance()

if __name__ == "__main__":
    main()