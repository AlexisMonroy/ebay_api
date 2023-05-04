from flask import Flask, render_template
import datetime 


app = Flask(__name__)

@app.route('/')
def index():
    user_data = {'Timestamp': datetime.datetime(2023, 5, 4, 19, 27, 50), 'Ack': 'Success', 'Version': '1207', 'Build': 'E1207_CORE_APISIGNIN_19151597_R1', 'User': {'AboutMePage': 'false', 'EIASToken': 'nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6MGlICgAJSAqQidj6x9nY+seQ==', 'Email': 'twtmarket.ca@gmail.com', 'FeedbackScore': '182', 'UniqueNegativeFeedbackCount': '0', 'UniquePositiveFeedbackCount': '14', 'PositiveFeedbackPercent': '100.0', 'FeedbackPrivate': 'false', 'IDVerified': 'false', 'eBayGoodStanding': 'true', 'NewUser': 'false', 'RegistrationDate': datetime.datetime(2020, 12, 30, 6, 15, 15), 'Site': 'US', 'Status': 'Confirmed', 'UserID': 'thewanderingtianquiztli', 'UserIDChanged': 'false', 'VATStatus': 'NoVATTax', 'SellerInfo': {'AllowPaymentEdit': 'true', 'CheckoutEnabled': 'true', 'CIPBankAccountStored': 'false', 'GoodStanding': 'true', 'LiveAuctionAuthorized': 'false', 'MerchandizingPref': 'OptIn', 'QualifiesForB2BVAT': 'false', 'SellerGuaranteeLevel': 'NotEligible', 'SchedulingInfo': {'MaxScheduledMinutes': '30240', 'MinScheduledMinutes': '0', 'MaxScheduledItems': '3000'}, 'StoreOwner': 'false', 'SellerBusinessType': 'Private', 'PaymentMethod': 'NothingOnFile', 'CharityRegistered': 'false', 'SafePaymentExempt': 'false', 'CharityAffiliationDetails': {'CharityAffiliationDetail': {'CharityID': '19491', 'AffiliationType': 'Community', 'LastUsedTime': datetime.datetime(2021, 5, 16, 3, 16, 20)}}, 'TransactionPercent': '98.6', 'RecoupmentPolicyConsent': None, 'DomesticRateTable': 'false', 'InternationalRateTable': 'false'}, 'BusinessRole': 'FullMarketPlaceParticipant', 'EBaySubscription': 'FileExchange', 'UserSubscription': ['FileExchange'], 'eBayWikiReadOnly': 'false', 'MotorsDealer': 'false', 'UniqueNeutralFeedbackCount': '0', 'EnterpriseSeller': 'false'}
                 }
    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run()