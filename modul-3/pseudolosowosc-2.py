import math
from random import randint

random_number = randint(1, 100)

print(f"Drawn number is: {random_number}")
print(f"Drawn number raised to the power is: {math.pow(random_number, 2)}")
print(f"Squared (round ceiling) is: {math.ceil(math.sqrt(random_number))}")
print(f"Squared (round floor) is: {math.floor(math.sqrt(random_number))}")

