import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"Číslo": 1, "Téma": "Moduly"},
        {"Číslo": 2, "Téma": "Funkce"},
        {"Číslo": 3, "Téma": "Slovníky"},
    ]
)
st.dataframe(df)
