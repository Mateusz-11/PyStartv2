dict_ang_pl = {
    'dog': 'pies',
    'cat': 'kot',
    'snake': 'wąż',
    'tiger': 'tygrys'
}

choice = input("Wybierz język (ang / pl): ")

if choice not in ['ang', 'pl']:
    print("Takie tłumaczenie jest niedostępne")
    quit()

if choice == "ang":
    ask_word = input("Jakie słowo przetłumaczyć na polski? ")
    for k, v in dict_ang_pl.items():
        if k == ask_word:
            print(f"Odpowiedź to: {v}")
            break
    else:
        print("Nie ma takiego słowa w słowniku.")
        quit()
elif choice == "pl":
    ask_word = input("Jakie słowo przetłumaczyć na angielski? ")
    for k, v in dict_ang_pl.items():
        if v == ask_word:
            print(f"Odpowiedź to: {k}")
            break
    else:
        print("Nie ma takiego słowa w słowniku.")
        quit()
else:
    print("Takie tłumaczenie jest niedostępne")

