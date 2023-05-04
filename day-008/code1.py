#Task:
#Create a function called greet() Write 3 print statements inside the function and call the greet() function and run the code.
name = input("Please enter your name: ")
location = input("Please enter your location: ")
def greet_with_name(name, location):
    print(f"Hello {name}, Are you from {location}")
    print(f"{name}, Hope you and your family is doing good in {location}")

greet_with_name("Jack", "Jones")

#Positional Arguments : greet_with_name(name, location)
#Keyword Arguments : greet_with_name(name="karan", location="karnal")