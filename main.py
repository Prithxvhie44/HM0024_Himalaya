import streamlit as st
from streamlit_authenticator.exceptions import RegisterError
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from database import getData
import numpy as np

st.set_page_config(page_title="Home", layout='centered')

with open('config.yaml') as authfile:
    config = yaml.load(authfile, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

def saveConfig():
    with open("config.yaml", 'w') as authfile:
        yaml.dump(config, authfile, default_flow_style=False)

data = getData()

_, col2, _ = st.columns(3)

col2.image('resources/logo.jpeg')
st.divider()

st.markdown("> ### `Money Is Hard`")
st.write("We know this better than anyone")
st.markdown("That's why we built *`yafa`*")
st.markdown("A simple, efficient way of managing your finances")
st.divider()

st.markdown("#### More than 50% of India's youngsters are financially illiterate ")
st.markdown("""> Help us spread awareness about investments, savings and ultimately `Financial Freedom`. Knowledge about mutual funds, stocks and planning about financial goals make your money game unbeatable.""")
st.divider()

st.code("""
        Get started now!
        """)

name, status, username = authenticator.login(location='sidebar')

if status == True:
    st.toast("Logged in!")
    st.switch_page("pages/view.py")
elif status == False:
    st.error("incorrect username/password")

try:
    email, username, name = authenticator.register_user(preauthorization=False)
    if email:
        saveConfig()
        st.success("User created successfully. Please log in.")
except RegisterError as e:
    st.error(str(e))

#

# st.title("Team Himalaya", anchor=False)
# st.divider()
#
# st.write("Hi! This is our official submission for the HackMatrix 2024 Hackathon!")
# st.write("This is a AI enabled expense tracker.")
#
# st.markdown("""
# `Features`
# - Uses Speech to Text and NLP to identify keywords within a user's sentence.
# - Visualize and understand your spending better (Coming Soon!)
# - Get investment recommendations according to your income
# """)
# st.divider()
#
# # col1, col2, col3, col4 = st.columns(4)
#
# st.code("Pratham Powar (pspiagicw)")
# st.link_button("Github", "https://github.com/pspiagicw")
#
# st.code("Arnav Tatewar")
# st.link_button("Github", "link here")
#
# st.code("Prithviraj More")
# st.link_button("Github", "https://github.com/Prithxvhie44")
#
# st.code("Vedant Hirekar")
# st.link_button("Github", "link here")
