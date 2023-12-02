from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list of questions
question_list = []

# Loop through questions and assign them to a list
for question in question_data:
    # Get question text from dictionary
    question_text = question["text"]
    # Get question answer from dictionary
    question_answer = question["answer"]
    # Create a new object from the information received from dictionary
    new_question = Question(question_text, question_answer)
    # Append the new object to the question list
    question_list.append(new_question)

quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()
    
print("All questions completed!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")