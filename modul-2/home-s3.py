txt = "Litwo ojczyzno moja"
new_txt = ''

for counter, word in enumerate(txt.split(' ')):
    if counter % 2 == 0:
        new_txt = f'{new_txt} {word.lower()}'
    else:
        new_txt = f'{new_txt} {word.upper()}'

print((new_txt))