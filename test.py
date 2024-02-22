from database import getData, addRow
from datetime import datetime
import pandas as pd

# dt = datetime.now()
# with open('categories.csv') as f:
#     print(f)

df = pd.read_csv('sample-data.csv')
for i in range(len(df)):
    # print(df.iloc[i])
    addRow(
            date=df.iloc[i]['Date'],
            username='demo',
            description=df.iloc[i]['Description'],
            category=df.iloc[i]['Category'],
            amount=df.iloc[i]['Amount']
            )
# print(set(getData()['category']))
