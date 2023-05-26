x = 3
y = '<pic_call>'
z = 'alexis'
q = '.jpg</pic_call>'
s = ''

for i in range(x):
    pic = y + z + str(i) + q
    s = s + pic
    print(pic)
print(s)    

verify_data = f'''<?xml version="1.0" encoding="utf-8"?>
  <VerifyAddItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
      <eBayAuthToken>{token[0]}</eBayAuthToken>
    </RequesterCredentials>
    <ErrorLanguage>en_US</ErrorLanguage>
    <WarningLevel>High</WarningLevel>
    <Item>
      <Title>{item_dict['title']}</Title>
      <Description>
        {item_dict['description']}
      </Description>
      <PrimaryCategory>
        <CategoryID>261186</CategoryID>
      </PrimaryCategory>
      <StartPrice>{item_dict['price']}</StartPrice>
      <CategoryMappingAllowed>true</CategoryMappingAllowed>
      <ConditionID>5000</ConditionID>
      <Country>US</Country>
      <Currency>USD</Currency>
      <DispatchTimeMax>3</DispatchTimeMax>
      <ListingDuration>GTC</ListingDuration>
      <ListingType>FixedPriceItem</ListingType>
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
  </VerifyAddItemRequest>'''
    