choice = "yes"
names_dict = {}
while choice != "no":
    new_name = input("What name do you want to add? ")
    if new_name in names_dict.keys():
        names_dict[new_name] += 1
        print("Updated a name!")
    else:
        names_dict[new_name] = 1
        print("Saved a new name")
    print("---" * 10)
    choice = input("Do you want add new name? (yes / no): ")

for name, occurances in names_dict.items():
    print(name, occurances)

unique_names = []
for _ in set(names_dict):
    unique_names.append(_)

print(sorted(unique_names))
