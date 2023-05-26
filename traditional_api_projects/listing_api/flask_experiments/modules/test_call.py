#from load_csv import read_csv
from additem import add_item
# Get the path to the CSV file
#file_path = 'data/books.csv'

# Read the data from the CSV file
#rows = read_csv(file_path)

# Print the data
#print(rows)

product_list = [(1,), (2,), (3,)]
token = 1

results = add_item(product_list, token)

print("\nRESULTS:\n", results)