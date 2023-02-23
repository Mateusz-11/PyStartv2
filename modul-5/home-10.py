def rand_number(number: int) -> int:
    numbers = list(str(number))
    # for num in str(number):
    #     numbers.append(num)
    result = sorted(numbers, reverse=True)
    return int("".join(result))


print(rand_number(12345))
print(rand_number(1998))
