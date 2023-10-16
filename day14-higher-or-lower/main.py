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
check = 0
score = 0

while keep_Playing:
    clear_Screen()
    print(logo)
    score = 0
    choice_Num1 = get_random()
    choice_Num2 = get_random()

    while choice_Num1 == choice_Num2:
        choice_Num2 = get_random()


    print("A: ")
    print_data(choice_Num1)
    print("B: ")
    print_data(choice_Num2)

    guess = input("Who has more followers? Type A or B: ")

    keep_Playing = False
