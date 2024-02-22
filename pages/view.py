import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sidebar import generateSideBar 
from database import getData

st.set_page_config(layout='wide')

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

st.title("Your logged expenses!")
st.divider()
database = getData()


df = database[database['username'] == st.session_state['username']]

# df['date'] = pd.to_datetime(df['date'], dayfirst=True).dt.date
# df = df.sort_values(by='date', ascending=[0])



df['amount']= df['amount'].astype(float)
avg = round(df['amount'].mean(),2)
ls = df.iloc[:30,4]
l_exp = df.iloc[0,4]

col1, col2, col3 = st.columns(3)
col1.metric("Average Expenditure", avg)
col2.metric("Sum of last 30 Expenditure", sum(ls))
col3.metric("Last Expenditure", l_exp)

st.divider()

df['date'] = pd.to_datetime(df['date'])
monthly_expenses = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
monthly_expenses = monthly_expenses.reset_index()
st.line_chart(data = monthly_expenses,  x = "date" ,y = 'amount')

st.divider()

item_prices = df.groupby('category')['amount'].sum()
total_price = item_prices.sum()
item_percentages = (item_prices / total_price) * 100
fig, ax = plt.subplots(figsize=(13, 5))
ax.pie(item_percentages, labels=item_percentages.index, autopct='%1.1f%%', startangle=90, radius=0.5, pctdistance=0.8)
ax.axis('equal')
st.pyplot(fig)

st.divider()

df['date'] = pd.to_datetime(df['date'], dayfirst=True).dt.date
df = df.drop(['username'], axis=1)
st.table(df)


