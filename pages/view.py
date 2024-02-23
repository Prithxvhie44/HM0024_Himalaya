import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from database import getData
from streamlit_extras.metric_cards import style_metric_cards
from sidebar import generateSideBar 

st.set_page_config(layout='wide')

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

st.title("`Expense At a Glance` :moneybag: ")
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
col1.metric("Average Expenditure", "Rs. "+ str(avg))
col2.metric("Sum of last 30 Expenditure","Rs. "+ str( sum(ls) ), delta= "Rs. "+str(l_exp) )
col3.metric("Last Expenditure", "Rs. "+ str(l_exp))

style_metric_cards()

st.divider()

df['date'] = pd.to_datetime(df['date'])
monthly_expenses = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
monthly_expenses = monthly_expenses.reset_index()
st.markdown("Expense by Month")

st.line_chart(data = monthly_expenses,  x = "date" ,y = 'amount')

st.divider()

item_prices = df.groupby('category')['amount'].sum()
total_price = item_prices.sum()
item_percentages = (item_prices / total_price) * 100
fig, ax = plt.subplots(figsize=(13, 5))
ax.pie(item_percentages,  labels=item_percentages.index, autopct='%1.1f%%', startangle=90, radius=0.5, pctdistance=0.8, explode=[0.025]*11)
ax.axis('equal')
st.markdown("Pie chart ")
st.pyplot(fig)

st.divider()

df['date'] = pd.to_datetime(df['date'], dayfirst=True).dt.date
df = df.drop(['username'], axis=1)


col1, col2 = st.columns(2)


with col1:
    d = st.date_input("Filter by Date", value = None)

with col2:
    
    cat = df.iloc[:,2].unique()
    cat = np.append("All", cat)
    cat_select = st.selectbox("Filter by category", cat)


df1= pd.DataFrame()

if cat_select == "All" and d == None:
    st.table(df)

if d == None:
    df1 = df[df['category'] == cat_select]
    st.markdown("Expense by : " + cat_select)
    st.line_chart(data =df1,  x = "date" ,y = 'amount')
    st.table(df1)

if cat_select == 'All':
    df3 = df[df['date'] == d]
    st.table(df3)

if d != None and cat_select != 'All':
    df1 = df[df['category'] == cat_select]
    df2 = df1[df1['date'] == d]
    st.markdown("Expense by : " + cat_select)
    st.line_chart(data =df1,  x = "date" ,y = 'amount')
    st.table(df2)
