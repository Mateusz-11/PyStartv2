import csv

## Zapis pliku CSV

with open('orders.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    writer.writerow([4, 'Piotr', 'Nowak'])

## Odczyt pliku CSV
with open('orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(row['first_name'], row['last_name'])