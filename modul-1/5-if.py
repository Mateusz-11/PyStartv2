##############
print("#1 Modulo")
a = int(input("Give a number: "))

if a % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


##############
print("#2 bigger smaller")
a = int(input("Number A: "))
b = int(input("Number B: "))

if a > b:
    print("A is bigger")
elif a == b:
    print("A equal B")
else:
    print("A is smaller")


##############
print("#3 temperature")
temp = int(input("Text a temperature in Celcius: "))

if temp <= 10:
    print("Stay at home")
elif 10 < temp < 20:
    print("Take a jacket")
else:
    print("Have a good time!")
