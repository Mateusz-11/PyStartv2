with open('transakcje.txt', encoding='utf8') as file, open('przychody.txt', encoding='utf8', mode='w') as output:
    for transaction in file:
        date_of_transaction, description, amount = transaction.strip().split(';')
        amount = float(amount)
        if amount > 0:
            output.write(transaction)


def sum_of_income():
    total = 0
    with open('przychody.txt', encoding='utf8') as income_file:
        for line in income_file:
            _,_, amount = line.strip().split(';')
            total += float(amount)
    print(f'Sum of income: {total} zl')


sum_of_income()


