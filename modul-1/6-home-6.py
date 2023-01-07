from math import sqrt, pi

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

# Middle of line
xmid = (x1 + x2) / 2
ymid = (y1 + y2) / 2

print(f"Middle point is: {xmid}, {ymid}")

# Lenght of line
lenght = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Lenght od line is {lenght}")

radius = lenght / 2

# Field of circle
field = pi * radius ** 2
print(f"Filed equal: {field}")

# Circumference of rectangle
len_rect_1 = sqrt((x1 - x2) ** 2 + (y2 - y2) ** 2)
len_rect_2 = sqrt((x1 - x1) ** 2 + (y1 - y2) ** 2)
print(f'Field od rectangle is: {len_rect_1 * len_rect_2}')
print(f'Circumference of rectangle = {len_rect_1 * 2 + len_rect_2 * 2}')
