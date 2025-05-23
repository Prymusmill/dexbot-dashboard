import pandas as pd
import streamlit as st
import os

def show_performance():
    memory_path = os.path.join(os.path.dirname(__file__), "..", "data", "memory.csv")

    try:
        if not os.path.exists(memory_path):
            st.warning("Plik memory.csv nie istnieje.")
            return

        df = pd.read_csv(memory_path)

        if df.empty or len(df.columns) < 2:
            st.warning("Plik memory.csv istnieje, ale jest pusty lub nie zawiera poprawnych danych.")
            return

        st.subheader("📉 Podgląd danych z pamięci")
        st.dataframe(df.tail(100))

    except Exception as e:
        st.error(f"Wystąpił błąd podczas ładowania danych: {e}")