import csv

with open('data/faker_data.csv') as f:
    myreader = csv.DictReader(f)
    for row in myreader:
        print(row['name'])
