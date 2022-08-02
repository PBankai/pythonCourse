# class User:
#     def __init__(self, user_id, username):
#         print("Object created")
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User(1233, "Pedro")
# print(user_1.username)
from question import Question
from data import question_data
from Question_Brain import QuizzBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)
while quizz.still_has_question():
    quizz.next_question()
print(f"You completed the quizz,\n you got {quizz.score} / {len(quizz.question_list)}")
