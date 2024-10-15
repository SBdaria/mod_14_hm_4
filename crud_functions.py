import sqlite3
from desc import *

connestion = sqlite3.connect('product.db')
cursor = connestion.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description NEXT,
    price INTEGER NOT NULL
    );
    ''')


initiate_db()

#for i in range(1, 5):
#    cursor.execute(f'INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
#                   (f'{name[i - 1]}', f'{noty[i - 1]}', f'{price[i - 1]}'))

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


connestion.commit()