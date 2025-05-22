# streamlit_app/Dashboard.py
import streamlit as st
import pandas as pd
import os

def show_performance():
    try:
        df = pd.read_csv("data/memory.csv")
        st.subheader("📈 Wyniki symulacji")
        st.dataframe(df.tail(100))
    except FileNotFoundError:
        st.warning("Brak pliku memory.csv")
    except Exception as e:
        st.error(f"Błąd: {e}")

def main():
    st.set_page_config(page_title="DEXBot Dashboard", layout="centered")
    st.title("📊 DEXBot – Wizualizacja")
    st.info("Symulacje działają w tle (Railway), dashboard działa w trybie tylko do odczytu.")
    show_performance()

if __name__ == "__main__":
    main()