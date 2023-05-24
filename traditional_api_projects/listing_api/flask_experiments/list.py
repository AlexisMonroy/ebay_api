import csv
import sqlite3
import os

data_folder = 'C:/Users/alexi/dev/ebay_api/ebay_api/traditional_api_projects/listing_api/flask_experiments/data'

conn = sqlite3.connect(os.path.join(data_folder, 'inventory.db'))

# Create a new table in the database

conn.execute('CREATE TABLE IF NOT EXISTS PENDING (PENDING_ID INTEGER PRIMARY KEY, PRODUCT_ID INTEGER NULL, MARKET_ID INTEGER NULL, DATE_TIME TEXT NULL, FOREIGN KEY (MARKET_ID) REFERENCES markets (MARKET_ID), FOREIGN KEY (PRODUCT_ID) REFERENCES books (PRODUCT_ID))')
conn.execute('CREATE TABLE IF NOT EXISTS POSTED (PENDING_ID INTEGER PRIMARY KEY, PRODUCT_ID INTEGER NULL, MARKET_ID INTEGER NULL, DATE_TIME TEXT NULL, FOREIGN KEY (MARKET_ID) REFERENCES markets (MARKET_ID), FOREIGN KEY (PRODUCT_ID) REFERENCES books (PRODUCT_ID))')


#cursor = conn.execute('SELECT ID from books where Title = ?', (book,))
cursor = conn.execute('SELECT ID from books')
product_ids = cursor.fetchall()

conn.commit()
conn.close()

print(product_ids)
print(product_ids[10])
