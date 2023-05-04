############DEBUGGING#####################

# # Describe Problem
# Describe the problem whatever is preventing you from getting the actual expected output from the code that has been written.
# def my_function():
#   for i in range(1, 20):
#       if i == 20:
#         print("You got it")
# my_function()

# # Reproduce the Bug
# Reproduce the error on when does the error trigger and which line triggers the error. Which is the condition/function that is being used which triggers that particular error.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# #Look at each line of code and evaluate what it is supposed to do.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# #Look and fix the errors that are being thrown by the application/console/text editor, Look if the output you are getting is the desired output that you expected out of the code
# age = int(input("How old are you?: "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# # Use print statements to check if all the variables are getting the values which they are supposed to get
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


# number = int(input("Which number do you want to check? : "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")


