# Start the program by taking the input of the user's name and the auction price.
# Create an empty dictionary
# Store the user's name and the auction price in the dictionary within the dictionary
# Every new entry will be a new key value pair addition within the existing dictionary of the user's name and auction price.
# Compare the auction value of all the existing users in the dictionary
# print the username and the auction value of the highest auction value entry.

#-> Working Solution


user_bids = {}

name = input("Please enter your name? : ")
price = input("Please enter the auction price that you want to bid for? : $")
more_users = input("Please let me know if there are any more bidders? (y/n) : ")
user_bids[name] = price

while more_users == "y":
    name = input("Please enter your name? : ")
    price = input("Please enter the auction price that you want to bid for? : $")
    more_users = input("Please let me know if there are more bidders? (y/n) : ")
    user_bids[name] = price
    if more_users == "n":
        break
    continue

#print(user_bids)

max_bid_price = max(user_bids.values())
#print(max_bid_price)

max_bid_name = max(user_bids, key=user_bids.get)
#print(max_bid_name)

print(f"Congratulations, We have the result, The maximum bid of ${max_bid_price} was made by {max_bid_name}")

# -> Working Solution ends

# # -> Angela's Solution
# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#     name = input("What is your name? ")
#     price = int(input("What is your bid? $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? [yes/no] : ")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#        #Clear the screen
#        continue

# # -> Angela's Solution Ends