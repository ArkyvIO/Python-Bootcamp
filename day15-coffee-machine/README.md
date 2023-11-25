# Day 15: Simulated Coffee Machine Program

## Project Description

The Day 15 project involves creating a simulated coffee machine program in Python. This program manages dictionaries containing menu information, keeps track of profits earned from coffee sales, handles money entered by users for coffee purchases (providing refunds for excessive money), tracks available resources for making coffee and offers refill options, allows users to select coffee types, provides resource status reports, implements graceful shutdown procedures, and incorporates variable importing from other documents.

## Key Concepts Applied

- **Dictionary Handling:** Managing dictionaries containing menu information, available resources, and other relevant data within the coffee machine program.
- **Profit Tracking:** Keeping track of profits earned from coffee sales and refunding excess money entered by users.
- **Resource Management:** Monitoring and updating available resources for making coffee and providing options for refills.
- **User Selections:** Allowing users to select different coffee types and managing their selections within the program.
- **Resource Reporting:** Providing reports detailing resource statuses and availability within the coffee machine.
- **Graceful Shutdown Procedures:** Implementing procedures for a controlled and graceful shutdown of the coffee machine program.
- **Variable Importing:** Importing variables and data from other documents to facilitate functionalities within the program.

## Project Progress

- [x] Define the structure and objectives of the simulated coffee machine program
- [x] Manage dictionaries containing menu information, resources, and profit tracking
- [x] Implement user interfaces for coffee selection, money handling, and resource management
- [x] Develop functionalities for providing resource reports and graceful shutdown procedures
- [x] Complete the simulated coffee machine program integrating all specified functionalities

## Code Snippet - Number Guessing Game (Scope and Difficulty Levels)

```python
def check_resources(selection_ingredients):
    insufficient_resources = [ingredient for ingredient, amount in selection_ingredients.items() if ingredient != "water" and amount > resources[ingredient]["amount"]]

    if insufficient_resources:
        print("Too low on:")
        for ingredient in insufficient_resources:
            print(ingredient)
        return False
    else:
        return True