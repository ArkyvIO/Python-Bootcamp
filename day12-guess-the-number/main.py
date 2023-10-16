import random
import time
import os

def clear_Screen():
    os.system("cls" if os.name == "nt" else "clear")

keep_Playing = True
HARD = 1
EASY = 0

while keep_Playing:
    # Print logo

    diff_Set = False
    game_Over = False
    difficulty = 0 # 1 = Hard / 0 = Easy
    turns = 0
    guessed = False

    while not diff_Set:
        difficulty_input = input("Would you like to play on (H)ard or (E)asy mode? ").lower()
        if difficulty_input and difficulty_input[0] == "h":
            difficulty = 1
            diff_Set = True
        elif difficulty_input and difficulty_input[0] == "e":
            difficulty = 0
            diff_Set = True
        else:
            print("Invalid input. Please try again.")

    if difficulty == HARD:
        print("Difficulty is set to: HARD")
        turns = 5
        time.sleep(1)
        clear_Screen()
    else:
        print("Difficulty is set to: EASY")
        turns = 10
        time.sleep(1)
        clear_Screen()

    random_Num = random.randint(1,100)    

    while not guessed and not game_Over:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess == random_Num:
            guessed = True
            clear_Screen()
            print("YOU WIN!")
            print(f"The number was {random_Num}")
        elif guess > random_Num:
            print("TOO HIGH")
            turns -= 1
            print(f"You have {turns} turns left...")
        elif guess < random_Num:
            print("TOO LOW")
            turns -= 1
            print(f"You have {turns} turns left...")

        if turns == 0:
            print("GAME OVER")
            print(f"The number was {random_Num}")
            game_Over = True

    play_Again_Accepted = False

    while not play_Again_Accepted:
        play_Again = input("Would you like to play again? Y/N: ")

        if play_Again == "":
            print("You entered nothing. Try again...")
        elif play_Again.lower()[0] == "n":
            keep_Playing = False
            play_Again_Accepted = True
        elif play_Again.lower()[0] == "y":
            play_Again_Accepted = True
        else:
            print("Not understood, try again...")
        