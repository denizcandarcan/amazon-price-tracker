import sqlite3

#Creating local db and table for project.
conn = sqlite3.connect('amazontracker.db')
c= conn.cursor()
c.execute(''' CREATE TABLE prices(date DATE,asin TEXT,price FLOAT,title TEXT)''')

