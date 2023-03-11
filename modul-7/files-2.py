income = []

with open('transakcje.txt') as file:
    for line in file:
        date, description, amount = line.strip().split(';')
        if int(amount) > 0:
            income.append({"amount": int(amount)})

# print(income)
with open('przychody.txt', mode='w') as file:
    for amount in income:
        file.write(f"{amount.get('amount')}\n")


def sum_of_income():
    result = 0
    with open('przychody.txt') as file1:
        for line1 in file1:
            data = line1.strip()
            result += int(data)
    print(f'Sum of income: {result} zl')


sum_of_income()
