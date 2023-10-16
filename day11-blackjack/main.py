import random
import os
import time
from dictionary import deck_of_cards

play_Again = True
game_Over = False

def shuffle_cards(num_Decks):
    deck_to_shuffle = []
    for _ in range(num_Decks):
        for card in deck_of_cards:
            deck_to_shuffle.append(card)
    random.shuffle(deck_to_shuffle)
    return deck_to_shuffle

def get_Points(hand):
    points = 0
    aces = 0
    for card in hand:
        if deck_of_cards[card] == 1:
            aces += 1
        else:
            points += deck_of_cards[card]
    
    for ace in range(aces):
        if (points + 11) > 21:
            points += 1
        else:
            points += 11

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

print("Welcome to BlackJack!") # Print welcome screen
print("--------------------")
time.sleep(1)
print("Shuffling and dealing cards...")
time.sleep(2)
clear_Screen()

num_Decks = 2 # We will use 2 decks unless the player wants one, choice to be implemented later
deck = shuffle_cards(num_Decks) # Shuffle the deck
shuffle_Length = len(deck) / 3

while play_Again: # We will stop the program if the player doesn't want to play again, but need to start the loop at least once
    computer_Turn = False # The player will go first, so computer_Turn should be false
    player_Turn = True # The player will go first, so player_Turn should be true
    busted = False # Boolean for if player busts

    player_Cards = [] # Initialize an empty list for the player
    computer_Cards = [] # Initialize an empty list for the computer

    if len(deck) < shuffle_Length:
        clear_Screen()
        print("Deck low, returning cards to deck and shuffling...")
        time.sleep(1)
        deck = shuffle_cards(num_Decks)

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
            show_Score(player_Cards, computer_Cards, computer_Turn)
            print("BUSTED")

    # Computer phase
    while computer_Turn:
        clear_Screen()
        show_Score(player_Cards, computer_Cards, computer_Turn)
        while get_Points(computer_Cards) < 17:
            computer_Cards.append(deck.pop(0))
            time.sleep(1)
            clear_Screen()
            show_Score(player_Cards, computer_Cards, computer_Turn)
        if get_Points(computer_Cards) > 21:
            clear_Screen()
            show_Score(player_Cards, computer_Cards, computer_Turn)
            print("YOU WIN - DEALER BUST")
            computer_Turn = False
            break
        else:
            if get_Points(player_Cards) > get_Points(computer_Cards):
                clear_Screen()
                show_Score(player_Cards, computer_Cards, computer_Turn)
                print("YOU WIN")
                computer_Turn = False
                break
            elif get_Points(player_Cards) < get_Points(computer_Cards):
                clear_Screen()
                show_Score(player_Cards, computer_Cards, computer_Turn)
                print("COMPUTER WINS")
                computer_Turn = False
                break
            else:
                clear_Screen()
                show_Score(player_Cards, computer_Cards, computer_Turn)
                print("TIE")
                computer_Turn = False
                break

    if input("Would you like to play again? Y/N").lower()[0] == "n":
        play_Again = False
    else:
        clear_Screen()