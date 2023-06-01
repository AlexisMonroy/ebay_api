import requests
import xml.etree.ElementTree as ET


def session_init():
    url = 'https://api.ebay.com/ws/api.dll'
    headers = { 
    'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',
'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
'X-EBAY-API-CALL-NAME': 'GetSessionID',
'X-EBAY-API-SITEID': '0',
'Content-Type' : 'text/xml'}

    data = '''<?xml version="1.0" encoding="utf-8"?>
    <GetSessionIDRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RuName>Alexis_Gonzalez-AlexisGo-pricep-ufgmqsmji</RuName>
    </GetSessionIDRequest>'''

    session_response = requests.post(url, headers=headers, data=data)
    if session_response.status_code == 200:
        session_output = "Success"
    else:
        session_output = "Failure"

    print(session_response.status_code)
    print(session_response.text)
    print(session_output)

    #create a tree from the response
    tree = ET.fromstring(session_response.text)
    #grab the session id from the tree
    session_id = tree[4].text
    print(tree[4].text)
    print("Done with Session Call")
    return session_id, session_response.text




