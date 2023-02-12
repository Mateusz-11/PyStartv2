from random import randint, choice

dishes = {
    'soup': ['pomidorowa', 'barszcz', 'rosół'],
    'dinner': ['pulpety', 'schabowy', 'golabki'],
    'dessert': ['lody', 'kisiel', 'ciasto'],
}

translation = {
    'soup': 'Zupa',
    'dinner': 'Drugie danie',
    'dessert': 'Deser'
}

## V1

# choiced_dict_of_dishes = {}
# for dish in dishes:
#     random_dish = (dishes[dish][randint(0, 2)])
#     choiced_dict_of_dishes[dish] = random_dish
#     print(choiced_dict_of_dishes)
#     print('---' * 10)
#
# for k, v in choiced_dict_of_dishes.items():
#     print(f"{k}: {v}")

## V2
for category, diches_at_category in dishes.items():
    dish_at_category = choice(diches_at_category)
    # print(f"{translation[category]}: {dish_at_category}")
    print(f"{translation.get(category, category)}: {dish_at_category}")
