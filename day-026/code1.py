#List Comprehension - Create a new list from a previous list. 
#List, Range, String, Tuple are all known as sequences. 

# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n*2 for n in range(1, 5)]
# print(new_list)

# names = ["alex", "beth", "caroline", "eleanor", "freddie", "karan", "anjika"]
# new_names = [name.upper() for name in names if len(name) >= 5]
# print(new_names)

#Dictionary Comprehension
#new_dict = {new_key:new_value for item in list} - shortened syntax
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

# import random

# student_score = {
#     student:random.randint(1, 100) for student in names
# }

# passed_students = {
#     new_key:new_value for (key, value) in dictionary.items()
# }


#List Comprehension - Create a new list from a previous list. 
#List, Range, String, Tuple are all known as sequences. 

# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n*2 for n in range(1, 5)]
# print(new_list)

# names = ["alex", "beth", "caroline", "eleanor", "freddie", "karan", "anjika"]
# new_names = [name.upper() for name in names if len(name) >= 5]
# print(new_names)

#Dictionary Comprehension
#new_dict = {new_key:new_value for item in list} - shortened syntax
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

# import random

# student_score = {
#     student:random.randint(1, 100) for student in names
# }

# passed_students = {
#     new_key:new_value for (key, value) in dictionary.items()
# }


## Use dictionary comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
# sentence = "What is the Airspeed Velocity of an Unladen Swallow"

# result = {
#     word:len(word) for word in sentence.split()
# }

# print(result)


##Use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degree Celsius and converts it into degree Fahrenheits.

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_f = {
#    # new_key:new_value for (key,value) in dictionary.items()
#     day:(temp_c*9/5)+32 for (day, temp_c) in weather_c.items()
# }

# print(weather_f)



## How to iterate over a pandas dataframe

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through a dictionary
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a dataframe

for (key, value) in student_data_frame.items():
    print(value)

#iter rows allows us to loop through each of the rows of the dataframe
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)
