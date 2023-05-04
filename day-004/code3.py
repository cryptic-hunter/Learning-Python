#Day 4 - Randomisation and Python Lists
#Rock Paper Scissors Game
import random

user_input = input("Please enter your input (rock/paper/scissors): ")

choices = ["rock","paper","scissors"]
computer = random.choice(choices)

if(user_input == "rock"):
    if(computer == "rock"):
        print("It's a draw, play again!!")
    elif(computer == "paper"):
        print("Computer Wins!!")
    elif(computer == "scissors"):
        print("User Wins!!")
    else:
        print("Please enter a valid input")
elif(user_input == "paper"):
    if(computer == "rock"):
        print("User Wins!!")
    elif(computer == "paper"):
        print("It's a draw, play again!!")
    elif(computer == "scissors"):
        print("Computer Wins!!")
    else:
        print("Please enter a valid input")
elif(user_input == "scissors"):
    if(computer == "rock"):
        print("User Wins!!")
    elif(computer == "paper"):
        print("Computer Wins!!")
    elif(computer == "scissors"):
        print("It's a draw, play again!!")
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")