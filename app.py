from requests_html import HTMLSession
import csv
import datetime
import sqlite3 

#DB Connection
conn = sqlite3.connect('amazontracker.db')
c= conn.cursor()

#Session start
s = HTMLSession()

#Empty list for asins
asins = []

#Adding asins to list from file.
with open('asins.csv', 'r') as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])

#Data Scrapping
for asin in asins:
    print(f'Trying to reach data for {asin} id product.')
    r = s.get(f'https://www.amazon.co.uk/dp/{asin}')
    r.html.render(sleep=2)

    # Important! Prices and title CSS Selectors can be change by Amazon in a time. If this script is crash please check css selectors on website and change on script.
    try:
        price = r.html.find('.a-offscreen')[1].text.replace('£', '').replace(
            ',', '').strip() 
    except:
        price = r.html.find('.a-offscreen')[0].text.replace('£', '').replace(
            ',', '').strip()

    title = r.html.find('#productTitle')[0].text.strip()
    asin=asin
    date = datetime.datetime.today()
    c.execute(''' INSERT INTO prices VALUES(?,?,?,?)''',(date,asin,price,title))
    print(f'{asin} id product data scrapped. Price:{price}')

conn.commit()
print('New entries committed to db succesfully.')