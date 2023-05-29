#from load_csv import read_csv
from additem import add_item
import datetime
# Get the path to the CSV file
#file_path = 'data/books.csv'

# Read the data from the CSV file
#rows = read_csv(file_path)

# Print the data
#print(rows)

product_list = [(1,), (2,), (3,), (4,)]
token = 1

results = add_item(product_list, token)

print("\nRESULTS:\n", results)
print("Type:\n", type(results))

for i in range(0, len(results)):
    print("\nRESULTS:\n", results[i])

with open('call_output.txt', 'a') as f:
    print("\nTime:\n", datetime.datetime.now(), file=f)
    print("\nRESULTS:\n", results, file=f)
    print("\nEnd Time:\n", datetime.datetime.now(), file=f)

    
          