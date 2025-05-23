import streamlit as st
import pandas as pd
import requests
from io import StringIO

# 👇 Wstaw właściwe repozytorium i gałąź
REPO = "Prymusmill/dexbot-worker"
BRANCH = "main"

def get_latest_csv_url():
    api_url = f"https://api.github.com/repos/{REPO}/contents/data/results"
    response = requests.get(api_url)
    if response.status_code != 200:
        st.error("❌ Nie udało się pobrać listy plików z GitHuba.")
        return None

    files = response.json()
    csv_files = [f for f in files if f["name"].endswith(".csv")]
    if not csv_files:
        st.warning("⚠️ Brak plików CSV w repozytorium.")
        return None

    # Sortuj po nazwie pliku (czyli timestampie w nazwie)
    csv_files.sort(key=lambda x: x["name"], reverse=True)
    return csv_files[0]["download_url"]

def show_performance():
    csv_url = get_latest_csv_url()
    if not csv_url:
        return

    try:
        response = requests.get(csv_url)
        if response.status_code != 200:
            st.error("❌ Nie udało się pobrać pliku CSV.")
            return

        df = pd.read_csv(StringIO(response.text))
        st.subheader("📊 Ostatnie 100 wpisów (z GitHub)")
        st.dataframe(df.tail(100))
    except Exception as e:
        st.error(f"❌ Błąd: {e}")