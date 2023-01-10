numbers = (1, 4, 7, 2, 7, 5, 15, 22, 77, 34, 98, 12, 56, 33)

for n in numbers:
    if n % 4 == 0 or n % 5 == 0:
        print(n)

names = ('Peter', 'Anna', 'John', 'Mathew', 'Hannah')

for n in names:
    if len(n) > 5:
        print(n)

for i in reversed(range(1, 5)):
    for x in range(1, i + 1):
        print(x, end=' ')
    print()
