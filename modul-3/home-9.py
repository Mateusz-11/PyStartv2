# deck - talia kart
from random import choice

colors = [chr(9824), chr(9830), chr(9829), chr(9827)]
values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

print(colors)
print(values)

deck = []
for color in colors:
    for value in values:
        deck.append(f"{value}{color}")

print(deck)
print(len(deck))

random_card = choice(deck)

print(random_card)