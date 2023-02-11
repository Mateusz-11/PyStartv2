import random

options = 'paper', 'stone', 'scissors'

choice_user = input("Write your move (paper / stone / scissors): ")
choice_computer = random.choice(options)

print(f"Choice user: {choice_user}")
print(f"Choice computer: {choice_computer}")

if choice_computer == 'paper' and choice_user == 'paper' or choice_computer == 'stone' and choice_user == 'stone' or choice_computer == 'scissors' and choice_user == 'scissors':
    print("Draw")
elif choice_computer == 'paper' and choice_user == 'stone' or choice_computer == 'stone' and choice_user == 'scissors' or choice_computer == 'scissors' and choice_user == 'paper':
    print('Computer won')
elif choice_computer == 'paper' and choice_user == 'scissors' or choice_computer == 'stone' and choice_user == 'paper' or choice_computer == 'scissors' and choice_user == 'stone':
    print('User won')
else:
    print('Wrong order!')
