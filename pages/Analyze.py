import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('database.csv')


df1 = df.groupby("Date").sum()

df1 = df1.reset_index()
print(df1)
st.line_chart(data = df1,  x = "Date",y = "Amount")


item_prices = df.groupby('Tags')['Amount'].sum()

total_price = item_prices.sum()

item_percentages = (item_prices / total_price) * 100

fig, ax = plt.subplots()
ax.pie(item_percentages, labels=item_percentages.index, autopct='%1.1f%%', startangle=90)
fig.set_figwidth(20)
fig.set_figheight(20)
ax.axis('equal')


st.pyplot(fig)
