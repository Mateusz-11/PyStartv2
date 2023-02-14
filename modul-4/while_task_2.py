from audioop import avg

number = 0
list_of_number = []
while True:
    number_user = int(input("Text a greater then previous number: "))
    if number < number_user:
        number = number_user
        list_of_number.append(number_user)
    else:
        break

print(list_of_number)
print(f"Average of this number is: {sum(list_of_number)/len(list_of_number)}")
