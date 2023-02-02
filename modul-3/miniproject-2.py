from math import ceil

walls_nr = int(input("Ile jest ścian do pomalowania? "))
print("Jeśli chcesz przyjąć poprzednią wysokość wciśnij enter.")

height_prev = 3
areas_of_wall = 0
for i in range(1, walls_nr + 1):
    width = float(input(f"Podaj szerokość {i} ściany w metrach: "))
    height = input(f"Podaj wysokość {i} ściany w metrach: ")

    if height == "":
        height = height_prev
    else:
        height = float(height)
        height_prev = height

    areas_of_wall += width * height
    # print(areas_of_wall)

paint_primer_consumption = 5
paint_consumption = 13

layer_of_prime_paint = int(input("Ilość warstw gruntu: "))
layer_of_paint = int(input("Ilość warstw farby: "))

amount_paint_primer = ceil((areas_of_wall * layer_of_prime_paint) / 5)
amount_paint = ceil((areas_of_wall * layer_of_paint) / 13)

print(f"Powierzchnia do pomalowania wynosi {round(areas_of_wall, 1)} m2")
print(f"Potrzebujesz {amount_paint_primer} litrów gruntu")
print(f"Potrzebujesz {amount_paint} litrów farby")
