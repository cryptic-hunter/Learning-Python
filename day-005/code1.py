#Build a password generator. Take input from the user for the total length of the password and then ask for the number of digits and the special character that the user wants in their passwords. Generate a secure password according to the user's choice inputs.
import random
print("Welcome to the PyPassword Generator")
num_capital_letters = int(input("How many Capital Letters would you like in your password? : "))
num_letters = int(input("How many Letters would you like in your password? : "))
num_symbols = int(input("How many Symbols would you like in your password? : "))
num_numbers = int(input("How many Numbers would you like in your password? : "))

total_length = num_letters + num_symbols + num_numbers + num_capital_letters
if(total_length < 10):
    print("You are about to generate a relatively insecure password. Please proceed at your own risk.")
else:
    print("You're 1337, this will be a safe password unless some dedicated hacker is at your door.")

capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[','{','}',']','"',';',':','<',',','>','.','?','/']
numbers = ['1','2','3','4','5','6','7','8','9']

random_capital = random.choices(capital_letters, k=num_capital_letters)
random_letters = random.choices(letters, k=num_letters)
random_symbols = random.choices(symbols, k=num_symbols)
random_numbers = random.choices(numbers, k=num_numbers)
random1 = random_capital + random_letters + random_symbols + random_numbers

str1 = ""
str2 = str1.join(random1)

random1 = ''.join(random.sample(str2,len(str2)))
if(total_length > 9):
    print("Your Secure Password is : " + random1)
else:
    print("Your not so secure password is : " + random1)