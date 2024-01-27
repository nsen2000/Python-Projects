class QuizBrain:
    """Class which will calculate each question to be asked"""
    def __init__(self, q_list):
        """List of attributes"""
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Method to check if all questions have been asked"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Method to iterate through questions and ask user for answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, answer):
        """Checking if user answer is correct/ not correct and printing score"""
        if answer.lower() == user_input.lower():
            self.score += 1
            print("That's correct!")
            print(f"The correct answer is {answer}.")
            print(f"Score: {self.score}/{self.question_number}")
        else:

            print("That's wrong!")
            print(f"The correct answer is {answer}.")
            print(f"Score: {self.score}/{self.question_number}")




