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
    st.sidebar.page_link(label="Add Record",page="pages/add.py")
    st.sidebar.page_link(label="Expense Stats ", page="pages/view.py")
    st.sidebar.page_link(label="Investment Stats", page="pages/invest.py")
    st.sidebar.page_link(label="Expense Forecasts", page="pages/forecast.py")
    if st.sidebar.button(label="Logout"):
        st.toast("Logged out!")
        try:
            authenticator.logout(location='unrendered')
        except:
            pass
        st.switch_page("main.py")



