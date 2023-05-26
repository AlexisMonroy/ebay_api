import os
import sqlite3
import requests
from flask import Flask, render_template, redirect, request
import datetime 
import xml.etree.ElementTree as ET
import sys

api_call_headers = {'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
      'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
      'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',  
      'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
      'X-EBAY-API-CALL-NAME': 'VerifyAddItem',
      'X-EBAY-API-SITEID': '0',  
      'Content-Type' : 'text/xml'}

pic_url = "https://alexismonroy.github.io/images/"

product_list = [(1,), (2,), (3,)]

data_folder = 'C:/Users/alexi/dev/ebay_api/ebay_api/traditional_api_projects/listing_api/flask_experiments/data'

conn = sqlite3.connect(os.path.join(data_folder, 'inventory.db'))

cursor = conn.cursor()

query = '''SELECT PRODUCT_ID FROM posted WHERE PRODUCT_ID = ?'''
select_item = '''SELECT * FROM books WHERE ID = ?'''


#check if the product id is in the posted table; has it been listed?
for i in range(0, len(product_list)):
    cursor.execute(query, product_list[i])
    posted_result = cursor.fetchone()
    #print(posted_result)
    if posted_result is None:
        print("No match found")
        #if the product id is not in the posted table, then retrieve the item details from the books table
        cursor.execute(select_item, product_list[i])
        item_details = cursor.fetchone()
        #initialize the count variable
        count = 0
        print("\n ITEM DETAILS:\n", item_details)
        print("TYPE: ", type(item_details))
        #create a dictionary to store the item details
        item_dict = {'item_id': None, 'Title': None, 'Author': None, 'Units': None, 'Illustrator': None, 'Genre': None, 'Publisher': None, 'Publication Year': None, 'Price': None, 'Description': None, 'Condition': None, 'Condition Description': None, 'Book Format': None, 'Features': None, 'Language': None, 'Topic': None, 'Book Series': None, 'Book Type': None, 'Narrative Type': None, 'Edition': None, 'Manufactured': None, 'Inscibed': None, 'Intended Audience': None, 'Vintage': None, 'Signed': None}
        name_value_list = []
        #iterate through the dictionary and assign the item details to the dictionary keys
        for key in item_dict:
            item_dict[key] = item_details[count]
            #add name value pairs to a list
            if key in ['Illustrator', 'Genre', 'Publisher', 'Publication Year', 'Description', 'Condition Description', 'Book Format', 'Features', 'Language', 'Topic', 'Book Series', 'Book Type', 'Narrative Type', 'Edition', 'Manufactured', 'Inscibed', 'Intended Audience', 'Vintage', 'Signed']:
                name_value_list.append((key, item_dict[key]))
            #increment the count variable
            count += 1
        #write the item details to a text file
        with open('item_dict.txt', 'a') as f:
            print("\nItem Details:\n", item_details, file=f)
            print("\nItem Dict:\n", item_dict, file=f)
            print("\nName Value List:\n", name_value_list, file=f)
        print("\nName Value List:\n",name_value_list)
        name_value_call = ""
        for i in range(0, len(name_value_list)):
            k = 0
            j = 1
            if name_value_list[i][j] != "":
                #store the value in a string
                name_value_string = str(name_value_list[i][j])
                #count the number of words in the value
                num_words = len(name_value_string.split(','))
                if num_words > 1:
                    #split the value into a list of words
                    words = name_value_string.split(',')
                    for word in words:
                        #add each word to the name value call
                        #store the names and values in variables
                        name = name_value_list[i][k]
                        value = word.strip()
                        name_value = f'''<Name>{name}</Name><Value>{value}</Value>'''
                        name_value_call = name_value_call + name_value
                else:
                    #add the name value pair to the name value call
                    #store the names and values in variables
                    name = name_value_list[i][k]
                    value = name_value_list[i][j]
                    name_value = f'''<Name>{name}</Name><Value>{value}</Value>'''
                    name_value_call = name_value_call + name_value
        num_pics = int(input("How many pictures do you want to add?\n"))
        picture_call = ""
        for i in range(0, num_pics):

        
        print("\nCALL:\n", name_value_call)             

           
    else:
        print("goodbye")

conn.close()
