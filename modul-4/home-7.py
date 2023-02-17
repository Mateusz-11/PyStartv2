even_numbers_list = []
odd_numbers_list = []
try:
    while (choice := int(input('Write w number: '))) != 0:
        # if choice % 2 == 0:
        #     even_numbers_list.append(choice)
        # else:
        #     odd_numbers_list.append(choice)
        even_numbers_list.append(choice) if choice % 2 == 0 else odd_numbers_list.append(choice)
except ValueError:
    print("Wrong data.")
    exit()

print(f"Amount of even numbers: {len(even_numbers_list)}")
for _ in even_numbers_list:
    print(_)
print("---" * 10)

print(f"Amount of odd numbers: {len(odd_numbers_list)}")
for _ in odd_numbers_list:
    print(_)
