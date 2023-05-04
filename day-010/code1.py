#Making a calculator App using functions

#Difference between print and return
#Print statement is used when the output has to be displayed in a human readable format.
#return is used to stop the program execution and return the result to the point where the function was declared. If the value of the output has to be sent from one place to another, return statement is used.

import math

def add(first_number, second_number):
    sum = first_number + second_number
    print(f"{first_number} + {second_number} = {sum}")
    return sum
def subtract(first_number, second_number):
    difference = first_number - second_number
    print(f"{first_number} - {second_number} = {difference}")
    return difference

def multiply(first_number, second_number):
    product = first_number * second_number
    print(f"{first_number} * {second_number} = {product}")
    return product

def division(first_number, second_number):
    quotient = first_number / second_number
    print(f"{first_number} / {second_number} = {quotient}")
    return quotient


first_number = float(input("Enter the first number: "))
should_continue = True

while should_continue:
    second_number = float(input("Enter the next number: "))
    math_operation = input("Enter the mathematical operation that you want to perform [add/subtract/multiply/divide] : ")

    if math_operation == "add":
        answer = add(first_number,second_number)
    elif math_operation == "subtract":
        answer = subtract(first_number, second_number)
    elif math_operation == "multiply":
        answer = multiply(first_number, second_number)
    elif math_operation == "divide":
        answer = division(first_number, second_number)
    else:
        print("please enter a valid operation between \"add\", \"subtract\", \"multiply\", and \"divide\" ")
    if input(f"Type \"Y\" to continue calculating with {answer} or type \"N\" to exit: ") == "Y":
        first_number = answer
    else:
        print(f"Your final calculation result is {answer}")
        should_continue = False


