import streamlit as st
from audiorecorder import audiorecorder
from speechlib import getPhrase
from nlp import getEntry
import pandas as pd
from datetime import datetime

st.title("Add a expense")
st.header("Use the below recorder to add a expense")

audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:

    audio.export("audio.wav", format="wav")
    phrase = getPhrase()
    st.write("This got recorded: " + str(phrase))

    tags, amount = getEntry(phrase)

    tags = ';'.join(tags)

    st.write("This is the identified parameters!" + tags + ":" + amount)

    db = pd.read_csv('database.csv', names=["Date", "Tags", "Amount"])

    dt = datetime.now()

    row = { 'Date': str(dt.date()), 'Tags': tags, 'Amount': amount }

    db = pd.concat([db, pd.DataFrame([row])], ignore_index = True)


    db.to_csv('database.csv')






