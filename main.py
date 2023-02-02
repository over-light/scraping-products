import requests
from bs4 import BeautifulSoup
import sqlite3
from itertools import zip_longest

# Create DB:
db = sqlite3.connect('products.sqlite')
open = db.cursor()

open.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, title TEXT, price INTEGER)')