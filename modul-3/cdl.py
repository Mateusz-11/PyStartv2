bands = ['Led Zepplin', 'Queen', 'ACDC']

bands[0] = "The Beatles"
print(bands)

del bands[0]
print(bands)

bands.append("Led Zepplin")
bands.append("The Beatles")
print(bands)

if "Queen" in bands:
    print("Queen jest!")

if "Kult" in bands:
    print("Kult jest!")
else:
    print("Kultu nie ma :(")

bands.remove("The Beatles")
print(bands)
