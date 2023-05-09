import requests
from flask import Flask, render_template
import datetime 

import os
import sys
from optparse import OptionParser

sys.path.insert(0, '%s/../' % os.path.dirname(__file__))

import ebaysdk
from ebaysdk.utils import getNodeText
from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading

def check_list(d, result):
    for item in d:
        if isinstance(item, dict):
            print_values(item, result)
        else:
            # store the item and the dictionary key:
            result.append((key, item))

def print_values(d, result):
    for key, value in d.items():
        if isinstance(value, dict):
            print_values(value, result)
        elif isinstance(value, list):
            check_list(value, result)
        else:
            # store the key and value pair:
            result.append((key, value))

result = []
api = Trading(config_file='myebay.yaml')
response = api.execute('GetUser', {})
print(response.dict())
print("\n\n\n")
print(response.reply)
print("\n\n\n")


#write response.dict() and response.reply to a notepad file:
with open('response_output/response.txt', 'w') as f:
    f.write(str(response.dict()))
    f.write("\n\n\n")
    f.write(str(response.reply))
    
get_categories = {'CategorySiteID': 0, 'DetailLevel': 'ReturnAll', 'LevelLimit': 1, 'ViewAllNodes': True}

cat_reponse = api.execute('GetCategories', get_categories)
cat_response_dict = cat_reponse.dict()
print_values(cat_response_dict, result)

print(cat_reponse.dict())
for key, value in result:
    print(key, value)


app = Flask(__name__)

@app.route('/')
def index():
    user_data = response.dict()
    return render_template('index.html', user_data=user_data)


@app.route('/other_page')
def other_page():
    cat_data = cat_reponse.dict()
    return render_template('categories_overview.html', result=result)

url = 'https://api.ebay.com/ws/api.dll'

headers = { 
    'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',
'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
'X-EBAY-API-CALL-NAME': 'GetCategories',
'X-EBAY-API-SITEID': '0',
'Content-Type' : 'text/xml'}

data = '''<?xml version="1.0" encoding="utf-8"?>
<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <CategorySiteID>0</CategorySiteID>
  <DetailLevel>ReturnAll</DetailLevel>
  <LevelLimit>7</LevelLimit>
  <ViewAllNodes>true</ViewAllNodes>
</GetCategoriesRequest>'''

test_response = requests.post(url, headers=headers, data=data)
if test_response.status_code == 200:
    test_output = "Success"
else:
    test_output = "Failure"

print(test_response.status_code)
print(test_response.text)
print(test_output)

@app.route('/third_page')
def third_page():
    return render_template('third_page.html', test_output=test_output)



if __name__ == '__main__':
    app.run()