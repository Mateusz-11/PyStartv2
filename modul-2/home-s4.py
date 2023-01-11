text = "Lito ojczyzno moja Ty jesteś.."

for word in text.split(' '):
    if word[0].lower() == word[-1].lower():
        print(word)

new_text  = ''
vowels = "aeiouyąę"

for char in text:
    if char.lower() not in vowels:
        new_text += char

print(new_text)