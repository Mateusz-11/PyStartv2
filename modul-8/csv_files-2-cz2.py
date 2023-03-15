import csv
with open('cars.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for line in reader:
        print(line)