from art import logo
import os

still_Bidding = True  # Loop until bidding has completed

bidder_Info = {}  # Dict full of bidders and bids


# Check if float
def is_float(x):
    if x.replace(".", "").isnumeric():
        return True
    else:
        return False


while still_Bidding:
    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # Clear the screen to ensure no previous information is seen by new bidder
    print(logo)  # Print the logo, always, first
    nameAccepted = False
    while not nameAccepted:
        name = input("Please enter your name: ").upper()
        if name in bidder_Info:
            print(
                "Unfortunately, that name has already been used. Please add a surname or initial to differentiate. Try again."
            )
        else:
            nameAccepted = True
    bidAccepted = False
    while not bidAccepted:
        bid = input("Please enter your bid: ")
        if bid.isnumeric() or is_float(bid):
            bidAccepted = True
        else:
            print("That is not a numeric value, please try again.")
    bidder_Info[name] = bid
    if (input("Are there other users who want to bid? Y/N: ")[0].upper()) == "N":
        still_Bidding = False

winnerName = str()
winnerBid = float()

for key in bidder_Info:
    if float(bidder_Info[key]) > winnerBid:
        winnerBid = float(bidder_Info[key])
        winnerName = key

winnerBid = "{:.2f}".format(winnerBid)

os.system("cls" if os.name == "nt" else "clear")

print(logo)

print(f"The winner of the bid is {winnerName} with a bid of ${winnerBid}!")
