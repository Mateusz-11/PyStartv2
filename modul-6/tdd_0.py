def count_letters(text, start='(', end=')'):
    return len(text)


def test_count_letters():
    text = 'ala'
    text2 = 'Money'
    text3 = 'Money'

    value = count_letters(text)
    value2 = count_letters(text2)

    assert value == 3
    assert value2 == 5

print(count_letters('text'))