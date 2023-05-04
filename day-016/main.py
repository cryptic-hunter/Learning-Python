from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)












































# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()



#procedural programming - style of programming where we set up procedures or functions that do particular things and one procedure leads to another procedure. Computer works from top to bottom and then jumping out into the function as needed.
#Object Oriented Programming - Makes use of objects, which are a kind of real world objects and several models are created for a particular project.
#When modelling a real world object, we need to think about what it has and what it does. It is known as attributes and models. Attributes are basically variables that are attached to a particular object, methods are functions that a particular modelled object can do. Class is responsible for generating objects. A python class is like an outline for creating a new object. An object can be anything that you wish to manipulate or change while working through the code.   
#from a class, we can generate as many objects as we want.
#car = CarBlueprint() - car is the object, CarBlueprint() is the class
#give the object a name, which can be anything that you want, set it equal to the name of the class with the parentheses, in the same way as it activates the function, it activates the construction of the object from the blueprint.
#A function tied to an object is known as method.

# import turtle
# timmy = turtle.Turtle()

# OR 

# from turtle import Turtle
# timmy = Turtle()
# from prettytable import PrettyTable
# #challenge : create a prettytable object and save it to a variable called table.
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column( "Type", ["Electric", "Water", "Fire"])
# print(table)

