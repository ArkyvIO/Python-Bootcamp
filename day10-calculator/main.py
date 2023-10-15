from art import logo


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2

# Check if float
def is_float(x):
    if x.replace(".", "").isnumeric():
        return True
    else:
        return False

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

continue_Calc = True
use_Answer = False

while continue_Calc == True:
    # Only ask for first number if we are not reusing the answer from a previous iteration of the calculator
    if use_Answer == True:
        num1 = answer
        print(f"Since we are using the previous answer, the first number is {num1}.")  # Repeat the answer previously calculated to user to let them know we are still using it
    else:
        num1 = input("What's the first number?: ")  # Get first number if not using previous answer

    while not str(num1).isnumeric() or not is_float(str(num1)): # We need to convert to strings or we get errors checking if numberic or float
        num1 = input("You entered a non-number, please try again: ")

    print("Available operators: ")

    # Show all available operators for use in the dictionary
    for x in operations:
        print(x, end="", flush=True)

    print(" ")  # New line

    operator_Symbol = input("Please enter an operator to use: ")

    operator_Accepted = False  # Boolean for error checking input

    num2 = input("What's the second number?: ") # Get second number, we will always need this

    while not str(num2).isnumeric() or not is_float(str(num2)):
        num2 = input("You entered a non-number, please try again: ")

    while not operator_Accepted:
        for x in operations:
            if x == operator_Symbol:
                operator_Accepted = True
        if not operator_Accepted:
            operator_Symbol = input(
                "You did not enter a correct operator. Please try again: "
            )

    answer = operations[operator_Symbol](
        float(num1), float(num2)
    )  # Call dictionary to route to function

    if answer % 1 == 0:
        answer = int(answer)

    print(f"The answer to {num1} {operator_Symbol} {num2} is {answer}.")

    if (
        input(
            "Would you like to continue using this answer in more calculations? Y/N: "
        ).upper()[0]
        == "Y"
    ):
        use_Answer = True
    else:
        if input("Would you like to start over? Y/N: ").upper()[0] == "N":
            continue_Calc = False
