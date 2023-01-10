grades = (6, 5, 3, 2, 5, 2, 6, 1)

print('Grades of student: ', sorted(grades))

average = sum(grades) / len(grades)

print(f'Average of grades: {average}')

if average >= 4.75:
    print("It will be belt certificate")
else:
    print("Better not to ask")