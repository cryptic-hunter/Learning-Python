#game of blackjack
#The user will be drawn 2 cards automatically by the card dealer and the first card of the computer will be displayed.
#If the user wants to get another card, they can hit y or else, they can hit n to finish the game and draw the cards.
#if the user hits n, the game ends, the computer will be drawn one card and the sum of the user's cards and the computer's cards will be displayed, the one with the higher sum wins.

#Rules of the game
#Goal: Add up the cards to the largest number without going over 21.
# If it goes over 21, you lose
# all cards from 2 to 10 are counted on their face values
# K Q J each count as 10
# A : Ace can either count as 1 or 11, depending if you're over 21 or under 21.

#use random function to draw a card for the user and the computer and show the computer's card and the user's card both.
#Use another random function and this time also, draw a card for the user and the computer but don't show the computer card info but show the user's card info.
#Ask the user if they want to draw any more cards,
#if yes, draw a card and calculate the result. If the card contains "Ace", ask the user if they want the value to be counted as 1 or 11. then calculate the sum and If the result is over 21, the user loses the game
#if no, calculate the result and store it in a variable, Calculate the card sum that computer has. If the card contains "Ace", then check if the result difference between 21 and the first card is greater than or equal to 11, if it is, put the value of Ace as 11 and if it's not, then put the value of Ace as 1. then calculate the sum and If the result is over 21, the user loses the game
#Display both the card results, whoever has the card sum closest to 21, wins the game.
import random
####BlackJack Game Rules####
#The Deck is unlimited in size
#There are no Jokers
#The Jack/King/Queen, all count as 10
#The Ace can count as 11 or 1
#The cards in the list have equal probability of being drawn
#Cards are not removed from the deck as they are drawn



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card
# deal_card()
# print(random_card)

#######Karan's Approach to draw 2 random cards out of the deck and calculate the sum#######
# user_cards = random.sample(cards,2)
# computer_cards = random.sample(cards,2)
# print(f"{user_cards[0]} + {user_cards[1]} = {user_cards[0] + user_cards[1]}")
# print(f"{computer_cards[0]} + {computer_cards[1]} = {computer_cards[0] + computer_cards[1]}")

#######Angela's Solution#######
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    #if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It is a draw"
    elif computer_score == 0:
        return "User has lost and opponent has a blackjack"
    elif user_score == 0:
        return "User wins with a blackjack"
    elif user_score > 21:
        return "You got over 21, user loses"
    elif computer_score > 21:
        return "Computer got over 21, computer loses"
    elif user_score > computer_score:
        return "User Wins"
    elif user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    else:
        return "Computer Wins."
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        ## += is a shorthand for writing the extend function. Extend function extends a list by appending elements from the iterable.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want another card to be drawn(Y/N): ")
            if user_should_deal == "Y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and final score is {user_score}")
    print(f"Computer's final hand is {computer_cards} and final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? (Y/N)") == "Y":
    play_game()