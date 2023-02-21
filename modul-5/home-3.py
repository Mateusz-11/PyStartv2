def choice_words(txt: str, min_length: int = 4, max_length: int = 8) -> set:
    result = set()
    txt_temp = txt.split()
    for i in txt_temp:
        if min_length < len(i) < max_length:
            result.add(i)
    return result


print(choice_words("Ala ma kotka Jerzego piętnastego", 4, 8))
