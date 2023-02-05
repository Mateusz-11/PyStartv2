dict_ang_pl = {"dog": "pies", "cat": "kot", "snake": "wąż", "tiger": "tygrys"}
choice = input("Wybierz język (ang/pl): ")

if choice == "ang":
    ask_word = input("Jakie słowo przetłumaczyć na polski? ")
    for k, v in dict_ang_pl:
        if ask_word in dict_ang_pl.keys() or ask_word in dict_ang_pl.values():
            print(dict_ang_pl.get(ask_word))
        else:
            print("Nie ma takiego słowa w słowniku.")

