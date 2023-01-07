################
print('#1 BMI')
height = float(input("Text your height (m): "))
weight = int(input("Text your height (kg): "))

bmi = weight/(height**2)
print(height)
print(weight)
print(bmi)

print(f"Your BMI is {bmi}")

################
print('#2 calc vat')
vat = 0.23
netto = int(input("Text netto amount: "))
brutto = netto * (1 + vat)

print(f"Brutto amount is: {brutto}")

################
print('#3 figure field')
a = int(input("Text A dimension: "))
b = int(input("Text B dimension: "))
h = int(input("Text H dimension: "))

field = ((a+b)*h)/2

print(f"Field equal: {field}")