#Scope in Programming
#
#enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Local Scope exists within functions. Any variable which is declared inside a function will have a local scope that will only by applicable to that function and those functions in which that function is being referenced.
#Global Scope exists in the complete code. A variable which is declared at the start of the code will be a global variable. it's value will remain same throughout the code unless it is modified by another declaration of the same variable. they are also available within the functions if there are no declarations with the same variable name within the function.
#Only Function will have a scope of its own, any type of loop will not have a scope and the variables declared inside them will still be considered as Global Variables.



############# KARAN'S SOLUTION #############
# from random import *
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# level = input("Choose a difficulty. Type 'easy' or 'hard'?: ")
# #attempts = 5

# random_choice = randint(1, 100)
# print(random_choice)
# if level == 'hard':
#     attempts = 5
#     while attempts > 0:
#         print(f"You have {attempts} attempts remaining to guess the number")
#         guess = int(input("Make a guess: "))
#         if guess == random_choice:
#             print("You guessed right!")
#             break
#         elif guess > random_choice:
#             print("That was high!")
#             attempts = attempts - 1
#         elif guess < random_choice:
#             print("You went low, can you increase it a bit?")
#             attempts = attempts - 1
#         else:
#             print("Something went wrong, Try again?")
#             attempts = attempts - 1
# elif level == 'easy':
#     attempts = 10
#     while attempts > 0:
#         print(f"You have {attempts} attempts remaining to guess the number")
#         guess = int(input("Make a guess: "))
#         if guess == random_choice:
#             print("You guessed right!")
#             break
#         elif guess > random_choice:
#             print("That was high!")
#             attempts = attempts - 1
#         elif guess < random_choice:
#             print("You went low, can you increase it a bit?")
#             attempts = attempts - 1
#         else:
#             print("Something went wrong, Try again?")
#             attempts = attempts - 1
# else:
#     print("Something went wrong!!")
############# KARAN'S SOLUTION ENDS#############














############# ANGELA'S SOLUTION #############
#Choosing a random number between 1 and 100
from random import *
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answers.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    elif guess == answer:
        print(f"You Got it, the correct answer was {answer}")

#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)

    turns = set_difficulty()
    
    guess = 0

    while guess != answer:
    #Let the user guess a number
        print(f"You have {turns} attempts remaining to guess the correct answer")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses!")
            return 

game()
############# ANGELA'S SOLUTION END#############