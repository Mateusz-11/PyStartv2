from datetime import date

today = date.today()

print(f'Dzis jest: {today}')

formatted = today.strftime("%d.%m.%Y")
print(formatted)

