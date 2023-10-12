print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇


runAgain = 1  # Only run again if the user wants to, boolean set

while runAgain:
    choice = input(
        'You\'re at a cross road. Where do you want to go? Type "left" or "right".'
    )

    if choice.lower() == "left":
        choice2 = input(
            "You found a wide stream blocking your path. The water is quite deep this time of day. Do you swim or wait?"
        )
        if choice2.lower() == "wait":
            choice3 = input(
                "You arrive at 3 doors of different colors. Red, Blue, and Yellow. You must pick one."
            )
            if choice3.lower() == "yellow":
                print("You found the treasure! Congratulations, you win!")
            elif choice3.lower() == "red":
                print("You died in a blaze of fire. GAME OVER.")
            elif choice3.lower() == "blue":
                print("You were eaten in a room full of monsters. GAME OVER.")
            else:
                print("You chose a door that didn't exist. You died. GAME OVER.")
        else:
            print("You drowned while trying to cross the stream. GAME OVER.")
    else:
        print("You fell into a hole and died. GAME OVER.")

    check = input("Would you like to play again?").lower()

    if check[0] == "y":
        runAgain = 1
    else:
        runAgain = 0
