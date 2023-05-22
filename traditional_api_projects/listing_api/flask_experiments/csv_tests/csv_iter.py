import csv

with open('Test_Books - Sheet1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    parent_dicts = []
    for row in reader:
        parent_dict = {row[0]: {}}
        child_dict = {}
        for i in range(1, len(header)):
            child_dict[header[i]] = row[i]
        parent_dict[row[0]] = child_dict
        parent_dicts.append(parent_dict)

print(parent_dicts)

