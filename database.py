import sqlite3
import pandas as pd

def getData():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("select * from users;", conn)
    return df

def addRow(date, time, username, description, category, amount):
    df = getData()
    df.loc[len(df.index)] = [date, time, username, description, category, amount]
    conn = sqlite3.connect("database.db")
    df.to_sql('users', conn, if_exists='replace')



