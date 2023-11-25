# Day 10: Simple Calculator - Functions with Outputs

## Project Description

The Day 10 project features a text-based calculator implemented in Python, designed to perform basic arithmetic operations (addition, subtraction, multiplication, division). It showcases the utilization of functions with outputs, specifically focusing on the integration of return statements within functions to handle arithmetic operations and maintain an integer memory for consecutive calculations.

## Key Concepts Applied

- **Functions with Outputs:** Demonstrating the usage of return statements within functions to produce calculated outputs.
- **Arithmetic Operations:** Implementing addition, subtraction, multiplication, and division functionalities within the calculator program.
- **Integer Memory:** Enabling the calculator to store the result of the previous operation as the starting number for subsequent calculations.

## Project Progress

- [x] Define the structure and objectives of the text-based calculator program
- [x] Implement functions for addition, subtraction, multiplication, and division
- [x] Develop integer memory functionality for consecutive calculations
- [x] Complete the simple calculator program showcasing functions with outputs

## Code Snippet - Simple Calculator Core Functions

```python
# Check if float
def is_float(x):
    if x.replace(".", "").isnumeric():
        return True
    else:
        return False