import streamlit as st
from sidebar import generateSideBar 

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False or st.session_state['authentication_status'] == None:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

st.header("Expenditure Forecasting is work in progress")
