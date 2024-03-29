# Day 17: Object-Oriented True/False Quiz Application with Open Trivia API Integration

## Project Description

The Day 17 project aims to develop a true/false quiz application in Python, emphasizing Object-Oriented Programming (OOP) principles. This project will explore the benefits of OOP by implementing a quiz program using classes, attributes, methods, and class constructors. To acquire quiz questions, the application will utilize the Open Trivia Database API, fetching new questions for the quiz.

## Key Concepts Applied

- **Object-Oriented Programming (OOP):** Creation of classes and objects to manage quiz questions, answers, and scoring within the application.
- **Class Creation:** Development of a 'Question' class with attributes, a class constructor (**init**()), and methods for managing quiz-related functionalities.
- **API Integration:** Use of the Open Trivia Database API to fetch true/false questions for the quiz application.
- **Data Handling:** Creation of question objects from retrieved data, management of user input for true/false answers, and tracking of scores.
- **OOP Principles Implementation:** Emphasis on encapsulation, abstraction, inheritance, and polymorphism in designing the quiz application.

## Project Progress

- [X] Define the 'Question' class structure with necessary attributes and methods
- [X] Implement fetching true/false questions from the Open Trivia Database API
- [X] Create a list of question objects based on the retrieved data
- [X] Develop the 'next_question()' method to display new quiz questions iteratively
- [X] Enable user input for true/false answers and implement score tracking functionality
- [X] Finalize the true/false quiz application leveraging Object-Oriented Programming concepts

## Code Snippet - 'Question' Class Initialization and Method Structure

```python
# API endpoint
api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"

# Make a GET request to the API endpoint
response = requests.get(api_url)

# Decode HTML from response
decoded_question_text = html.unescape(current_question.text)
