import sqlite3
import pandas as pd

def getData():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("select * from users;", conn)
    return df



