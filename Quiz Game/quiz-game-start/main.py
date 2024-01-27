from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

"""Creating list to hold questions"""
question_bank = []

for question in question_data:
    """Filling in question bank with list of questions"""
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

"""Creating object for question"""
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    """Calling method from QuizBrain class"""
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")

