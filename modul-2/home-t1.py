numbers = ()

for i in range(12,1024):
    if i % 6 == 0:
        numbers += i


print(type(numbers))