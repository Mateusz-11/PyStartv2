def calculate_common_dividor(a, b, c=2):
    result = []
    if b >= a:
        for i in range(c, b + 1):
            if b % i == 0 and a % i == 0:
                result.append(i)
    else:
        for i in range(c, a + 1):
            if b % i == 0 and a % i == 0:
                result.append(i)
    return result if result != [] else None


print(calculate_common_dividor(3, 6))
print(calculate_common_dividor(3, 6, 4))
print(calculate_common_dividor(16, 8))
