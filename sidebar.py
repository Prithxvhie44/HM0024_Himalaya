import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

with open('config.yaml') as authfile:
    config = yaml.load(authfile, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


def logoutUser():
    st.switch_page("main.py")

def generateSideBar():
    st.sidebar.page_link(label="Add",page="pages/add.py")
    st.sidebar.page_link(label="View", page="pages/view.py")
    st.sidebar.page_link(label="Invest", page="pages/invest.py")
    st.sidebar.page_link(label="Forecast", page="pages/forecast.py")
    st.sidebar.button(label="Logout", on_click=logoutUser)

