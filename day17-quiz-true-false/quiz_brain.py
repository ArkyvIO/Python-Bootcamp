import html

class QuizBrain:
    
    # Initialize base object, has question num, list and score
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    # Get next question in object list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        decoded_question_text = html.unescape(current_question.text)
        user_answer = input(f"Question {self.question_number}: {decoded_question_text} --- True or False: ")
        # User input validation, should always be t or f for first letter of answer
        while True:
            if user_answer[0].lower() == "t" or user_answer[0].lower() == "f":
                break
            else:
                user_answer = input("That input was not recognized, please try again: ")
        self.check_answer(user_answer, current_question.answer)
        
    # Check if the list still has questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    # Check if the answer was correct or incorrect.
    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            self.score += 1
            print(f"Correct! Your score is now {self.score}/{self.question_number}")
        else:
            print(f"Incorrect! Your score is now {self.score}/{self.question_number}")
        print("\n")
