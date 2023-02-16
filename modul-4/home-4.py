account_balance = 1000

while True:
    if account_balance >= 0:
        print(f"Your Account Balance = {account_balance}. What do you do? ")
        try:
            choice = int(input("1 - cash withdrawal / 2 - cash payment / 3 exit program >> "))
        except ValueError:
            print("Wrong order!")
            exit()
        if choice == 1:
            amount = float(input("What amount?"))
            if account_balance >= amount:
                account_balance -= amount
            else:
                print("You don't have enough cash.")
        elif choice == 2:
            amount = float(input("What amount?"))
            account_balance += amount
        elif choice == 3:
            exit()
        else:
            print("Wrong order")
        print("---" * 10)
