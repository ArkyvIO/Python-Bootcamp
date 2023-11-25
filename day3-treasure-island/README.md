# Day 3: Treasure Island Game

## Project Description

For Day 3, I created a Treasure Island game using Python. The game involves decision-making using control flow and logical operators. Players navigate through a series of choices to discover hidden treasure on an island.

## Concepts Learned

- **Control Flow in Python:** Implementing decision-making structures such as if statements, elif, and else clauses.
- **Logical Operators:** Understanding and using logical operators (e.g., `and`, `or`, `not`) to create conditional statements.

## Project Progress

- [x] Define project goals
- [x] Set up the initial game structure
- [x] Implement control flow for player choices
- [x] Complete the Treasure Island game with multiple outcomes

## Code Snippet - Game Structure Example

```python
print("Welcome to Treasure Island.")

direction = input("Choose a path: 'left' or 'right': ").lower()

if direction == "left":
    choice = input("You found a key. Do you want to open the door? 'yes' or 'no': ").lower()

    if choice == "yes":
        print("Congratulations! You found the treasure. You Win!")
    else:
        print("You chose not to open the door. Game Over.")
else:
    print("You fell into a hole. Game Over.")
