from datetime import datetime, timedelta

date_start = datetime.strptime(input('Data rozpoczecia dd.mm.rrrr: '), '%d.%m.%Y')
date_end = datetime.strptime(input('Data zakonczenia dd.mm.rrrr: '), '%d.%m.%Y')
day_salary = int(input('Pensja dzienna: '))

diff = date_end - date_start
salary = (diff.days + 1) * day_salary

while (date_start <= date_end):
    if date_start.strftime('%a') in ['Sat', 'Sun']:
        salary += day_salary
    print(date_start.strftime('%a%d.%m.%Y'))
    date_start += timedelta(days=1)

print(f'Pracownik zarobi: {salary}')
