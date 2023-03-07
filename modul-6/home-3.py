def count_words(sentence: str, word: str) -> int:
    # return sentence.count(word)
    counter = 0
    for i in sentence.split(' '):
        if i == word:
            counter += 1
    return counter

def test_count_words():
    assert count_words('Python i Python', 'Python') == 2
    assert count_words('Python i Python', 'python') == 0
    assert count_words('Python i python', 'python') == 1
    assert count_words('Java i PHP', 'Python') == 0
    assert count_words('"I love apples, apple are my favorite fruit"', 'apple') == 1
