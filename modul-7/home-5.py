correct_lines = []

with open('balagan.txt') as file:
    for line in file:
        if 'Javascript' not in line:
            line = line.strip().replace('Java', 'Python')

        correct_lines.append(line.strip())

with open('balagan.txt', 'w', encoding='utf8') as file:
    file.write('\n'.join(correct_lines))