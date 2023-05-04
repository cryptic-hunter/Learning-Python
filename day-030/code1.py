#Error Handling in Python
#Try: - something that might cause an exception
#Except: - Do this if there is an exception encountered
#Else: - Do this if there were no exceptions encountered
#Finally: - Do this no matter what happens

try:
    file=open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["asdasd"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else: #executes when everything succeeds, whatever we're trying.
    content = file.read()
    print(content)
finally: #executes no matter what happens
    file.close()
    print("File was closed")



#Raising your own exceptions
#raise keyword allows us to raise our own exceptions.