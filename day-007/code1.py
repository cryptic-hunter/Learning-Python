#Hangman Project
#Game - guess a word and for every wrong letter submitted will end up taking a life away from a little man, and the longer it takes you to guess the correct word, the more you put your player in danger.
import random

word_list = ["Hello", "World", "This", "Beautiful", "Anjikaran", "Manan", "Noname", "anonymous", "blackhat","ardvark"]
chosen_word = random.choice(word_list).lower()
print(chosen_word)
guess = input("Guess an alphabet to save your player: ").lower()
chosen_word_list = list(chosen_word)
length_chosen_word_list = len(chosen_word)

for letter in chosen_word_list:
    if guess == letter:
        print("Guess : " + guess + " chosen word character : " + letter)
        print("Congrats! You guessed one of the correct letters.")
        #print("Right")
    else:
        #print("Wrong")
        print("Guess : " + guess + " chosen word character : " + letter)
        print("Oops! you want to try again?")