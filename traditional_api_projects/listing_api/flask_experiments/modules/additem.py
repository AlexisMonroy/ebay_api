import os
import sqlite3
import requests
from flask import Flask, render_template, redirect, request
import datetime 
import xml.etree.ElementTree as ET
import sys

def add_item(product_list, token):
    api_call_headers = {'X-EBAY-API-COMPATIBILITY-LEVEL': '719',
        'X-EBAY-API-DEV-NAME': 'dae89547-48b8-4c4b-9e57-e8e9a84527dd',
        'X-EBAY-API-APP-NAME': 'AlexisGo-pricepre-PRD-3ca7161d2-d3ef5057',  
        'X-EBAY-API-CERT-NAME': 'PRD-ca7161d2a58b-663b-4c87-9cec-8cbd',
        'X-EBAY-API-CALL-NAME': 'VerifyAddItem',
        'X-EBAY-API-SITEID': '0',  
        'Content-Type' : 'text/xml'}

    pic_site = "https://alexismonroy.github.io/images/"

    data_folder = 'C:/Users/alexi/dev/ebay_api/ebay_api/traditional_api_projects/listing_api/flask_experiments/data'

    conn = sqlite3.connect(os.path.join(data_folder, 'inventory.db'))

    cursor = conn.cursor()

    query = '''SELECT PRODUCT_ID FROM posted WHERE PRODUCT_ID = ?'''
    select_item = '''SELECT * FROM books WHERE ID = ?'''


    #check if the product id is in the posted table; has it been listed?
    call_list = []
    pic_call_list = []
    add_item_list = []
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
            item_dict = {'item_id': None, 'Title': None, 'Author': None, 'Units': None, 'Illustrator': None, 'Genre': None, 'Publisher': None, 'Publication Year': None, 'Price': None, 'Description': None, 'Condition': None, 'Condition Description': None, 'Book Format': None, 'Features': None, 'Language': None, 'Topic': None, 'Book Series': None, 'Book Type': None, 'Narrative Type': None, 'Edition': None, 'Manufactured': None, 'Inscibed': None, 'Intended Audience': None, 'Vintage': None, 'Signed': None, 'Pictures': None}
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
                print("\nTime:\n", datetime.datetime.now())
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
            if name_value_call != "":
                call_list.append(name_value_call)
            with open('call_output.txt', 'a') as f:
                print("\nTime:\n", datetime.datetime.now(), file=f)
                print("\nCall List:\n", call_list, file=f)
                #print the time the call was made
                

            #get the number of pictures
            num_pics = item_dict['Pictures']
            pic_details = ""
            #append the picture name
            for i in range(0, num_pics):
                picture_name = item_dict['Title'] + str(i)
                print("\nPicture Name:\n", picture_name)
                pic_location = pic_site + picture_name + ".jpg"
                pic_details = pic_details + f'''<PictureURL>{pic_location}</PictureURL>'''
                print("\nPicture Call:\n", pic_details)
            #pic_call = f'''<PictureDetails>{pic_details}</PictureDetails>'''
            
            if pic_details != "":
                pic_call_list.append(pic_details)
            with open('call_output.txt', 'a') as f:
                print("\nTime:\n", datetime.datetime.now(), file=f)
                print("\nPicture Call List:\n", pic_call_list, file=f)
                

            verify_data = f'''<?xml version="1.0" encoding="utf-8"?>
  <VerifyAddItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
      <eBayAuthToken>{token}</eBayAuthToken>
    </RequesterCredentials>
    <ErrorLanguage>en_US</ErrorLanguage>
    <WarningLevel>High</WarningLevel>
    <Item>
      <Title>{item_dict['Title']}</Title>
      <Description>
        {item_dict['Description']}
      </Description>
      <PrimaryCategory>
        <CategoryID>261186</CategoryID>
      </PrimaryCategory>
      <StartPrice>{item_dict['Price']}</StartPrice>
      <CategoryMappingAllowed>true</CategoryMappingAllowed>
      <ConditionID>5000</ConditionID>
      <Country>US</Country>
      <Currency>USD</Currency>
      <DispatchTimeMax>3</DispatchTimeMax>
      <ListingDuration>GTC</ListingDuration>
      <ListingType>FixedPriceItem</ListingType>
      <PictureDetails>
        {pic_details}
      </PictureDetails>
      <PostalCode>95125</PostalCode>
      <Quantity>1</Quantity>
      <ItemSpecifics>     
      {name_value_call}
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
  </VerifyAddItemRequest>'''

            add_item_list.append(verify_data)
            print("\nCALL:\n", verify_data)             
            print(token)
            
            with open('call_output.txt', 'a') as f:
                print("\nTime:\n", datetime.datetime.now(), file=f)
                print("\nVerify Data:\n", verify_data, file=f)
        else:
            print("Item has already been posted")
    #print the end time to call_output.txt
    with open('call_output.txt', 'a') as f:
        print("\nEnd Time:\n", datetime.datetime.now(), file=f)
    return add_item_list
    conn.close()
    print("\nConnection Closed\n")
