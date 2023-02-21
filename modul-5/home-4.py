def count_letters(text: str, start='(', end=')'):
    should_i_count = False
    counter = 0

    for char in text:
        if char == end:
            should_i_count = False

        if should_i_count:
            counter += 1

        if char == start:
            should_i_count = True

    return counter


print(count_letters('(ala) ma (kota)'))
print(count_letters('ala ma (kota)'))
print(count_letters('<> kod <103>', '<', '>'))
print(count_letters('abrakadabra'))
