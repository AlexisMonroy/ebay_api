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


get_categories = {'CategorySiteID': 0, 'DetailLevel': 'ReturnAll', 'LevelLimit': 1, 'ViewAllNodes': True}

cat_reponse = api.execute('GetCategories', get_categories)
print(cat_reponse.dict())
print("\n\n\n")
print(cat_reponse.reply)
print("\n\n\n")

