def most_frequency_word(ignore_case=True, *args: str):
    tmp_dict = {}
    for i in args:
        if ignore_case == True : i = i.lower()

        if i not in tmp_dict.keys():
            tmp_dict[i] = 1
        else:
            tmp_dict[i] += 1
    value = 0
    for k,v in tmp_dict.items():
        if v >= value:
            value = v
    return tmp_dict


# print(most_frequency_word(False, 'test', 'test', 'peter', 'key', 'key', 'key'))
print(most_frequency_word(False, 'test', 'test', 'peter', 'Key', 'key', 'key'))
print(most_frequency_word(True, 'test', 'test', 'peter', 'Key', 'key', 'key'))
print(most_frequency_word(True, 'test', 'Test', 'peter', 'key', 'Key', 'key'))
