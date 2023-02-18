first_txt = "pythOnnnaa"
second_txt = "nnaathypOn"

first_txt_sort = sorted(first_txt.lower())
second_txt_sort = sorted(second_txt.lower())

print("They are anagrams") if first_txt_sort == second_txt_sort else print("They aren't anagrams.")
