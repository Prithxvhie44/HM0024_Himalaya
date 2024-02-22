import sqlite3
import pandas as pd

def checkTable():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""create table if not exists users(
        date date, 
        username varchar(200),
        description varchar(300),
        category varchar(100),
        amount int
        );""")
    cur.close()
    conn.close()

def getData():
    conn = sqlite3.connect("database.db")
    checkTable()
    df = pd.read_sql_query("select * from users;", conn, index_col=None)
    conn.close()
    return df

def addRow(date, username, description, category, amount):
    df = getData()
    df.loc[len(df.index)] = [date, username, description, category, amount]
    conn = sqlite3.connect("database.db")
    df.to_sql('users', conn, if_exists='replace', index=False)
    conn.close()



