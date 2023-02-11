countries = []
for _ in range(3):
    country_record = {}
    country = input("Write the country: ")
    capital = input("Write the capital od country: ")
    language = input("Write the official language: ")
    country_record['country'] = country
    country_record['capital'] = capital
    country_record['language'] = language
    print(country_record)
    countries.append(country_record)
    print(countries)

for country in countries:
    print(country['country'], country['capital'], country['language'])
    print("---" * 10)

for country in countries:
    for column, value in country.items():
        print(f'{column}: {value}')
    print("---" * 10)

