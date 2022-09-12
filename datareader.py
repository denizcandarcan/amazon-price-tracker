import sqlite3
import pandas as pd

#DB connection
conn = sqlite3.connect('amazontracker.db')

#Reading data from table.
df = pd.read_sql_query('''SELECT * FROM prices''',conn)

print(df)