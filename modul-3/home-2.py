fruits = {
    'jablko': 3.33,
    'banan': 4.32,
    'winogron': 5.09,
    'gruszka': 3.44,
    'arbuz': 1.23,
}

print(f"Cena jablka to: {fruits['jablko']}")
print(f"Cena banana to: {fruits['banan']}")

for fruit in fruits:
    if fruit in ('jablko', 'banan'):
        print(fruits[fruit])