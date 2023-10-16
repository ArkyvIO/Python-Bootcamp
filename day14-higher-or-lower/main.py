import random
import time
import os

from game_data import data
from art import logo

def get_random():
    return random.choice(data)

def print_data(random_choice):
    name = random_choice["name"]
    description = random_choice["description"]
    country = random_choice["country"]
    print(f"{name}. {description}, {country}")

def clear_Screen():
    os.system("cls" if os.name == "nt" else "clear")

keep_Playing = True

while keep_Playing:

    check = 0
    score = 0
    played = 0
    still_in_game = True

    while still_in_game:
        clear_Screen()
        print(logo)

        if played > 0:
            print(f"Current Score: {score}")

        choice_Num1 = get_random()
        choice_Num2 = get_random()

        while choice_Num1 == choice_Num2:
            choice_Num2 = get_random()

        print("A: ")
        print_data(choice_Num1)
        print("B: ")
        print_data(choice_Num2)
        
        guess_Accepted = False
        
        while not guess_Accepted:
            guess = input("Who has more followers? Type A or B: ")
            if guess == "":
                print("You entered nothing. Try entering one of the presented options...")
            elif guess.lower()[0] == "a" or guess.lower()[0] == "b":
                guess_Accepted = True
            else:
                print("You didn't enter one of the available options. Please try again.")

        if choice_Num1["follower_count"] > choice_Num2["follower_count"] and guess == "a":
            score += 1
        elif choice_Num2["follower_count"] > choice_Num1["follower_count"] and guess == "b":
            score += 1
        else:
            print("Sorry! Game over!")
            still_in_game = False

        played += 1
    
    keep_playing_accepted = False

    while not keep_playing_accepted:
        keep_playing_input = input("Would you like to play again? Y/N: ")
        if keep_playing_input == "":
            print("You entered nothing. Try again...")
        elif keep_playing_input.lower()[0] == "n":
            keep_Playing = False
            keep_playing_accepted = True
        elif keep_playing_input.lower()[0] == "y":
            keep_Playing = True
            keep_playing_accepted = True
        else:
            print("Command not recognized, try again...")