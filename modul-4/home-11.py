text_1 = input("Text a word 1: ")
text_2 = input("Text a word 2: ")

#  v1  Lists
# result = []
# for char1 in text_1:
#     if char1 in text_2:
#         result.append(char1)
#
# print(set(result))


# V2 Sets

text_1 = set(text_1)
text_2 = set(text_2)

common_letters = text_1 & text_2
print(common_letters)