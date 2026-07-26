import csv
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open("products.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    
products = soup.find_all("div", class_="products")

with open("products_data.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
    writer = csv.writer(csv_file)
    
    
    writer.writerow(["(تومان)قیمت","عنوان محصول"])
    
    for product in products:
        title = product.find("h2", class_="title").text
        price = product.find("h2", class_="title").text
        
        writer.writerow([title, price])
        
print("products_data.csv ساخته شد ")