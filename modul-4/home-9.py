text = "testowy tekst do szyfrowania"
text = text.lower()
SECRET = 3

encrypted_text = ''
for char in text:
    if char.isalpha():
        char = chr((ord(char)) - SECRET - ord('A') % 26 + ord('A'))

    encrypted_text += char

print(encrypted_text)