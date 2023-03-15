import csv

data = [
    {'name': 'Koenisgegg One 1',
     'time_to_100': 2.6,
     'speed_record': 450
     },
    {'name': 'SSC Tuatara',
     'time_to_100': 2.5,
     'speed_record': 460
     },
    {'name': 'Agera RS',
     'time_to_100': 3.1,
     'speed_record': 457
     },
]

columns = ['name', 'time_to_100', 'speed_record']

with open('cars.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for row in data:
        writer.writerow(row)