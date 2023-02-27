def most_frequency_word(*args: str, ignore_case=True):
    tmp_dict = {}
    # V1
    # for i in args:
    #     i = i.lower() if ignore_case == True else i
    #
    #     if i not in tmp_dict.keys():
    #         tmp_dict[i] = 1
    #     else:
    #         tmp_dict[i] += 1

     # V2
    for arg in args:
        arg = arg.lower() if ignore_case else arg
        tmp_dict[arg] = tmp_dict.get(arg, 0) + 1

    value = 0
    for k, v in tmp_dict.items():
        if v == max(tmp_dict.values()):
            return k, tmp_dict


# print(most_frequency_word(False, 'test', 'test', 'peter', 'key', 'key', 'key'))
print(most_frequency_word('alpha', 'alpha', 'peter', 'Key', 'key', 'key', ignore_case=False))
print(most_frequency_word('alpha', 'alpha', 'peter', 'Key', 'key', 'key', ignore_case=True))
print(most_frequency_word('alpha', 'Alpha', 'peter', 'key', 'Key', 'key', ignore_case=True))
