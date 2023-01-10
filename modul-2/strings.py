# EX-1
first_name = input("Write your name: ")

# if first_name[-1] == "a":
if first_name.endswith('a'):
    print("Witam Panią")
else:
    print("Witam Pana")

# EX-2
password = input("Write new password: ")
passord_cipher = password.replace('a', '@').replace('s', '$')

print(passord_cipher)

# EX-3
text = "Pies to najlepszy przyjeciel człowieka, lecz nie każdy pies o tym wie"
number = text.lower().count("pies")

print(number)

# EX-4
text = "12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek."
text_2 = text.split()
# print(text_2)
result = 0

for t in text_2:
    if t.isnumeric():
        result += int(t)

print(f'Total weight of products is: {result} kg')
