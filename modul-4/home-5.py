from statistics import mean

dict_temp_city = {}

while True:
    choice = int(input("What do you do? 1- add new datas / 2 - exit program >> "))
    if choice == 2:
        break
    elif choice == 1:
        city = input("City: ")
        temperature = float(input("Temperature: "))
        dict_temp_city[city] = temperature
    print("---" * 10)

list_temp = []
for k, v in dict_temp_city.items():
    list_temp.append(v)

avg_temp = mean(list_temp)
print(f"Avarage temperature: {round(avg_temp, 2)}  Cels grades")

highest_temp = []
lowest_temp = []

for city, temp in dict_temp_city.items():
    if temp == max(dict_temp_city.values()):
        highest_temp.append(city)
    if temp == min(dict_temp_city.values()):
        lowest_temp.append(city)

print(f"Highest temperature: {highest_temp}")
print(f"Lowest temperature: {lowest_temp}")
