from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")














































# #creating a class
# #class Car:

# class User:
#     def __init__(self, user_id, username):
#         #we initialize or create the starting values of our attributes. This init function is going to be called everytime we create an object from this class.
#         #self keyword in the argument to the init function refers to the actual object that is being created or being initialized. 
#         self.id = user_id
#         self.username = username

# user_1 = User("001", "some name")
# print(user_1.id)

# #constructor - part of the blueprint that allows us to specify what should happen when our object is being constructed. Also known as initializing an object.

