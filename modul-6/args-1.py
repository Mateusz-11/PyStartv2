def sum_of_numbers(*args, limit: int = 0) -> int:
    tmp_list = []
    for i in args:
        if i > limit:
            tmp_list.append(i)
    return sum(tmp_list)


print(sum_of_numbers(3, 5, 2, 4, limit=3))
