my_dict = {'Timestamp': '2023', 'CategoryArray': {'Category': [{'BestOfferEnabled': 'true', 'CategoryLevel': '1', 'CategoryParentID': '20081'}, {'BestOfferEnabled': 'true', 'AutoPayEnabled': 'true', 'CategoryID': '550', 'CategoryLevel': '1', 'CategoryName': 'Art', 'CategoryParentID': '550'}, {'BestOfferEnabled': 'true', 'AutoPayEnabled': 'true', 'CategoryID': '2984', 'CategoryLevel': '1', 'CategoryName': 'Baby', 'CategoryParentID': '2984'}, {'BestOfferEnabled': 'true', 'AutoPayEnabled': 'true', 'CategoryID': '267', 'CategoryLevel': '1', 'CategoryName': 'Books & Magazines', 'CategoryParentID': '267'}]}, 'Category Count': '34'}

def check_list(d):
        for item in d:
            if isinstance(item, dict):
                print_values(item)
            else:
                #print the item and the dictionary key:
                print(item)
                

def print_values(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print_values(value)
        elif isinstance(value, list):
            check_list(value)
        else:
            print(key, value)

print_values(my_dict)

