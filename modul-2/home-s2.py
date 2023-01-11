txt = "Być, albo nie być oto jest pytanie"

new_txt = ''

for char in txt:
    if char.isnumeric() or char.isalpha():
        new_txt += char


print(new_txt)