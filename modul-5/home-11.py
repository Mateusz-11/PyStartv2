#  V1
# def reverse_numbers(number_list: list) -> list:
#     result_list = []
#     for i in number_list:
#         result_list.append(i * -1)
#
#     return result_list
# print(reverse_numbers([1, 2, 3, 4, 5]))
# print(reverse_numbers([-1, -2, -3, 4, 5]))


# V2 with MAP Function
def reverse_numbers(i: int) -> int:
    return i * -1


numbers = [-1, -2, -3, 4, 5]
result = map(reverse_numbers, numbers)
print(list(result))
