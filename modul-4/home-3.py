PASSWORD = "Python2023"

while True:
    try:
        user_answer = input("Text the password or 'end' to close the program: ")
    except ValueError:
        print("Wrong answer")
    if user_answer == "end":
        exit()
    if PASSWORD == user_answer:
        print("Correct password!")
        break
    else:
        print("Bad answer. Try again.")
        print("---" * 10)


