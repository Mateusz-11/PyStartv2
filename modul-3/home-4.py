animals_2 = {}
for _ in range(5):
    name = input("Jaka jest nazwa zwierzęcia? ")
    nr_of_legs = int(input("Ile ma nóg? "))
    animals_2[name] = nr_of_legs

print(animals_2)

animals = {
    'kon': 4,
    'pies': 4,
    'stonoga': 100,
    'stonoga2': 100,
    'kaczka': 2,
    'pajak': 8,
    'slimak': 0,
}


number_max_legs = 0
for animal in animals:
    if animals[animal] > number_max_legs:
        number_max_legs = animals[animal]

for animal in animals:
    if animals[animal] == number_max_legs:
        print(f"{animal} - {animals[animal]}")

# print(f'Największą liczbę nóg ma {}, ta ilość to: {number_max_legs}')