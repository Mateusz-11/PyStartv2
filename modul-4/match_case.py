answer = int(input("Text a month (like a number from 1 to 12): "))

## V1 - Match Case
#
# match answer:
#     case 1:
#         print("1 month it's january!")
#     case 2:
#         print("2 month it's fabruary!")
#     case 3:
#         print("3 month it's march!")
#     case 4:
#         print("4 month it's april!")
#     case 5:
#         print("5 month it's may!")
#     case 6:
#         print("6 month it's june!")
#     case 7:
#         print("7 month it's july!")
#     case 8:
#         print("8 month it's august!")
#     case 9:
#         print("9 month it's september!")
#     case 10:
#         print("10 month it's october!")
#     case 11:
#         print("11 month it's november!")
#     case 12:
#         print("12 month it's december!")
#     case _:
#         print("Bad value")

## V2 - Dictionaries

dict_of_months = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december",
}

if answer not in dict_of_months:
    print("Bad value")
else:
    print(f"{answer} month it's a {dict_of_months[answer]}")
