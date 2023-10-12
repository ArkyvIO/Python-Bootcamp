rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import os


def choicePrint(x):
    if x == 1:
        print(rock)
    elif x == 2:
        print(paper)
    else:
        print(scissors)


import random

scoreUser = 0  # Score holding variable for user
scoreComp = 0  # Score holding variable for computer
gameOver = 0  # Game over bool
playAgain = 1  # Play again bool

while playAgain:
    while not gameOver:
        if scoreUser > 0 or scoreComp > 0:
            print(f"The current score is {scoreUser} (YOU) to {scoreComp} (COMP)")
        choiceUser = int(
            input(
                "Best 3 out of 5! Please choose 1 for Rock, 2 for Paper, and 3 for Scissors: "
            )
        )
        os.system("cls" if os.name == "nt" else "clear")
        choiceComp = random.randint(1, 3)
        print("You chose: ")
        choicePrint(choiceUser)
        print("----------")
        print("Computer chose: ")
        choicePrint(choiceComp)
        print("----------")
        if choiceUser == 1:
            if choiceComp == 1:
                print("TIE")
            elif choiceComp == 2:
                print("COMPUTER POINT")
                scoreComp += 1
            else:
                print("YOUR POINT")
                scoreUser += 1
        elif choiceUser == 2:
            if choiceComp == 1:
                print("YOUR POINT")
                scoreUser += 1
            elif choiceComp == 2:
                print("TIE")
            else:
                print("COMPUTER POINT")
                scoreComp += 1
        else:
            if choiceComp == 1:
                print("COMPUTER POINT")
                scoreComp += 1
            elif choiceComp == 2:
                print("YOUR POINT")
                scoreUser += 1
            else:
                print("TIE")
        if scoreUser == 3 or scoreComp == 3:
            gameOver = 1
            print("WE HAVE A WINNER: ")
            if scoreUser == 3:
                print("YOU WIN!!!")
            else:
                print("COMPUTER WINS")
            if input("Would you like to play again? Y/N")[0].lower() == "y":
                gameOver = 0
                scoreComp = 0
                scoreUser = 0
            else:
                playAgain = 0
