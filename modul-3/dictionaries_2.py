txt = input("Wpisz tekst: ")

#  V1
txt_list = txt.split(" ")
# txt_list_short = []
#
# for i in txt_list:
#     if i not in txt_list_short:
#         txt_list_short.append(i)
#
# # print(txt_list)
# # print(txt_list_short)
# values = []
# for i in txt_list_short:
#     values.append(txt_list.count(i))

# print(values)

# result_dict = dict(zip(txt_list_short, values))

#  V2
result_dict = {}

for word in txt_list:
    ### V2-A
    # if word not in result_dict:
    #     result_dict[word] = 0
    #
    # result_dict[word] = result_dict[word] + 1

    ### V2-B
    # result_dict[word] = result_dict.get(word, 0) + 1

    ### V2-C
    result_dict.update({word: result_dict.get(word, 0) + 1})

# lambda - set the column (values), which we sort by
result_sorted = sorted(result_dict.items(), key=lambda x:x[1], reverse=False)
result_dict_sorted = dict(result_sorted)

print(result_dict)
print(result_dict_sorted)