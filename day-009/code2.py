student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_grades = {}

student_name = list(student_scores.keys())
student_score = list(student_scores.values())

for i in student_score:
    if i > 90 and i < 101:
        index = student_score.index(i)
        student_score[index] = "Outstanding"
    elif i > 80 and i < 91:
        index = student_score.index(i)
        student_score[index] = "Exceeds Expectations"
    elif i > 70 and i < 81:
        index = student_score.index(i)
        student_score[index] = "Acceptable"
    elif i < 71 and i > 0:
        index = student_score.index(i)
        student_score[index] = "Failed"

for name in student_name:
    for score in student_score:
        student_grades[name] = score
        student_score.remove(score)
        break

print(student_grades)


#ANGELA's SOLUTION
#for student in student_scores: // apparently, in a for loop looping through the dictionary, 
# the item that gets called out automatically is the key of the item
#   score = student_scores[student] // assigning the value of the key to the variable
#   if score > 90:
#       student_grades[student] = "Outstanding"
#   elif score > 80:
#       student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#       student_grades[student] = "Acceptable"
#   else:
#       student_grades[student] = "Failed"