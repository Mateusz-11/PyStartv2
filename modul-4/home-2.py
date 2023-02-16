try:
    amount = float(input("What amount you want to convert? "))
except ValueError:
    print("Wrong answer!")
    quit()

kg_lb = 35.274
kg_oz = 2.20462

match int(input("1 - kilograms to pounds / 2 - pounds to kilograms / 3 - kilograms to pounds / 4 - pounds to kilograms")):
    case 1: print(f"{amount * kg_oz}")
    case 2: print(f"{amount / kg_oz}")
    case 3: print(f"{amount * kg_lb}")
    case 4: print(f"{amount / kg_lb}")
    case _: print("Not allowed choice")
