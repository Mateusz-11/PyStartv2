def count_a_strong(a=1):
    if a == 0:
        return 1
    return count_a_strong(a-1) * a


print(count_a_strong(0))
print(count_a_strong(1))
print(count_a_strong(2))
print(count_a_strong(3))
print(count_a_strong(4))
print(count_a_strong(5))
print(count_a_strong(6))
print(count_a_strong(7))
print(count_a_strong(8))