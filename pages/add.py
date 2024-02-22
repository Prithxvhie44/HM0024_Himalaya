import streamlit as st
from audiorecorder import audiorecorder
from speechlib import getPhrase
from nlp import getEntry
import pandas as pd
from datetime import datetime
from sidebar import generateSideBar
from database import addRow

st.set_page_config(page_title="Add Expense", layout="centered")

categories = [
'Education', 'Social Life', 'Transportation', 'Food',
 'Household', 'Money transfer', 'Investment', 'Tourism', 'Health', 'Subscription'
]

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False or st.session_state['authentication_status'] == None:
    st.toast("Not authenticated")
    st.switch_page("main.py")


def predictCategory(tags):
    category = None
    cat = pd.read_csv('data/categories.csv')
    print(cat.head())
    for tag in tags:
        for i in range(len(cat)):
            if tag in cat.iloc[i]['words'].split():
                category = cat.iloc[i]['category']
                break
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


generateSideBar()

# Description
st.title("`Add a Expense` :coin:")
st.divider()
st.write("Record a voicenote to track a expense.")

audio = audiorecorder("🎤", "⏺")


if len(audio) > 0:

    audio.export("audio.wav", format="wav")
    # Using speechlib.py for Speech Recognition
    with st.spinner():
        phrase = getPhrase()

    if phrase == None:
        st.error("Nothing got recorded!")
        st.stop()

    st.info("Given below is the text that got recorded")
    st.code(phrase)
    # Extract tags and amount using NLP. Defined in nlp.py
    tags, amount = getEntry(phrase)

    am = None

    try:
        am = int(amount)
    except:
        st.error("Amount is not int")

    predicted_category = predictCategory(tags)

    index = 0
    if predicted_category in [item.lower() for item in categories]:
        index = [item.lower() for item in categories].index(predicted_category)

    tags = ' '.join(tags)

    if predicted_category != None:
        st.success("A category has been automatically detected!")
    else:
        st.warning("Coouldn't detect a category.Please select manually")
    category = st.selectbox(label="Category", options=categories, index=index)
    
    st.info("Given below are the essential components of your note.")
    st.write(f"- Tags: `{tags}`")
    st.write(f"- Amount: `{amount}`")
    # Button to add to database.
    st.button("Add to database ?", on_click=lambda: addToDatabase(tags, amount, category))

with st.expander("How does it work ?"):
    st.write("1) Record transactions using your voice.")
    st.write("2) Automagically detect the description,amount and category.")
    st.write("3) Add any expense with 3 taps.")




