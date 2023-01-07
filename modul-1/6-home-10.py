number = int(input('Write number day of week: '))

if number == 1:
    print("Poniedziałek")
elif number == 2:
    print("Wtorek")
elif number == 3:
    print("Środa")
elif number == 4:
    print("Czwartek")
elif number == 5:
    print("Piątek")
elif number == 6:
    print("Sobota")
elif number == 7:
    print("Niedziela")
else:
    print("Error - the number is incorrect")

match number:
    case 1: print("Poniedziałek")
    case 2: print("Wtorek")
    case _: print("Error - the number is incorrect")

