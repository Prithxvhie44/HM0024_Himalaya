import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Vedant Hirekar\Downloads\expenserecords.csv")


df1 = df.groupby("date").sum()

col1, col2 = st.columns(2, gap = "large")

with col1:
    df1 = df1.reset_index()
    print(df1)
    st.line_chart(data = df1,  x = "date",y = "price")


with col2:
    item_prices = df.groupby('item')['price'].sum()

    total_price = item_prices.sum()

    item_percentages = (item_prices / total_price) * 100


    fig, ax = plt.subplots()
    ax.pie(item_percentages, labels=item_percentages.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')


    st.pyplot(fig)








