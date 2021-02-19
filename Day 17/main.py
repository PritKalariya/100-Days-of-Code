from question_model import Question
from data import  question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:

    # Loading the question & answers
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Creating the questions object
    new_question = Question(question_text, question_answer)

    # Append the question to the list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congrats! You have completed the quiz.")
print(f"You Final score is: {quiz.score}/{quiz.question_number}. ")