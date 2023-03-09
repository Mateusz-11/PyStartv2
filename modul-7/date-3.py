from datetime import datetime, timedelta

date_start = datetime.strptime(input('Data rozpoczecia dd.mm.rrrr: '), '%d.%m.%Y')
date_end = datetime.strptime(input('Data zakonczenia dd.mm.rrrr: '), '%d.%m.%Y')
day_salary = int(input('Pensja dzienna: '))

diff = date_end - date_start

while (date_start <= date_end):
    print(date_start)
    date_start += timedelta(days=1)

print(f'Pracownik zarobi: {day_salary * diff.days}')
