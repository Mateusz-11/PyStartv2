a = float(input("Write num A: "))
b = float(input("Write num B: "))
c = float(input("Write num C: "))

max_val = c
min_val = c

if a > b:
    if a > c:
        max_val = a
    else:
        max_val = c
else:
    if b > c:
        max_val = b
    else:
        max_val = c

if a < b:
     if a < c:
         min_val = a
     else:
         min_val = c
else:
    if b < c:
        min_val = b
    else:
        min_val = c

print(f'The biggest number is {max_val}, the smallest number is {min_val}')