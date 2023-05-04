#Enter the list of student scores seperated by a space and find the highest marks of the student
student_marks = input("Please enter the marks of the students seperated by a space: ").split()
highest_marks = student_marks[0]

for marks in student_marks:
    if int(marks) > int(highest_marks):
        highest_marks = marks
print("Highest Marks are: " + highest_marks)