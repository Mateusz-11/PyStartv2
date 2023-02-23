def reverse_text(txt: str) -> str:
    new_txt = txt.split(' ')
    result = []
    for i in new_txt:
        result.append(i[::-1])
    return " ".join(result)


print(reverse_text("programuję w pythonie"))
