first_name = input("Wpisz swoje imię: ")
last_name = input("Wpisz swoje nazwisko: ")

with open('users.txt', 'a', encoding='utf8') as file:
    file.write(f"{first_name} {last_name}\n")
