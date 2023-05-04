#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel", "Hello", "World", "This", "Beautiful", "Anjikaran", "Manan", "Noname", "anonymous", "blackhat", "ardvark"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"This is {word_length} letter word.")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter.lower() == guess.lower():
            display[position] = letter
            print(stages[lives])

    if guess.lower() not in chosen_word:
        if lives > 0:
            lives = lives - 1
            print(stages[lives])
        else:
            end_of_game=True
            print("You Lose")
            print(stages[lives])
            
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(stages[lives])