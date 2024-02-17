import streamlit as st

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.ibb.co/Cs449rG/florian-delee-Olgz-U9-Ka-Akg-unsplash.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Team HIMALAYAS", anchor=False)
st.divider()

st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.subheader("Member 1")
col1.link_button("Github", "link here")

col2.subheader("Member 2")
col2.link_button("Github", "link here")

col3.subheader("Member 3")
col3.link_button("Github", "link here")

col4.subheader("Member 4")
col4.link_button("Github", "link here")
