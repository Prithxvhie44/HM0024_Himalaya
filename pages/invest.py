import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sidebar import generateSideBar

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()

st.title("Analysis")
st.header("Here's a analysis of your daily spending")
st.divider()

df = pd.read_csv('database.csv')

df1 = df.groupby("Date").sum()

df1 = df1.reset_index()
st.line_chart(data = df1,  x = "Date",y = "Amount")

st.divider()
st.header("Expenditure breakup")
st.write("Here's a breakup of your expenditure based on the items.")

item_prices = df.groupby('Tags')['Amount'].sum()

total_price = item_prices.sum()

item_percentages = (item_prices / total_price) * 100

fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(item_percentages, labels=item_percentages.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')


st.pyplot(fig)

st.divider()
st.header("Investments")
st.write("Here's how your can achieve your financial goals.")



df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
# Group by 'Date' (month) and sum the prices
df_grouped = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
# Calculate the average total expenditure per month
average_expenditure = df_grouped.mean()




def calculate_total_amount(principal, monthly_installment, years, interest_rate):
    total_amount = principal
    monthly_interest_rate = (interest_rate / 100) / 12
    for year in range(years):
        for month in range(12):
            total_amount *= (1 + monthly_interest_rate)
            total_amount += monthly_installment
    return total_amount

ps = st.slider('Principal amount', 1000, 50000, 2000)
ys = st.slider("Years", 10, 30, 25)
irs = st.slider("Interest(Monthly)", 1, 25, 4)
# Define parameters
# principal = 1000
rec_cutting = average_expenditure * 0.1
print(rec_cutting)
principal = ps
monthly_installment = rec_cutting
years = ys
interest_rate = irs

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
