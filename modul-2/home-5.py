from math import sqrt, ceil

number = int(input('GIve the number: '))
is_prime = True

for div in range(2, ceil(sqrt(number))+1):
    if number % div == 0:
        is_prime = False
        break

if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")