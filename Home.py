import streamlit as st



st.title("Team Himalaya", anchor=False)
st.divider()

st.write("Hi! This is our official submission for the HackMatrix 2024 Hackathon!")
st.write("This is a AI enabled expense tracker.")

st.markdown("""
`Features`
- Uses Speech to Text and NLP to identify keywords within a user's sentence.
- Visualize and understand your spending better (Coming Soon!)
- Get investment recommendations according to your income
""")
st.divider()

# col1, col2, col3, col4 = st.columns(4)

st.code("Pratham Powar (pspiagicw)")
st.link_button("Github", "https://github.com/pspiagicw")

st.code("Arnav Tatewar")
st.link_button("Github", "link here")

st.code("Prithviraj More")
st.link_button("Github", "link here")

st.code("Vedant Hirekar")
st.link_button("Github", "link here")
