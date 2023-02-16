from sys import argv
# pesel = "18210177915"
# pesel = "99010124415"

# Uruchomienie w cmd: python password_walidator.py 99010124415
if len(argv) == 2:  # długość tupli - nazwa pliku + wartość
    pesel = argv[1]  # wartość w tupli pod indeksem 1
else:
    pesel = input("Text your pesel number to check: ")

try:
    pesel_list = list(map(int, pesel))
except ValueError:
    print("Wrong data")

multipiler = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

try:
    control_sum = 0
    for pes, multi in zip(pesel_list, multipiler):
        control_sum += pes * multi

    if len(pesel_list) == 11 and control_sum % 10 == 0:
        print("Pesel is ok")
    else:
        print("Pesel is wrong")
except NameError:
    quit()
