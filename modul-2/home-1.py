# Part 1
number = int(input("Give me a number: "))
total = ""
counter = 0

for i in range(2, number + 1, 2):
    total += (str(i) + ',')
    counter += 1

print(total)

# Part 2
r_sum = 0
r_mul = 1
for i in range(2, number + 1):
    if i % 2 == 0:
        r_sum += i
        r_mul *= i

avg_num = r_sum / counter

print(f'Suma to: {r_sum}')
print(f'Iloczyn to: {r_mul}')
print(f'Średnia to: {avg_num}')
