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

def generateSideBar():
    st.sidebar.page_link(label="Add Expense",page="pages/dashboard.py")
    authenticator.logout(location='sidebar')


