number = int(input("Write the number: "))

if number % 5 ==0 and number % 11 == 0:
    print("Number is divisible by 5 and 11")
elif number % 5 ==0:
    print("Number is divisible by 5")
elif number % 11 == 0:
    print("Number is divisible by 11")
else:
    print("Number is not divisible by 5 or 11")