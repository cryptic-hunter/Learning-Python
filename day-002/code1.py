#TIP CALCULATOR
import math
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? (in USD) : "))
num_people = float(input("How many people need to split up the bill? : "))
tip = float(input("What percentage tip would you like to give? : "))
if bill > 0 and num_people > 0 and tip > 0:
    each_person_share = bill/num_people
    tip_amount = tip/100*bill
    actual_tip = tip_amount/num_people
    bill_by_each_person = each_person_share + actual_tip
    #rounded_bill_each_person = round(bill_by_each_person, 2)
    rounded_bill_each_person = "{:.2f}".format(bill_by_each_person)
    print(f"OUTPUT : Each person should pay ${rounded_bill_each_person}")
else:
    print("Sorry, you cannot proceed")