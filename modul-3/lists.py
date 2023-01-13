# Ex-1
# sentence = input("Write text: ")
#
# split_sentence = sentence.split(" ")
# print("Amount of words", len(split_sentence))
# print("Amount of characters", len(sentence))


# Ex-2
# numbers = []
# for _ in range(5):
#     numbers.append(int(input("Write number: ")))
#
# max_number = max(numbers)
# min_number = min(numbers)
# print(f"Max number is: {max_number}")
# print(f"Min number is: {min_number}")


# Ex-3
names = 'Adam Mickiewicz, Adam Asnyk, Zbigniew Nienacki'
persons = names.split(', ')
list_of_names = []

for person in persons:
    first_name, last_name = person.split(' ')
    if first_name not in list_of_names:
        list_of_names.append(first_name)

list_of_names.sort(reverse=True)
print(list_of_names)
