import streamlit as st
from audiorecorder import audiorecorder
from speechlib import getPhrase
from nlp import getEntry
import pandas as pd
from datetime import datetime

st.title("Add a expense")

st.write("")
st.header("Use the below button to record a expense")
st.divider()

def addToDatabase(tags, amount):
    db = pd.read_csv('database.csv', index_col=[0])

    dt = datetime.now()

    db.loc[len(db)] = {'Date': str(dt.date()), 'Tags': tags, 'Amount': amount}

    db.to_csv('database.csv')

    st.success("Successfully added to the database! Use the other tabs to explore more about your financial spending")


audio = audiorecorder("Start Recording", "Stop Recording")

def checkFile():
    try:
        pd.read_csv('database.csv')
    except:
        db = pd.DataFrame(columns=['Date', 'Tags', 'Amount'])
        db.to_csv('database.csv')

if len(audio) > 0:

    audio.export("audio.wav", format="wav")

    with st.spinner():
        phrase = getPhrase()

    if phrase == None:
        st.error("Nothing got recorded!")
        st.stop()

    st.info("Given below is the text that got recorded")
    st.text(phrase)

    tags, amount = getEntry(phrase)


    st.info("Given below are the essential components of your sentence.")
    tags = ' '.join(tags)

    checkFile()

    st.write(f"Tags: `{tags}`")
    st.write(f"Amount: `{amount}`")

    st.button("Add to database ?", on_click=lambda: addToDatabase(tags, amount))



