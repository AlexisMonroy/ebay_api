import requests
import xml.etree.ElementTree as ET




def fetch_token(call_header, session_id, url):
    try:
        if session_id is not None:
            fetch_token_call = 'FetchToken' 
            use_fetch_token = True
            if use_fetch_token:
                call_name = fetch_token_call
                call_header['X-EBAY-API-CALL-NAME'] = call_name

                header = call_header    

                fetch_token_data = f'''<?xml version="1.0" encoding="utf-8"?>
                <FetchTokenRequest xmlns="urn:ebay:apis:eBLBaseComponents">
                <SessionID>{session_id}</SessionID>
                </FetchTokenRequest>'''

                fetch_token_response = requests.post(url, headers=header, data=fetch_token_data)
                print(fetch_token_response.status_code)
                print(fetch_token_response.text)

                fetch_token_tree = ET.fromstring(fetch_token_response.text)
                fetch_token = fetch_token_tree[4].text
                #token.append(fetch_token)
                print("Token: " + fetch_token)
                return fetch_token, fetch_token_response.text
    except:
        print("Error with Fetch Token Call")