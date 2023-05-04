#Python Dictionaries
#every dictionary has 2 parts of it, left side is the key and it has got an associated value.
#Dictionary Syntax : {key: value} each key-value pair is seperated using a ,
#Multiple items in a dictionary : {key:value,key:value,key:value}

programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected",
    "Function" : "A piece of code that you can easily call over and over again",
    "Loop" : "The action of doing something over and over again.",
}

#retrieve an item from dictionary
print(programming_dictionary["Loop"])

#Loop through a dictionary
for key in programming_dictionary:
   # print(key)
    print(programming_dictionary[key])