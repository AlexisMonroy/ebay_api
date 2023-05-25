import os
import sqlite3
import requests
from flask import Flask, render_template, redirect, request
import datetime 
import xml.etree.ElementTree as ET
import sys

product_list = [(1,), (2,), (3,)]

data_folder = 'C:/Users/alexi/dev/ebay_api/ebay_api/traditional_api_projects/listing_api/flask_experiments/data'

conn = sqlite3.connect(os.path.join(data_folder, 'inventory.db'))

cursor = conn.cursor()

query = '''SELECT PRODUCT_ID FROM posted WHERE PRODUCT_ID = ?'''
select_item = '''SELECT * FROM books WHERE ID = ?'''

for i in range(0, len(product_list)):
    cursor.execute(query, product_list[i])
    posted_result = cursor.fetchone()
    print(posted_result)
    if posted_result is None:
        print("hello")
        cursor.execute(select_item, product_list[i])
        item_details = cursor.fetchone()
        print(item_details)
        
        item_id = item_details[0]
        title = item_details[1]
        author = item_details[2]
        units = item_details[3]
        illustrator = item_details[4]
        genre = item_details[5]
        publisher = item_details[6]
        pub_date = item_details[7]
        price = item_details[8]
        description = item_details[9]
        condition = item_details[10]
        condition_description = item_details[11]
        book_format = item_details[12]
        features = item_details[13]
        language = item_details[14]
        topic = item_details[15]
        book_series = item_details[16]
        book_type = item_details[17]
        narrative_type = item_details[18]
        edition = item_details[19]
        manufactured = item_details[20]
        inscibed = item_details[21]
        intended_audience = item_details[22]
        vintage = item_details[23]
        signed = item_details[24]


        

    else:
        print("goodbye")

conn.close()
