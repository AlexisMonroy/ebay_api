import os
import sys
import datetime
from optparse import OptionParser

sys.path.insert(0, '%s/../' % os.path.dirname(__file__))

import ebaysdk
from ebaysdk.utils import getNodeText
from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading


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

try:
    myitem = {
        "Item": {
            "Title": "Harry Potter and the Philosopher's Stone",
            "Description": "This is the first book in the Harry Potter series. In excellent condition!",
            "PrimaryCategory": {"CategoryID": "377"},
            "StartPrice": "10.0",
            "BuyItNowPrice": "15.0",
            "CategoryMappingAllowed": "true",
            "Country": "US",
            "ConditionID": "3000",
            "Currency": "USD",
            "DispatchTimeMax": "3",
            "ListingDuration": "Days_7",
            "ListingType": "Chinese",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "tkeefdddder@gmail.com",
            "PictureDetails": {"PictureURL": "http://i1.sandbox.ebayimg.com/03/i/00/30/07/20_1.JPG?set_id=8800005007"},
            "PostalCode": "95125",
            "Quantity": "1",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsAccepted",
                "RefundOption": "MoneyBack",
                "ReturnsWithinOption": "Days_30",
                "Description": "If you are not satisfied, return the book for refund.",
                "ShippingCostPaidByOption": "Buyer"
            },
            "SellerProfiles": {
                "SellerPaymentProfile": {
                    "PaymentProfileName": "PayPal:Immediate pay",
                },
                "SellerReturnProfile": {
                    "ReturnProfileName": "30 Day Return Policy",
                },
                "SellerShippingProfile": {
                    "ShippingProfileName": "USPS First Class, Priority, Priority Express Flat Rate Envelope",
                }
            },
            "ShippingDetails": {
                "ShippingType": "Calculated",
                "ShippingServiceOptions": {
                    "ShippingServicePriority": "1",
                    "ShippingService": "USPSMedia"
                },
                "CalculatedShippingRate": {
                    "OriginatingPostalCode": "95125",
                    "PackagingHandlingCosts": "0.0",
                    "ShippingPackage": "PackageThickEnvelope",
                    "WeightMajor": "1",
                    "WeightMinor": "0"
                }
            },
            "Site": "US"
        }
    }

    item_response = api.execute('VerifyAddItem', myitem)
    print(item_response.dict())
    print("\n\n\n")
    print(item_response.reply)

except ConnectionError as e:
    print(e)
    print(e.response.dict())
