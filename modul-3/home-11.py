from random import choice, shuffle

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

user_points = 0

for _ in range(3):
    # random_choice = choice(list_of_country)
    shuffle(list_of_country)
    random_choice = list_of_country.pop()
    user_answer = input(f"Jaka jest stolica {random_choice['country']}?")
    if user_answer == random_choice['capital']:
        user_points += 1
        print('Dobrze!')
    else:
        print('Żle :(')
    print('---' * 10)

if user_points == 3:
    print('3 - bezbłędnie Ci poszło')
elif user_points == 2:
    print('2 - Tylko jeden błąd! Nieźle!')
elif user_points == 1:
    print('1 - Jeden punkt na otarcie łez')
elif user_points == 0:
    print('0 - Nastepnym razem pójdzie CI lepiej!')
