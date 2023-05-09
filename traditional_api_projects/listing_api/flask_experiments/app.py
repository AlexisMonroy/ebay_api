import requests
from flask import Flask, render_template
import datetime 

import os
import sys

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

url = 'https://api.ebay.com/ws/api.dll'

headers = { 
    'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',
'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
'X-EBAY-API-CALL-NAME': 'GetSessionIDRequest',
'X-EBAY-API-SITEID': '0',
'Content-Type' : 'text/xml'}

data = '''<?xml version="1.0" encoding="utf-8"?>
<GetSessionIDRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RuName>Alexis_Gonzalez-AlexisGo-pricep-ufgmqsmji</RuName>
</GetSessionIDRequest>'''

test_response = requests.post(url, headers=headers, data=data)
if test_response.status_code == 200:
    test_output = "Success"
else:
    test_output = "Failure"

print(test_response.status_code)
print(test_response.text)
print(test_output)

@app.route('/')
def index():
    return render_template('index.html', test_output=test_output)
