# Day 11: Full Blackjack Game Implementation (CAPSTONE Project)

## Project Description

The Day 11 project features a full implementation of the Blackjack game in Python, serving as a CAPSTONE project that combines a comprehensive range of previously learned concepts. This game incorporates functionalities from importing modules (`random`, `os`, `time`), dictionaries, functions, functions with returns, booleans, loops (`while` and `for`), conditional arguments, time delay (`sleep`), scorekeeping, game resets, randomization for card selection, user decision-making that influences game outcomes, and score displaying.

## Key Concepts Applied

- **Importing Modules:** Incorporating functionalities from imported modules such as `random`, `os`, and `time` for various game operations.
- **Dictionaries:** Utilizing dictionaries to manage card values, player hands, and game-related information.
- **Functions with Returns:** Implementing functions that return specific outcomes or values based on game actions.
- **Loops and Conditional Statements:** Utilizing `while` and `for` loops, alongside conditional statements, to drive game logic and decision-making.
- **User Decision-Making and Game Outcomes:** Allowing user decisions to influence game outcomes, resulting in varied gameplay scenarios.
- **Score Displaying and Management:** Displaying scores and managing game resets for multiple rounds of play.

## Project Progress

- [x] Define the structure and objectives of the Blackjack game
- [x] Implement functionalities for card selection, hand management, and game logic
- [x] Develop user decision-making processes and game outcomes
- [x] Integrate scorekeeping and reset functionalities for multiple rounds
- [x] Complete the full Blackjack game demonstrating all covered concepts

## Code Snippet - Blackjack Game Core Logic Overview

```python
# Player Phase
    while player_Turn and not busted:
        if get_Points(player_Cards) > 21:
            busted = True
        print("--------------------")
        if not busted:
            if input("Would you like to hit or stay? H/S: ").lower()[0] == "h":
                player_Cards.append(deck.pop(0))
                clear_Screen()
                show_Score(player_Cards, computer_Cards, computer_Turn)
            else:
                player_Turn = False
                computer_Turn = True
        else:
            clear_Screen()
            computer_Turn = True
            show_Score(player_Cards, computer_Cards, computer_Turn)
            print("BUSTED")
            computer_Turn = False