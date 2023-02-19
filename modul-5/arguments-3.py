#  V1
def repeat_txt(txt, delimiter=',', repeat=1):
    txt_result = (txt + delimiter) * repeat
    return txt_result

#  V2
def repeat_txt2(txt, delimiter=',', repeat=1):
    output = []
    for _ in range(repeat):
        output.append(txt)
    return delimiter.join(output)

print(repeat_txt2("Ala ma kota"))
print(repeat_txt2("Python", delimiter=";", repeat=3))
