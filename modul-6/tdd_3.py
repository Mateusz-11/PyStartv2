import pytest


def create_list_of_words(text: str) -> set:
    result = set()
    vowel_list = ['i', 'y', 'e', 'a', 'o', 'u', 'ą', 'ę']
    new_text = text.split(' ')
    for i in new_text:
        if i[0].lower() not in vowel_list and i[-1].lower() in vowel_list:
            result.add(i)
    return result


@pytest.mark.parametrize("text,expected", [
    ("Ala ma kota", {'ma', 'kota'}),
    ("Ala MA KOTA", {'MA', 'KOTA'}),
    ("Ala Ma KOTA", {'Ma', 'KOTA'}),
    ("ala ma kota", {'ma', 'kota'}),
    ("Ala ma nowy dom", {'ma', 'nowy'}),
    ("Nowy pies i kot", {'Nowy'}),

])
def test_search_words(text, expected):
    search_words = create_list_of_words(text)
    assert search_words == expected
