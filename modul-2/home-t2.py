person = ('John', "Smith", 40)

print("imię:", person[0])
print("nazwisko: ", person[1])
print("wiek: ", person[2])

print("---" * 20)

calculations = (1, 2, 3), (4, 5, 6), (7, 8, 9)

for calculation in calculations:
    print(f'{calculation[0]} + {calculation[1]} + {calculation[2]} = {sum(calculation)}')