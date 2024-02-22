import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sidebar import generateSideBar
from database import getData
import pickle

st.set_page_config(page_title="Investments", layout='centered')

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False or st.session_state['authentication_status'] == None:
    st.toast("Not authenticated")
    st.switch_page("main.py")


generateSideBar()


data = getData()

st.title("`Analysis` :money_with_wings:")
st.divider()
st.write("A showcase of your spending.")
st.divider()

model = pickle.load(open('data/model.h5', 'rb'))

sip_amt = st.slider(label="Min Sip", min_value=500, max_value=2000, value=500)
lumpsum_amt = st.slider(label="Min Lumpsum", min_value=1000, max_value=20000)
expense_ratio = st.slider(label="Expense Ratio", min_value=0.1, max_value=5.0, value=0.89)

fund_size = 3812.0
fund_age = 10

sortino = 2.5
alpha = 2.37
sd = 9.96
beta = 0.77
sharpe = 1.17

risk_level = st.slider(label="Risk Level", min_value=1, max_value=6, value=3)
rating = st.slider(label="Rating", min_value=1, max_value=5, value=5)

X = [
        [
            sip_amt,
            lumpsum_amt,
            expense_ratio,
            fund_size,
            fund_age,
            sortino,
            alpha, 
            sd,
            beta,
            sharpe,
            risk_level,
            rating
            ]
        ]

predicted = model.predict(X)

# st.write(predicted)

# df1 = df.groupby("Date").sum()
#
# df1 = df1.reset_index()
# st.line_chart(data = df1,  x = "Date",y = "Amount")
#
# st.divider()
# st.header("Expenditure breakup")
# st.write("Here's a breakup of your expenditure based on the items.")
#
# item_prices = df.groupby('Tags')['Amount'].sum()
#
# total_price = item_prices.sum()
#
# item_percentages = (item_prices / total_price) * 100
#
# fig, ax = plt.subplots(figsize=(5, 5))
# ax.pie(item_percentages, labels=item_percentages.index, autopct='%1.1f%%', startangle=90)
# ax.axis('equal')
#
#
# st.pyplot(fig)
#
# st.divider()
# st.header("Investments")
# st.write("Here's how your can achieve your financial goals.")
#
#
#
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
# # Group by 'Date' (month) and sum the prices
# df_grouped = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
# # Calculate the average total expenditure per month
# average_expenditure = df_grouped.mean()
#
#
#
#
def calculate_total_amount(principal, monthly_installment, years, interest_rate):
    total_amount = principal
    monthly_interest_rate = (interest_rate / 100) / 12
    for year in range(years):
        for month in range(12):
            total_amount *= (1 + monthly_interest_rate)
            total_amount += monthly_installment
    return total_amount
#
# ps = st.slider('Principal amount', 1000, 50000, 2000)
# ys = st.slider("Years", 10, 30, 25)
# irs = st.slider("Interest(Monthly)", 1, 25, 4)
# # Define parameters
# principal = 1000
rec_cutting = sip_amt
principal = sip_amt
monthly_installment = rec_cutting
years = st.slider(label="Total years", min_value=5, max_value=30, value=10)
interest_rate = predicted[0][1]

# Calculate total amount and invested money for each year
total_amounts = []
invested_money = []
total_investment = 0
for year in range(1, years+1):
    total_investment += 12 * monthly_installment
    invested_money.append(total_investment)
    total_amounts.append(calculate_total_amount(principal, monthly_installment, year, interest_rate))

# Plot the graph
fig, ax = plt.subplots()
ax.plot(range(1, years+1), total_amounts, marker='o', label='Total Amount')
ax.plot(range(1, years+1), invested_money, marker='o', color='orange', linestyle='--', label='Invested Money')

ax.set_xlabel('Years')
ax.set_ylabel('Amount')
ax.set_title('Total Amount vs. Years (with 4% interest compounded monthly)')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)


