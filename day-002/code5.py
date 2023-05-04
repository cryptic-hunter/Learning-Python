#Write a program to calculate the BMI of a person based on their weight and height depending on the user input.
#BMI = weight(kg)/(height)^2
height = float(input("Please enter your height in m: "))
weight = float(input("Please enter your weight in kg: "))
bmi = weight/(height*height)
bmi1 = int(bmi)
print("Your BMI is: " + str(bmi1))