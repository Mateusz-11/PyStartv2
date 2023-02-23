def stat(random_list: list) -> dict:
    dict_result = {}
    dict_result['total'] = len(random_list)
    dict_result['mean'] = sum(random_list) / len(random_list)
    dict_result['max'] = max(random_list)
    dict_result['min'] = min(random_list)
    return dict_result


print(stat([1, 2, 3, 4, 5]))
