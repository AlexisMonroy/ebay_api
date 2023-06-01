import requests
from flask import Flask, render_template, redirect, request
import datetime 
import xml.etree.ElementTree as ET
import os
import sys
from modules.load_csv import read_csv 
from modules.pending import pending_check
from modules.additem import add_item
from modules.xml_reader import extract_shipping_details
from modules.session_init import session_init
from modules.fetch_token import fetch_token

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

#load the csv file
file_path = os.path.join(os.path.dirname(__file__), 'data', 'books.csv')
print(file_path)

rows = read_csv(file_path)
print("Done with CSV Call")

#query the database for pending and posted items
product_ids = pending_check()
print(product_ids)

with open('product_ids.txt', 'a') as f:
    print(product_ids, file=f)
print("Done with Pending Check")


url = 'https://api.ebay.com/ws/api.dll'
call_header = { 
    'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
    'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
    'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',
    'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
    'X-EBAY-API-CALL-NAME': '{call_name}',
    'X-EBAY-API-SITEID': '0',
    'Content-Type' : 'text/xml'}

pic_url = 'https://alexismonroy.github.io/images/Monte_Cristo.jpg'
token = []
#grab the session id

session_id, session_output = session_init()

@app.route('/')
def index():
    return render_template('index.html', test_output=session_output)

@app.route('/signin')
def signin():
    signin_url = f'https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&runame=Alexis_Gonzalez-AlexisGo-pricep-ufgmqsmji&SessID={session_id}'
    return redirect(signin_url)

