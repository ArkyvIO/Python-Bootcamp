# Day 7: Hangman Game Utilizing Python Concepts

## Project Description

The Day 7 project focuses on creating an interactive Hangman game using a variety of Python concepts learned from previous days. It incorporates elements such as randomization, lists, ASCII art, variables, loops, conditional statements, booleans, append functions for lists, and screen clearing for readability within the game interface.

## Key Concepts Applied

- **File Handling:** Opening and reading files within Python to access external resources, such as word lists, enhancing the gameplay experience by expanding the available vocabulary.
- **Randomization:** Utilizing randomization to select words for the Hangman game from a predetermined list or source.
- **Lists and Append Functions:** Implementing lists and the append function to manage and manipulate game-related data.
- **ASCII Art for User Interface:** Using ASCII art for visual representation and enhancing the user interface experience.
- **Variables and Booleans:** Employing variables and booleans to store and manage game states, player input, and game logic.
- **Loops and Conditional Statements:** Employing loops and conditional statements for iterative gameplay and decision-making processes.

## Project Progress

- [x] Define the game structure and objectives
- [x] Set up initial code structure
- [x] Implement word selection and randomization
- [x] Develop gameplay mechanics with ASCII art visualization
- [x] Complete playable game

## Code Snippet - Hangman Game Core Logic Example

```python
# Open wordlist.txt
with open("wordlist.txt", "r") as file:
    word_list = [word.strip() for word in file.readlines()]

# Create empty list for displaying '_'
display = list()
for x in range(0, len(chosen_word)):
    display.append(" _ ")

# Clear screen
os.system("cls" if os.name == "nt" else "clear")