import datetime


def print_values(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print_values(value)
        else:
            print(value)

my_dict = {'Timestamp': datetime.datetime(2023, 5, 4, 19, 27, 50), 'Ack': 'Success', 'Version': '1207', 'Build': 'E1207_CORE_APISIGNIN_19151597_R1', 'User': {'AboutMePage': 'false'}}

print_values(my_dict)
            
#get all values of the dictionary, including nested dictionaries:
#def get_all_values(nested_dictionary):
    #for key, value in nested_dictionary.items():
        #if type(value) is dict:
           #get_all_values(value)
       # else:

