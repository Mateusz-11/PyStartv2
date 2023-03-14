from requests import get

# V1
# url = 'https://danepubliczne.imgw.pl/api/data/synop/station/kielce'
# parameters = ['temperatura', 'cisnienie']
# response = get(url)
# data = response.json()
# for k, v in data.items():
#     if k in parameters:
#         print(k, v)

city = ['Kielce']
# V2
url = 'https://danepubliczne.imgw.pl/api/data/synop'
parameters = ['temperatura', 'cisnienie']
response = get(url)
data = response.json()
for record in data:
    if record['stacja'] == 'Gdańsk' or record['stacja'] == 'Warszawa':
        print(f"Pogoda dla miasta: {record['stacja']}")
        print(f"Ciśnienie: {record['cisnienie']}")
        print(f"Temperatura: {record['temperatura']}")
