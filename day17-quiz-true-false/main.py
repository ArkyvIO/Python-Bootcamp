from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

# Create an empty list of questions
question_list = []

# API endpoint
api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"

# Make a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    api_data = response.json()

    # Extract the list of questions and answers from the API response
    results = api_data.get('results', [])

    # Convert API data into the desired format (similar to question_data)
    for result in results:
        question_text = result.get('question', '')
        correct_answer = result.get('correct_answer', '')
        # Creating the dictionary for each question
        new_question = Question(question_text, correct_answer)  # Use the Question class
        # Append the new question to the question_list
        question_list.append(new_question)

    # Replace the question_data with the API retrieved questions
    print(question_list)

else:
    print("Failed to retrieve data from the API, using backup list.")
    # Use question_data as a backup if the API call fails
    for item in question_data:
        new_question = Question(item["text"], item["answer"])  # Use the Question class
        question_list.append(new_question)

quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()
    
print("All questions completed!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")