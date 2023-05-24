from load_csv import read_csv

# Get the path to the CSV file
file_path = 'data/books.csv'

# Read the data from the CSV file
rows = read_csv(file_path)

# Print the data
print(rows)