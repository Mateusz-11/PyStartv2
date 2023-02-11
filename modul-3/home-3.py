movies = [
    {
        'name': 'movie1',
        'rezyser': 'Steven',
        'rok produkcji': 2000,
    },
    {
        'name': 'movie2',
        'rezyser': 'August',
        'rok produkcji': 1998,
    },
    {
        'name': 'movie3',
        'rezyser': 'Mongomery',
        'rok produkcji': 1995,
    },
    {
        'name': 'movie4',
        'rezyser': 'Robert',
        'rok produkcji': 1990,
    },
    {
        'name': 'movie5',
        'rezyser': 'Steven',
        'rok produkcji': 1980,
    }
]

print(movies)

for movie in movies:
    if movie['rezyser'] == "Steven":
        movies.pop(movies.index(movie))
        # print(movies.index(movie))

print(movies)
