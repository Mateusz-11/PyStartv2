from datetime import date

today = date.today()
birthday_this_year = date(today.year + 1, 5, 13)

diff = birthday_this_year - today
print(f'Do urodzin pozostało: {diff.days} dni')
