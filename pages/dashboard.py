import streamlit as st
from sidebar import generateSideBar
import matplotlib
from database import getData
from millify import millify

st.set_page_config(page_title="Dashboard", layout='centered')


if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False or st.session_state['authentication_status'] == None:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

_, col2, _ = st.columns(3)


data = getData()

