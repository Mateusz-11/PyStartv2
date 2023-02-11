import math
from random import randint

random_number = randint(1, 100)

print(f"Drawn number is: {random_number}")
print(f"Drawn number raised to the power is: {math.pow(random_number, 2)}")
print(f"Drawn number squared is: {math.ceil(math.sqrt(random_number))} (round ceiling)")
print(f"Drawn number squared is: {math.floor(math.sqrt(random_number))} (round floor)")

