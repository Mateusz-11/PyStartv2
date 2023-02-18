text = "Python likes purple birds."
text_list = text.lower().split(" ")
letter = "p"

for el in text_list:
    if el.startswith(letter):
        text_list.remove(el)

print(" ".join(text_list))
