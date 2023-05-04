#PYTHON LISTS
#list is a data structure. fruits = [item1, item2] - any data type and mixed data type.
#Write a python program to take a list of names as an input and then determine that who will pay the bills
from random import randrange
names = input("Enter all the names of the members seperated by a ',': ")
names_split = names.split(",")
random_name = randrange(len(names_split))
print(names_split[random_name] + " will pay the bill for today")