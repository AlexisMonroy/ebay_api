import csv
import sqlite3
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'books.csv'))

with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = []

    for row in reader:
        modified_row = [int(cell) if cell.isdigit() else cell for cell in row]
        rows.append(modified_row)
    
    print(rows)
# Create a new SQLite database
conn = sqlite3.connect('inventory.db')

# Create a new table in the database
conn.execute('CREATE TABLE IF NOT EXISTS books (ID INTEGER PRIMARY KEY, Title TEXT NULL, Author TEXT NULL, Units INTEGER NULL, Illustrator TEXT NULL, Genre TEXT NULL, Publisher TEXT NULL, Publication_Year INTEGER NULL, Price REAL NULL, Description TEXT NULL, Condition TEXT NULL, Condition_Description TEXT NULL, Format TEXT NULL, Features TEXT NULL, Language TEXT NULL, Topic TEXT NULL, Book_Series TEXT NULL, Type TEXT NULL, Narrative_Type TEXT NULL, Edition TEXT NULL, Manufactured TEXT NULL, Inscribed TEXT NULL, Intended_Audience TEXT NULL, Vintage TEXT NULL, Signed TEXT NULL)')

# Insert the data into the table

for row in rows:

    conn.execute('INSERT OR IGNORE INTO books (ID, Title, Author, Units, Illustrator, Genre, Publisher, Publication_Year, Price, Description, Condition, Condition_Description, Format, Features, Language, Topic, Book_Series, Type, Narrative_Type, Edition, Manufactured, Inscribed, Intended_Audience, Vintage, Signed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
