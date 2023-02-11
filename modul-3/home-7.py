from random import shuffle, choice

list_of_words = ['python', 'javascript', 'java']

right_word = choice(list_of_words)
word_to_guess = list(right_word)
shuffle(word_to_guess)

print('---' * 10)

print(f'Word to guess: {"".join(word_to_guess)}')
print("Do you know what is the word?")

for _ in range(3):
    user_answer = input("Write your answer: ")
    if user_answer == right_word:
        print(f"Congratualtions! You got it right {_+1} time!")
        break
    else:
        print("Sorry. Try again.")