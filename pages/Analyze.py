import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analysis")
st.header("Here's a analysis of your daily spending")
st.divider()

df = pd.read_csv('database.csv')

df1 = df.groupby("Date").sum()

df1 = df1.reset_index()
st.line_chart(data = df1,  x = "Date",y = "Amount")

st.divider()

item_prices = df.groupby('Tags')['Amount'].sum()

total_price = item_prices.sum()

item_percentages = (item_prices / total_price) * 100

fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(item_percentages, labels=item_percentages.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')


st.pyplot(fig)