@app.route('/api_calls', methods=['GET', 'POST'])
def api_calls():
    if request.method == 'POST':
        button = request.form['button']
        #fetch the token
        if button == 'FetchToken':
            fetch_token_call, fetch_token_output = fetch_token(call_header, session_id, url)
            token.append(fetch_token_call)
            return render_template('index.html', test_output=fetch_token_output)  
    
        if button == 'VerifyItem':
          
          verify_data = add_item(product_ids, token[0], call_header, url)
          
          return render_template('api_calls.html', verify_responses=verify_data)
        
        elif button == 'GetDetails':
            api_call_headers = {'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
      'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
      'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',  
      'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
      'X-EBAY-API-CALL-NAME': 'GetebayDetails',
      'X-EBAY-API-SITEID': '0',
      'Content-Type' : 'text/xml'}
            get_details_data = f'''<?xml version="1.0" encoding="utf-8"?> 
<GeteBayDetailsRequest xmlns="urn:ebay:apis:eBLBaseComponents"> 
  <RequesterCredentials> 
    <eBayAuthToken>{token[0]}</eBayAuthToken> 
  </RequesterCredentials>  
  <DetailName>ShippingServiceDetails</DetailName> 
</GeteBayDetailsRequest>'''
            get_details_response = requests.post(url, headers=api_call_headers, data=get_details_data)
            print(get_details_response.status_code)
            print(get_details_response.text)
            print("Done with API Call")
            extract_shipping_details(get_details_response.text)
            with open('resp_output/get_details.txt', 'a') as f:
                f.write("Start:\n:" + str(datetime.datetime.now()))
                f.write(str(get_details_response))
                f.write("\n\n\n")
                f.write(str(get_details_response.text))
                print("\n\n\n")
                print("End:\n:" + str(datetime.datetime.now()))
            return render_template('api_calls.html', get_details_response=get_details_response)
            
        #GetCategoryFeatures call
        elif button == 'GetCategoryFeatures':
            api_call_headers = {'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
      'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
      'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',  
      'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
      'X-EBAY-API-CALL-NAME': 'GetCategoryFeatures',
      'X-EBAY-API-SITEID': '0',
      'Content-Type' : 'text/xml'}
            
            category_data = f'''<?xml version="1.0" encoding="utf-8"?>
  <GetCategoryFeaturesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
      <eBayAuthToken>{token[0]}</eBayAuthToken>
    </RequesterCredentials>
    <CategoryID>261186</CategoryID>
    <FeatureID>ConditionValues</FeatureID>
    <DetailLevel>ReturnAll</DetailLevel>
  </GetCategoryFeaturesRequest>'''
            
            category_response = requests.post(url, headers=api_call_headers, data=category_data)
            print(category_response.status_code)
            print(category_response.text)
            print("Done with API Call")
            with open('resp_output/api_call_response.txt', 'w') as f:
                f.write(category_response.text)
                f.write("\n\n\n")
                f.write(str(category_response))
            return render_template('api_calls.html', get_time_response=category_response)
        
        elif button == 'AddItem':
            api_call_headers = {'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
      'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
      'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',  
      'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
      'X-EBAY-API-CALL-NAME': 'AddItem',
      'X-EBAY-API-SITEID': '0',
      'Content-Type' : 'text/xml'}
            
            add_item_data = f'''<?xml version="1.0" encoding="utf-8"?>
  <AddItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
      <eBayAuthToken>{token[0]}</eBayAuthToken>
    </RequesterCredentials>
    <ErrorLanguage>en_US</ErrorLanguage>
    <WarningLevel>High</WarningLevel>
    <Item>
      <Title>Harry Potter and the Philosopher's Stone</Title>
      <Description>
        This is the first book in the Harry Potter series. In excellent condition!
      </Description>
      <PrimaryCategory>
        <CategoryID>261186</CategoryID>
      </PrimaryCategory>
      <StartPrice>1.0</StartPrice>
      <CategoryMappingAllowed>true</CategoryMappingAllowed>
      <ConditionID>4000</ConditionID>
      <Country>US</Country>
      <Currency>USD</Currency>
      <DispatchTimeMax>3</DispatchTimeMax>
      <ListingDuration>Days_7</ListingDuration>
      <ListingType>Chinese</ListingType>
      <PictureDetails>
        <PictureURL>https://alexismonroy.github.io/images/montecristo4.jpg</PictureURL>
      </PictureDetails>
      <PostalCode>95125</PostalCode>
      <Quantity>1</Quantity>
      <ItemSpecifics>     
      <NameValueList> 
          <Name>Title</Name>
          <Value>Harry Potter and the Philosophers Stone</Value> 
      </NameValueList> 
      <NameValueList> 
          <Name>Publisher</Name> 
          <Value>Smashwords</Value> 
      </NameValueList> 
      <NameValueList> 
          <Name>Author</Name> 
          <Value>JK Rowling</Value> 
      </NameValueList> 
      <NameValueList> 
          <Name>Language</Name> 
          <Value>English</Value> 
      </NameValueList>
      </ItemSpecifics>
      <ReturnPolicy>
        <ReturnsAcceptedOption>ReturnsAccepted</ReturnsAcceptedOption>
        <RefundOption>MoneyBack</RefundOption>
        <ReturnsWithinOption>Days_30</ReturnsWithinOption>
        <ShippingCostPaidByOption>Buyer</ShippingCostPaidByOption>
      </ReturnPolicy>
      <ShippingDetails>
        <ShippingType>Flat</ShippingType>
        <ShippingServiceOptions>
          <ShippingServicePriority>1</ShippingServicePriority>
          <ShippingService>USPSMedia</ShippingService>
          <ShippingServiceCost>2.50</ShippingServiceCost>
        </ShippingServiceOptions>
      </ShippingDetails>
      <Site>US</Site>
    </Item>
  </AddItemRequest>'''
            
            add_item_response = requests.post(url, headers=api_call_headers, data=add_item_data)
            print(add_item_response.status_code)
            print(add_item_response.text)
            print("Done with API Call")
            with open('resp_output/api_call_response.txt', 'w') as f:
                f.write(add_item_response.text)
                f.write("\n\n\n")
                f.write(str(add_item_response))
            return render_template('api_calls.html', get_time_response=add_item_response)

        elif button == 'PostPicture':
                    api_call_headers = {'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
    'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
    'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',  
    'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
    'X-EBAY-API-CALL-NAME': 'UploadSiteHostedPictures',
    'X-EBAY-API-SITEID': '0',
    'Content-Type' : 'text/xml'}
                    post_picture_data = f'''<?xml version="1.0" encoding="utf-8"?>
<UploadSiteHostedPicturesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
    <eBayAuthToken>{token[0]}</eBayAuthToken>
  </RequesterCredentials>
  <WarningLevel>High</WarningLevel>
  <ExternalPictureURL>{pic_url}</ExternalPictureURL>
  <PictureName>Developer Page Banner</PictureName>
</UploadSiteHostedPicturesRequest>'''

                    post_picture_response = requests.post(url, headers=api_call_headers, data=post_picture_data)
                    print(post_picture_response.status_code)
                    print(post_picture_response.text)
                    print("Done with Picture API Call")
                    with open('resp_output/post_picture_response.txt', 'w') as f:
                        f.write(post_picture_response.text)
                        f.write("\n\n\n")
                        f.write(str(post_picture_response))
                    return render_template('api_calls.html', post_picture_response=post_picture_response)
    
    else:
        return render_template('api_calls.html')
    