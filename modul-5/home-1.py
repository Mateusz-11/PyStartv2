a = [2, 4, 6]
b = [8, 6, 4]


def sum_list(list_a, list_b):
    result = []
    for x, y in zip(list_a, list_b):
        result.append(x + y)
    return result


print(sum_list(a, b))
