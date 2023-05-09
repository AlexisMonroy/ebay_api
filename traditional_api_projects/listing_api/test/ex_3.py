my_dict = {'Timestamp': '2023', 'CategoryArray': {'Category': [{'BestOfferEnabled': 'true', 'CategoryLevel': '1', 'CategoryParentID': '20081'}, {'BestOfferEnabled': 'true', 'AutoPayEnabled': 'true', 'CategoryID': '550', 'CategoryLevel': '1', 'CategoryName': 'Art', 'CategoryParentID': '550'}, {'BestOfferEnabled': 'true', 'AutoPayEnabled': 'true', 'CategoryID': '2984', 'CategoryLevel': '1', 'CategoryName': 'Baby', 'CategoryParentID': '2984'}, {'BestOfferEnabled': 'true', 'AutoPayEnabled': 'true', 'CategoryID': '267', 'CategoryLevel': '1', 'CategoryName': 'Books & Magazines', 'CategoryParentID': '267'}]}, 'Category Count': '34'}
   
def check_list(d, result):
    for item in d:
        if isinstance(item, dict):
            print_values(item, result)
        else:
            # store the item and the dictionary key:
            result.append((key, item))

def print_values(d, result):
    for key, value in d.items():
        if isinstance(value, dict):
            print_values(value, result)
        elif isinstance(value, list):
            check_list(value, result)
        else:
            # store the key and value pair:
            result.append((key, value))

result = []
print_values(my_dict, result)
print(result)

for key, value in result:
    print(key, value)