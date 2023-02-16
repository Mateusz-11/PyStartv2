choice = int(input("What do you want to do? 1-multiplication, 2-division, 3-addition, 4-substraction: "))
first_nr = int(input("Number 1 = "))
second_nr = int(input("Number 2 = "))

match choice:
    case 1:
        print(f"{first_nr * second_nr}")
    case 2:
        print(f"{first_nr / second_nr}")
    case 3:
        print(f"{first_nr + second_nr}")
    case 4:
        print(f"{first_nr - second_nr}")
    case _:
        print("Not allowed choice")
