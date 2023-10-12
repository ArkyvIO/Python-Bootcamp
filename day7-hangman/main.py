import random
import os
import string

# Assign bool variable for game over and play again
playAgain = 1
gameOver = 0

while playAgain:
    # Assign an empty wordlist
    word_list = list()

    # Open wordlist.txt
    with open("wordlist.txt", "r") as file:
        word_list = [word.strip() for word in file.readlines()]

    # Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    chosen_word = random.choice(word_list).upper()

    # Create empty list for displaying '_'
    display = list()
    for x in range(0, len(chosen_word)):
        display.append(" _ ")

    # Keep track of strikes
    strikes = 0

    # List of letters available
    avail = list(string.ascii_uppercase)

    # List of used letters
    used = list()

    while not gameOver:
        # Clear screen
        os.system("cls" if os.name == "nt" else "clear")

        # Is guess already used? Bool placeholder until guess made.
        acceptable = 0

        # Print all missing and discovered characters
        print("".join(display))

        # Show strikes
        print(f"You currently have {strikes} strikes.")

        # Show available letters
        print("The following letters are still available: ")
        print("".join(avail))

        while not acceptable:
            # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess uppercase.
            guess = input("Please guess a letter: ")[0].upper()

            if guess in avail:
                acceptable = 1
                avail.remove(guess)
            else:
                print("That letter is already used. Try again.")

        # Check if guess is in the word
        if guess in chosen_word:
            for x in range(len(chosen_word)):
                if guess == chosen_word[x]:
                    display[x] = " " + chosen_word[x] + " "
        else:
            strikes += 1

        if strikes == 5:
            gameOver = 1
            print("YOU LOSE!")

        if " _ " not in display:
            print("YOU WIN!")
            gameOver = 1

    # See if user wants to play again
    if input("Do you want to play again? Y/N: ")[0].upper() == "N":
        playAgain = 0
    else:
        gameOver = 0
