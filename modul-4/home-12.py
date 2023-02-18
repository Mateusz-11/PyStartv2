words = input("Text words separated by commas: ")
set_of_words = set(words.replace(",", "").lower().split(" "))

for _ in set_of_words:
    print(_)