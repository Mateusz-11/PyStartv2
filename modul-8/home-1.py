from datetime import datetime

products = set()

while (product_name := input('Wpisz nazwę produktu')) != 'koniec':
    products.add(product_name)

today = datetime.now()
filename = today.strftime('%d%m%Y') + '.txt'

with open(filename, 'w') as file:
    file.write('\n'.join(products))