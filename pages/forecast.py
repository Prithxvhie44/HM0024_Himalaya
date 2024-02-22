import streamlit as st
from sidebar import generateSideBar 

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == False or st.session_state['authentication_status'] == None:
    st.toast("Not authenticated")
    st.switch_page("main.py")

generateSideBar()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import streamlit as st


df = pd.read_csv("C:/Users/Vedant Hirekar/Downloads/archive (3)/Expensedata.csv")
# df = df.iloc[300:]
# print(df)

# Preprocess the data
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df[["Amount"]]
# print(df)


df_monthly = df.resample('M').sum()  


model = ARIMA(df_monthly['Amount'], order=(5,1,0))  
arima_model = model.fit()


forecast_steps = 6  # Forecast one additional month
forecast = arima_model.forecast(steps=forecast_steps)


plt.figure(figsize=(10, 6))
plt.plot(df_monthly.index, df_monthly['Amount'], label='Original Data', color='blue')
plt.plot(pd.date_range(start=df_monthly.index[-1], periods=forecast_steps+1, freq='M'), np.append(df_monthly['Amount'].values[-1], forecast), color='red', label='Forecast')
plt.title('Monthly ARIMA Forecast')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend()
# plt.show()

st.set_option('deprecation.showPyplotGlobalUse', False)

# fig, ax = plt.subplots()
st.pyplot()
