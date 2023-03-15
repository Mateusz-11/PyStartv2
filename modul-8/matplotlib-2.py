import csv

with open('operacje.csv', encoding='utf8', newline='') as file:
    columns = ['data', 'rodzaj operacji', 'opis operacji', 'kwota operacji']
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

