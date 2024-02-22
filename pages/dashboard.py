import streamlit as st
from sidebar import generateSideBar 


if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")


st.header("Welcome to Yafa")
st.text("This is a dashboard, info about the project and basic metrics can be shown.")
generateSideBar()

