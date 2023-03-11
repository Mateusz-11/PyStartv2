passed = []

with open('students.txt') as file:
    for line in file:
        first_name, last_name, note = line.strip().split(';')
        print(first_name, last_name, note)
# if note == '2':
#     passed.append({"first_name": first_name, "last_name": last_name, "note": note})


with open('output.txt', encoding='utf8', mode='w') as file:
    for student in passed:
        file.write(f'{student.get("first_name")};{student.get("last_name")};{student.get("note")}\n')
