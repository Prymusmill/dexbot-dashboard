import pandas as pd
import streamlit as st
import os
from core.fetch_results import fetch_latest_csv

def show_performance():
    st.subheader("📉 Podgląd danych z pamięci")

    csv_path = fetch_latest_csv()
    if not csv_path:
        st.warning("Nie udało się pobrać danych z bota.")
        return

    try:
        df = pd.read_csv(csv_path)
        if df.empty or len(df.columns) < 2:
            st.warning("Plik CSV nie zawiera poprawnych danych.")
            return
        st.dataframe(df.tail(100))
    except Exception as e:
        st.error(f"Błąd wczytywania: {e}")