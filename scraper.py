import sqlite3
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        price TEXT
    )
''')

with open("products.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    
products = soup.find_all("div", class_="products")

for product in products:
    title_elem = product.find("h2", class_="title")
    price_elem = product.find("h2", class_="price")
    
    title = title_elem.text.strip() if title_elem else "بدون عنوان"
    price = price_elem.text.strip() if price_elem else "بدون قیمت"
    
    cursor.execute("INSERT INTO products (title, price) VALUES (?, ?)", (title, price))

# ۵. ثبت تغییرات و بستن اتصال
conn.commit()
conn.close()

print("داده‌ها با موفقیت در products.db ذخیره شدند!")
