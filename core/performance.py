import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://dexbot-worker-production.up.railway.app/results/"

def get_latest_csv_url():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        links = [a.get("href") for a in soup.find_all("a") if a.get("href", "").endswith(".csv")]
        if not links:
            return None

        latest = sorted(links)[-1]  # Zakładamy, że nazwa pliku zawiera timestamp
        return BASE_URL + latest
    except Exception as e:
        st.error(f"Błąd podczas pobierania listy CSV: {e}")
        return None

def load_csv_from_url(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Błąd podczas wczytywania pliku CSV: {e}")
        return None

def show_performance():
    st.subheader("\ud83d\udcca Podgląd danych z symulacji (z serwera)")

    csv_url = get_latest_csv_url()
    if not csv_url:
        st.warning("Brak plików CSV do wyświetlenia.")
        return

    df = load_csv_from_url(csv_url)
    if df is not None and not df.empty:
        st.success(f"Załadowano dane z: {csv_url}")
        st.dataframe(df.tail(100))
    else:
        st.warning("Plik CSV jest pusty lub nieprawidłowy.")