#conditional statements, logical operators, code blocks and scope


#BMI Calculator 2.0
#Write a program that interprets the BMI based on the user's height and weight.
#If BMI under 18.5 - they are underweight
#Over 18.5 and under 25 - they have a normal weight
#over 25 and below 30 - they are overweight
#over 30 and below 35 - they are obese
# above 35 - they are clinically obese
#BMI = weight(kg)/height*height(m)

height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))

bmi = weight/(height**2)

if(bmi<=18.5):
    print("Hey, your BMI is " + str(bmi) + " and you are underwight")
    #print(f"Your bmi is {bmi}, you are underweight")
elif(bmi>18.5 and bmi <= 25):
    print("Your BMI is " + str(bmi) + " and you have a normal weight")
elif(bmi>25 and bmi <= 30):
    print("Your BMI is " + str(bmi) + " and you are overweight")
elif(bmi > 30 and bmi <= 35):
    print("Hey, your BMI is " + str(bmi) + " and you are overweight")
elif(bmi>35):
    print("Hey, your BMI is " + str(bmi) + " and I would recommend you to please go and visit a doctor, you are clinically obese")
else:
    print("Please enter a valid input")