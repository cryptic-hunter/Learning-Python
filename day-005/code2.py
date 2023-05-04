#Calculate the average height of students from the given list of heights.
import math
student_height = input("Enter the height of the students(in cms) seperated by a space: ").split()
total = 0
# for i in range(0, len(student_height)):
#     total = total + int(student_height[i])
# #print("Sum of all elements in given list: " + str(total))
# #print("Number of elements in a given list: " + str(len(student_height)))
# list_length = len(student_height)
# average_height = total/list_length
# decimal_student_height = round(average_height, 2)
# print("Average height is " + str(decimal_student_height) + "cms")
count = 0
for element in student_height:
    count += 1
#print(count)
for i in range(0, count):
    total = total + int(student_height[i])
#print(total)
average_height = total/count
decimal_student_height = round(average_height, 2)
print("Average height is " + str(decimal_student_height) + "cms")