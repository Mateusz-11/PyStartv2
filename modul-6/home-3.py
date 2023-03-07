def count_words(sentence: str, word: str) -> int:
    return sentence.count(word)


def test_count_words():
    assert count_words('Python i Python', 'Python') == 2
    assert count_words('"I love apples, apple are my favorite fruit"', 'apple') == 2
