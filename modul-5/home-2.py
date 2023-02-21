def filter_even_numbers(numbers: list):
    set_numbers = set()
    for i in numbers:
        if i % 2 == 0:
            set_numbers.add(i)
    return set_numbers


print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
