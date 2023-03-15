# Do zrobienia:
# 1. Zapis do json
# 2. Zapis z nazwą pliku ze slugu
# 3. Pobieranie danych po slugu
# 4. DOdanie wyjątku, jeśli nei znajdzie w bazie

from requests import get

url = 'https://wolnelektury.pl/api/books'
wanted_author = "Ajschylos"
# wanted_author = input("Książek jakiego autora szukasz? ")
response = get(url)
data = response.json()

books = []

for book in data:
    if book['author'] == wanted_author:
        print(f"Książka: {book['title']}")
        books.append(book['title'].strip())


with open('1-test.txt', 'w', encoding='utf8') as file:
    file.write('\n'.join(books))

