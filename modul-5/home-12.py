def convert_str_to_int(list_strings:list) ->list:
    return list(map(int, list_strings))

def convert_int_to_str(list_int:list) -> list:
    return list(map(str, list_int))

print(convert_int_to_str([1,2,3,4]))
print(convert_str_to_int(['1','2','3','4']))
