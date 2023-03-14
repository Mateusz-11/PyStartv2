from requests import get

url = 'https://wolnelektury.pl/api/books'
wanted_author = "Ajschylos"
# wanted_author = input("Książek jakiego autora szukasz? ")
response = get(url)
data = response.json()

for book in data:
    if book['author'] == wanted_author:
        print(f"Książka: {book['title']}")
