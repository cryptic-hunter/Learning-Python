#based on a user's order, print their final bill for pizza
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
small_pepperoni = 2
medium_pepperoni = 3
large_pepperoni = 3
extra_cheese_price = 1

if(size == "S"):
    if(add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
            bill = small_pizza + small_pepperoni + extra_cheese_price
            print("Your final bill is: $" + str(bill))
        else:
            bill = small_pizza + small_pepperoni
            print("Your final bill is: $" + str(bill))
    else:
        bill = small_pizza
        print("Your final bill is: $" + str(bill))
if(size == "M"):
    if(add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
            bill = medium_pizza + medium_pepperoni + extra_cheese_price
            print("Your final bill is: $" + str(bill))
        else:
            bill = medium_pizza + medium_pepperoni
            print("Your final bill is: $" + str(bill))
    else:
        bill = medium_pizza
        print("Your final bill is: $" + str(bill))
if(size == "L"):
    if(add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
            bill = large_pizza + medium_pepperoni + extra_cheese_price
            print("Your final bill is: $" + str(bill))
        else:
            bill = large_pizza + medium_pepperoni
            print("Your final bill is: $" + str(bill))
    else:
        bill = large_pizza
        print("Your final bill is: $" + str(bill))