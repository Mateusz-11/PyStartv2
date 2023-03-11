with open('transakcje.txt') as file:
    for line in file:
        date, description, amount = line.strip().split(';')
        print(date, description, amount)