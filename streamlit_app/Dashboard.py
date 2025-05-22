# streamlit_app/Dashboard.py

import streamlit as st
import json
import os
import time
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.trade_executor import simulate_trade
from config.settings import load_settings
from core.performance import show_performance

CONFIG_PATH = "config/settings.json"

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

        # 📊 Podgląd skuteczności
        show_performance()

if __name__ == "__main__":
    main()