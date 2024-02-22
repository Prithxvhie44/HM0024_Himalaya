from database import getData, addRow
from datetime import datetime
from datetime import date
from datetime import timedelta
import pandas as pd

# dt = datetime.now()
# with open('categories.csv') as f:
#     print(f)

df = pd.read_csv('data/sample-data.csv')
for i in range(len(df)):
    # print(df.iloc[i])
    day, month, year = map(int, df.iloc[i]['Date'].split('-'))
    dt = datetime(year=year, month=month, day=day)
    td = timedelta(days=1980)
    addRow(
            date=(dt + td).strftime("%d-%m-%Y"),
            username='demo',
            description=df.iloc[i]['Description'],
            category=df.iloc[i]['Category'],
            amount=df.iloc[i]['Amount']
            )
# print(set(getData()['category']))
