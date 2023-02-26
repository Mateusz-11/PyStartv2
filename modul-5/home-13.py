def sum_it(num: int) -> int:
    if num == 0:
        return 0
    return num + sum_it(num - 1)


print(sum_it(8))
print(sum_it(2))
print(sum_it(3))
