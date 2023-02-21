def choice_words(txt: str):
    result = set()
    txt_temp = txt.split()
    for i in txt_temp:
        if 4 < len(i) < 8:
            result.add(i)
    return result


print(choice_words("Ala ma kotka Jerzego piętnastego"))
