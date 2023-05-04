#Higher-Lower Game

#Parse the dictionary and ask the user to compare a person with another persom from the dictionary, print their country and occupation along with it.
#compare the user choices by making the calculation
#if the guess is correct, then the person in the second choice [B] becomes the user with the first choice [A] and now, we choose another user, [B], ask the user which of them have more followers again.
# if the user is wrong, close the game and show them the user score.







from data import data
import random

score = 0
game_continue = True
account_b = random.choice(data)

while game_continue:

    def format_data(account):
        """Take the account data and returns a printable format"""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def check_answer(guess, a_followers, b_followers):
        """Takes the user guess and follower counts and returns if they got it right."""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if the user's guess is correct
    ##Get follower count of each account
    ## Use if statement to check if the user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess

    if is_correct:
        score += 1
        print(f"You're right!, Current score is {score}")
    else:
        game_continue = False
        print(f"Sorry, you're wrong!, your final score is {score}")