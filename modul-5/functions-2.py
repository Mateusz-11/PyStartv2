tuple_of_letters = ('a', 'o', 'e', 'u', 'o', 'y')
vowels_in_word = []


def get_vowels():
    word = input("Write a word: ")
    for i in word.lower():
        if i in tuple_of_letters:
           vowels_in_word.append(i)
    return set(vowels_in_word)

print(get_vowels())