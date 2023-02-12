from random import choice

list_of_country = [
    {
        'country': 'Polska',
        'capital': 'Warszawa',
    },
    {
        'country': 'Niemcy',
        'capital': 'Berlin',
    },
    {
        'country': 'Hiszpania',
        'capital': 'Madryt',
    },
]

random_choice = choice(list_of_country)

user_answer = input(f"Jaka jest stolica {random_choice['country']}?")

if user_answer == random_choice['capital']:
    print('Dobrze!')
else:
    print('Żle :(')
