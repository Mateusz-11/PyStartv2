animals = [
    {'name': 'pies', 'breed': 'owczarek niemiecki'},
    {'name': 'kot', 'breed': 'syberyjski'},
    {'name': 'konik polny', 'breed': 'arab'},
    {'name': 'świnia', 'breed': 'dwudzielna'},
    {'name': 'żaba', 'breed': 'żaba moczarowa'},
    {'name': 'mrówka', 'breed': 'mrówka miodowa'},
]

max_length = None
for animal in animals:
    length = len(animal['name']) + len(animal['breed'])
    # print(animal['name'], length)
    if max_length is None or length > max_length:
        max_length = length

for animal in animals:
    length = len(animal['name']) + len(animal['breed'])
    if length == max_length:
        print(animal['name'], animal['breed'], length)
