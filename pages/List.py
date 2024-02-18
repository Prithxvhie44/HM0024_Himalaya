import streamlit as st
import pandas as pd


st.title("Your logged expenses!")
st.divider()
database = pd.read_csv("database.csv", index_col=[0])

st.table(database)


