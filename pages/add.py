import streamlit as st
from audiorecorder import audiorecorder
from speechlib import getPhrase
from nlp import getEntry
import pandas as pd
from datetime import datetime
from sidebar import generateSideBar
from database import addRow


categories = [
'Culture', 'Education', 'Self-development', 'Grooming', 'Family', 'Social Life', 'Transportation', 'Food',
 'Apparel', 'Household', 'Festivals', 'Money transfer', 'Investment', 'Other', 'Gift', 'Tourism', 'Health', 'Subscription', 'Rent'
]

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False or st.session_state['authentication_status'] == None:
    st.toast("Not authenticated")
    st.switch_page("main.py")

st.set_page_config(page_title="Add Expense")
generateSideBar()

# Description
st.title("Add a expense")

st.write("")
st.header("Use the below button to record a expense")
st.divider()

def predictCategory(tags):
    category = None
    cat = pd.read_csv('categories.csv')
    print(cat.head())
    for tag in tags:
        for i in range(len(cat)):
            if tag in cat.iloc[i]['words'].split():
                category = cat.iloc[i]['category']
    return category

def addToDatabase(description, amount, category):
    am = 0

    try:
        am = int(amount)
    except:
        st.error("Amount not a int")

    dt = datetime.now()
    date = dt.strftime("%d-%m-%Y")

    addRow(
            date=date,
            username=st.session_state['username'],
            description=description,
            category=category,
            amount = am,
        )
    st.success("Successfully added to the database! Use the other tabs to explore more about your financial spending.")



audio = audiorecorder("Start Recording", "Stop Recording")


if len(audio) > 0:

    audio.export("audio.wav", format="wav")
    # Using speechlib.py for Speech Recognition
    with st.spinner():
        phrase = getPhrase()

    if phrase == None:
        st.error("Nothing got recorded!")
        st.stop()

    st.info("Given below is the text that got recorded")
    st.text(phrase)
    # Extract tags and amount using NLP. Defined in nlp.py
    tags, amount = getEntry(phrase)

    am = None

    try:
        am = int(amount)
    except:
        st.error("Amount is not int")

    st.info("Given below are the essential components of your sentence.")
    predicted_category = predictCategory(tags)

    index = 0
    if predicted_category in [item.lower() for item in categories]:
        index = [item.lower() for item in categories].index(predicted_category)

    tags = ' '.join(tags)

    category = st.selectbox(label="Category", options=categories, index=index)
    
    st.write(f"Tags: `{tags}`")
    st.write(f"Amount: `{amount}`")
    # Button to add to database.
    st.button("Add to database ?", on_click=lambda: addToDatabase(tags, amount, category))



