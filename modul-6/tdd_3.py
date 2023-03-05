import pytest


def create_list_of_words(text: str) -> list:
    result = []
    vowel_list = ['i', 'y', 'e', 'a', 'o', 'u', 'ą', 'ę']
    new_text = text.split()
    for i in new_text:
        if i[0] not in vowel_list and i[-1] in vowel_list:
            result.append(i)
    return result


@pytest.mark.parametrize("text,expected", [
    ("ala ma kota", ['ma', 'kota']),
    ("ala ma nowy dom", ['ma', 'nowy']),

])
def test_search_words(text, expected):
    search_words = create_list_of_words(text)
    assert search_words == expected
