from json import load, dump

new_author = "Witold Gombrowicz"
new_title = "Ferdydurke"

with open('book.json') as file:
    books = load(file)

for book in books:
    print(book.get('title'))
    print(book.get('author'))
    print('---' * 10)

with open('book.json', 'w') as file:
    books.append({
        'title': new_title,
        'author': new_author,
    })
    dump(books, file)

[
  {
    "type": "Opłaty",
    "amount": 1000
  }
]