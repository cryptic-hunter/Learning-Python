#Functions with Outputs

# def format_name():
#     f_name = input("Enter the first name: ").capitalize()
#     l_name = input("Enter the last name: ").capitalize()
#     print(f_name)
#     print(l_name)

# format_name()

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))