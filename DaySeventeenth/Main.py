from question import Question
from data import question_data
from Question_Brain import QuizzBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)
while quizz.still_has_question():
    quizz.next_question()
print(f"You completed the quizz,\n you got {quizz.score} / {len(quizz.question_list)}")
