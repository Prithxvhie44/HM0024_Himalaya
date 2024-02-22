import streamlit as st
import pandas as pd
from sidebar import generateSideBar 
from database import getData

st.set_page_config(layout='wide')

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

st.title("Your logged expenses!")
st.divider()
database = getData()

df = database[database['username'] == st.session_state['username']]

st.table(df)


