import streamlit as st
from audiorecorder import audiorecorder
from speechlib import getPhrase
from nlp import getEntry
import pandas as pd
from datetime import datetime
from sidebar import generateSideBar
from database import addRow

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")

st.set_page_config(page_title="Add Expense")
generateSideBar()

# Description
st.title("Add a expense")

st.write("")
st.header("Use the below button to record a expense")
st.divider()

def checkFile():
    # Tries to read the database. If exists, leave it, if no, creates a empty db with 3 columns.
    try:
        pd.read_csv('database.csv')
    except:
        db = pd.DataFrame(columns=['Date', 'Tags', 'Amount'])
        db.to_csv('database.csv')


def addToDatabase(description, amount):
    dt = datetime.now()
    date = dt.date()

    addRow(
            date=date,
            username=st.session_state['username'],
            description=description,
            category='category',
            amount = amount,
        )
    st.success("Successfully added to the database! Use the other tabs to explore more about your financial spending.")

    # # Read the database.
    # db = pd.read_csv('database.csv', index_col=[0])
    # # Using datatime module to get the date.
    # dt = datetime.now()
    #
    # # Append row to database.
    # db.loc[len(db)] = {'Date': str(dt.date()), 'Tags': tags, 'Amount': amount}
    #
    # # Save database
    # db.to_csv('database.csv')
    #
    # st.success("Successfully added to the database! Use the other tabs to explore more about your financial spending")


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


    st.info("Given below are the essential components of your sentence.")
    tags = ' '.join(tags)
    
    # Check if database exists using checkFile()
    checkFile()

    st.write(f"Tags: `{tags}`")
    st.write(f"Amount: `{amount}`")
    # Button to add to database.
    st.button("Add to database ?", on_click=lambda: addToDatabase(tags, amount))



