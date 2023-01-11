numbers = tuple(range(12, 1024, 6))

print(numbers)

print(f"Ilość: {len(numbers)}")

print(f"pierwsze liczby: {numbers[:3]}")

print(f"Przed ostatni element: {numbers[-2]}")

print(f"Co 6 element od 4: {numbers[3::6]}")

print(f"co 3 element licząc od końca: {numbers[::-3]}")

print(f"Śr ost 10 wartości: {sum(numbers[-10::]) / 10}")
