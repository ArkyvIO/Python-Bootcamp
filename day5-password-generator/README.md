# Day 5: Password Generator

## Project Description

For Day 5, I worked on a Password Generator project using Python. This project focused on implementing Python loops (`for` and `while`), using random numbers, and incorporating `if` statements. The Password Generator generates secure passwords based on user-defined parameters.

## Concepts Learned

- **Python Loops:** Understanding iterative actions using loops like `for` and `while`.
- **Randomization in Python:** Utilizing the `random` module to generate random elements.
- **Conditional Statements (`if`):** Implementing conditions to control program flow.

## Project Progress

- [x] Define project goals
- [x] Implement password generation functionality
- [x] Complete functional Password Generator using Python

## Code Snippet - Password Generation Example

```python
# Lists for character use
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Assign a random location for the symbols and the numbers
symbolLocs = [] # Create empty array to hold position values to place symbols in the password array
numberLocs = [] # Create empty array to hold position values to place numbers in the password array
while len(symbolLocs) < nr_symbols:
    possibleLocation = random.randint(0, nr_letters - 1)
    if possibleLocation not in symbolLocs and possibleLocation not in numberLocs:
        symbolLocs.append(possibleLocation)
while len(numberLocs) < nr_numbers:
    possibleLocation = random.randint(0, nr_letters - 1)
    if possibleLocation not in symbolLocs and possibleLocation not in numberLocs:
        numberLocs.append(possibleLocation)

# See code for more information