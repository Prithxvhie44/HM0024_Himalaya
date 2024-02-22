from database import getData, addRow
from datetime import datetime

dt = datetime.now()

addRow(dt.date(),'demo', 'some other demo description', 'expense', 300 )
# print(getData())
