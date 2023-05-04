import random

word_list = ["aardvark", "baboon", "camel", "Hello", "World", "This", "Beautiful", "Anjikaran", "Manan", "Noname", "anonymous", "blackhat", "ardvark"]

chosen_word = random.choice(word_list)

chosen_word_list = chosen_word.split()

print(chosen_word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

length_chosen_word = len(chosen_word)

displayed_list = []

for i in range(0,length_chosen_word):
    f = "_"
    displayed_list.append(f)

guess = input("Guess a letter: ").lower()

i = 0

for letter in chosen_word:
    if letter.lower() == guess.lower():
        displayed_list[i] = letter.lower()
    i = i+1

print(displayed_list)