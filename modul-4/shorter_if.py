base_salary = 2000
intership_allowance = 0.1 if int(input("How long do you work here? ")) > 2 else 0.02
sales_bonus = 0.25 if int(input("How much did you sell? ")) > 30 else 0
for_the_active = 0.08 if int(input("How long do you work here?")) > 1 and int(input("What time work do you have (in hour)?")) > 169 else 0.02

print(f"Total sallary is: {base_salary + (base_salary*intership_allowance) + (base_salary * sales_bonus) + (base_salary* for_the_active)}")