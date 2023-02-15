answer = None
sum_of_numbers = 0

## V1 Without Walrus operator
# while answer != 0:
#     answer = int(input("Text a positive number: "))
#     sum_of_numbers += answer

## V2 With Walrus Operator
while (answer:=int(input("Text a positive number: "))) != 0:
    sum_of_numbers += answer

print(f"The Sum is: {sum_of_numbers}")
