set_divisible_3 = set(range(3, 100, 3))
set_divisible_5 = set(range(5, 100, 5))

set_common_numbers = set_divisible_3 & set_divisible_5

print(set_common_numbers)