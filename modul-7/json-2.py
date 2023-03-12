from json import load, dump


def calculate_expenses():
    choice = input('Co chcesz zrobić? [d] Dodaj wydatek [w] Wypisz wszystkie: ')
    with open('expenses.json') as file:
        expenses = load(file)
    if choice == 'd':
        new_type = input('Czego dotyczy wydatek? ')
        new_amount = int(input('Jaka kwota została wydane? '))

        expenses.append({
            'type': new_type,
            'amount': new_amount
        })
        with open('expenses.json', 'w') as file:
            dump(expenses, file)

    elif choice == 'w':
        total = 0
        for expense in expenses:
            total += expense.get('amount')
            print(expense.get('type'))
            print(expense.get('amount'))
            print('--' * 10)
        print(f"Łączne wydatki = {total} zl")


calculate_expenses()
