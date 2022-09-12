# Amazon Price Tracker
A simple web scraping project in Python 3.

# Features
    Scraping price data of an specific products(choosed by user) on Amazon UK and store on local db.
    Visualizes db data to user.

# Requirements
* Python 3.9.x or above installed.
* Good speed internet connection.

# How to get started

1. First, I highly recommend creating virtual env for this project via `python -m venv env`
2. After we create our virtual env, we need to install required libraries via `pip install -r requirements.txt`
3. Run `dbsetup.py` to create local db for project.
4. I already added 10 sample asins for test, you can remove my sample products or add your products via `asins.csv`.
5. Thats it, run `app.py` then script will be start scraping for you :)
6. To visualizes scrapped data  run `datareader.py`

# How can i find my product asin?

You can simply find asin of your product via link of item or searching with `ctrl+f for asin` on product page.

# Example:
    https://www.amazon.co.uk/dp/B018PUYPCA/.
    Your product asin is : B018PUYPCA
![Picture](https://i.imgur.com/ya1geoz.png)
