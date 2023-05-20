    fetch_token_headers = { 
        'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
    'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
    'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',
    'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
    'X-EBAY-API-CALL-NAME': 'FetchToken',
    'X-EBAY-API-SITEID': '0',
    'Content-Type' : 'text/xml'}     

    fetch_token_data = f'''<?xml version="1.0" encoding="utf-8"?>
    <FetchTokenRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <SessionID>{session_id}</SessionID>
    </FetchTokenRequest>'''

    fetch_token_response = requests.post(url, headers=fetch_token_headers, data=fetch_token_data)
    print(fetch_token_response.status_code)
    print(fetch_token_response.text)

    fetch_token_tree = ET.fromstring(fetch_token_response.text)
    print(str(fetch_token_tree))

    dict_data = {}
    for child in tree:
        dict_data[child.tag] = child.text
    print(dict_data)


    with open('resp_output/response.txt', 'w') as f:
        f.write(test_response.text)
        f.write("\n\n\n")
        f.write(str(tree))
        f.write("\n\n\n")
        f.write(str(dict_data))
        f.write("\n\n\n")
        f.write(fetch_token_response.text)
        f.write("\n\n\n")
        f.write(str(fetch_token_tree))