import requests
from bs4 import BeautifulSoup
import sqlite3

# Create DB:
db = sqlite3.connect('products.sqlite')
open = db.cursor()

open.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, title TEXT, price REAL)')

# main algorithm:
def app(db, handl):
    url = get_url()
    url_soup = get_url_soup(url)
    data = get_products_data(url_soup)
    store_products_data(data, db, handl)


def get_url():
    url = input('print a url for products from "jlood" website: ')
    return url

def get_url_soup(url):
    # fetch the url:
    content = requests.get(url).content
    soup = BeautifulSoup(content, "lxml")

    return soup

def get_products_data(soup):
    data = []
    products_details = soup.find_all("div", {"class": "productitem--info"})

    for product_datails in products_details:
        product_price = product_datails.find('div', {'class': 'price__current'}).find('span', {'class': 'money'}).find('span').text.split()[0]
        product_price = handle_price_number(product_price)
        product_name = product_datails.find('h2', {'class': 'productitem--title'}).find('a').text.strip()
        data.append({"title": product_name, "price": product_price})
    return data

def handle_price_number(price):
    new_price = ""
    for num in list(price.strip()):
        if num == "," : continue
        new_price += num

    return float(new_price)

def store_products_data(data,dataBase,handl):
    for product in data:
        handl.execute('INSERT INTO products(title, price) VALUES (?, ?)', (product['title'], product['price']))
        dataBase.commit()

app(db, open)
