import streamlit as st
import pandas as pd
from sidebar import generateSideBar 

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

st.title("Your logged expenses!")
st.divider()
database = pd.read_csv("database.csv", index_col=[0])

st.table(database)


