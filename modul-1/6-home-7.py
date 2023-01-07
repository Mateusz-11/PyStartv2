current_year = 2023
year_of_birth = int(input("Write the year of your birth: "))
age = current_year-year_of_birth

print(f"Your age is: {age}")

if age >= 18:
    print("You are adult")
else:
    print("You are not adult")

if year_of_birth % 4 == 0 and not year_of_birth % 100 == 0:
    print("You were born in a leap year")
elif year_of_birth % 400 == 0:
    print("You were born in a leap year")
else:
    print("You were not born in a leap year")
