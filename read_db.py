import sqlite3
import sys


sys.stdout.reconfigure(encoding='utf-8')


conn = sqlite3.connect('products.db')

conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""SELECT * 
               FROM products""")
rows = cursor.fetchall()
for row in rows:
    print(f"شناسه: {row['id']} | عنوان: {row['title']} | قیمت: {row['price']}") 

conn.commit()
conn.close()
