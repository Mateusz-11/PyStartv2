from datetime import datetime

date_start = input('Data rozpoczecia dd.mm.rrrr: ')
date_end = input('Data zakonczenia dd.mm.rrrr: ')
day_salary = int(input('Pensja: '))

d_start = datetime.strptime(date_start, '%d.%m.%Y')
d_end = datetime.strptime(date_end, '%d.%m.%Y')

diff = d_end - d_start

print(f'Pracownik zarobi: {day_salary * diff.days}')
