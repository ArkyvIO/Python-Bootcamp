import random
import os
import time
from dictionary import deck_of_cards

play_Again = True
playing_Hand = True

def shuffle_cards(num_Decks):
    deck_to_shuffle = []
    for _ in range(num_Decks):
        for card in deck_of_cards:
            deck_to_shuffle.append(card)
    random.shuffle(deck_to_shuffle)
    return deck_to_shuffle

def get_Points(hand):
    points = 0
    for card in hand:
        points += deck_of_cards[card]
    return points

def show_Score(player_Cards, computer_Cards, computer_Turn):
    print(f"There are still {len(deck)} cards in the deck.")
    # Show cards and point values for the player
    print(f"Your cards totaling {get_Points(player_Cards)} points: ")
    for card in player_Cards:
        print(card)
    
    print("--------------------")

    # Show cards and point value for the computer, hiding the second card unless player done
    if computer_Turn:
        print(f"Computer cards totaling {get_Points(computer_Cards)} points: ")
        for card in computer_Cards:
            print(card)
    else:
        print(f"Computer cards with {deck_of_cards[computer_Cards[0]]} points visible: ")
        print(computer_Cards[0])
        print("HIDDEN")

def clear_Screen():
    os.system("cls" if os.name == "nt" else "clear")


while play_Again: # We will stop the program if the player doesn't want to play again, but need to start the loop at least once
    computer_Turn = False # The player will go first, so computer_Turn should be false
    player_Turn = True # The player will go first, so player_Turn should be true
    num_Decks = 2 # We will use 2 decks unless the player wants one, choice to be implemented later
    busted = False # Boolean for if player busts

    print("Welcome to BlackJack!") # Print welcome screen
    print("--------------------")
    if input("Are you ready to play? Y/N: ").lower()[0] == "y":
        clear_Screen()
    else:
        print("Really? Then why did you start the program?")
        time.sleep(3)
        break

    deck = shuffle_cards(num_Decks) # Shuffle the deck

    player_Cards = [] # Initialize an empty list for the player
    computer_Cards = [] # Initialize an empty list for the computer

    # Two cards for the player
    for _ in range(2):
        player_Cards.append(deck.pop(0))

    # Two cards for the computer
    for _ in range(2):
        computer_Cards.append(deck.pop(0))

    show_Score(player_Cards, computer_Cards, computer_Turn)

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
            print("BUSTED")

    # Computer phase
    while computer_Turn:
        show_Score()
        while get_Points(computer_Cards) < 17:
            computer_Cards.append(deck.pop(0))
            show_Score()
        if get_Points(computer_Cards) > 21:
            print("YOU WIN")
            computer_Turn = False
            break
        else:
            if get_Points(player_Cards) > get_Points(computer_Cards):
                print("YOU WIN")
                computer_Turn = False
                break
            else:
                print("TIE")
                computer_Turn = False
                break

    play_Again = False