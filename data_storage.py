import sqlite3
import pandas as pd 

df = pd.read_csv("dataset.csv")

df.columns = df.columns.str.strip()

conn =  sqlite3.connect("ohlc_data.db")

df.to_sql('hello', conn, if_exists='replace')

