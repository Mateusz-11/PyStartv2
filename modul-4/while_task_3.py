import random

random_number = random.randint(1, 100)

try_nr = 1
user_answer = 0

while user_answer != random_number:
    try:
        user_answer = int(input("Guess a number from 1 to 100: "))
    except ValueError:
        print("Wrong answer!")
    if user_answer > random_number:
        print(f"Too big! Your {try_nr} try.")
    elif user_answer < random_number:
        print(f"Too small! Your {try_nr} try.")
    try_nr += 1
    print("---" * 10)

print("Congratulations you guessed it!")
