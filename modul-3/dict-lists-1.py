workers = [
    {'id': 1,
     'job_title': 'junior_developer',
     'name': "John",
     'programming_language': ['python']
     },
    {'id': 2,
     'job_title': 'senior_developer',
     'name': "Mark",
     'programming_language': ['python', 'php']
     },
    {'id': 3,
     'job_title': 'stuff_developer',
     'name': "Alex",
     'programming_language': ['php', 'javascript', 'python']
     },
    {'id': 4,
     'job_title': 'junior_developer',
     'name': "Bart",
     'programming_language': ['javascript', 'php']
     },
    {'id': 5,
     'job_title': 'senior_developer',
     'name': "Carl",
     'programming_language': ['python', 'javascript']
     },
    {'id': 6,
     'job_title': 'junior_developer',
     'name': "Martha",
     'programming_language': ['php', 'javascript']
     }
]

statistics = {}
for worker in workers:
    # print(worker['name'])
    # print(worker['programming_language'])
    for programming_language in worker['programming_language']:
        # print(programming_language)
        if programming_language not in statistics:
            statistics[programming_language] = {
                'quantity': 0,
                'names': [],
            }

        statistics[programming_language]['quantity'] += 1
        statistics[programming_language]['names'].append(worker['name'])

print(statistics)
