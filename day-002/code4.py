#type casting - we change a piece of data from one data type to another.
#print(70 + float("100.5")) -> 170.5 -> the string was converted into a float and float can be added up to int.


#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output would be 3+5 = 8
user_input = int(input("Enter any 2 digit number: "))
if user_input < 10 or user_input > 99:
    print("Please enter the input in a requested format.")
else:
    first_num = int(user_input/10)
    second_num = int(user_input%10)
    sum = first_num + second_num
    print("Sum of the digits of the numbers entered is: " + str(sum))