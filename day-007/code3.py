#Step 3

import random
word_list = ["aardvark", "baboon", "camel", "Hello", "World", "This", "Beautiful", "Anjikaran", "Manan", "Noname", "anonymous", "blackhat", "ardvark"]
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

f = "_"

while f in display:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            print(display)
        if f not in display:
            print("You Won")
            break