from defs import *

profit = 0

while True:
    # Get user choice and money for choice
    selection = get_user_choice()

    if not check_resources(MENU[selection]["ingredients"]):        
        refill_ingredients()

    if not check_funds_available(selection):
        dots = ""
        for x in range(3):
            clear_Screen()
            print(f"You have not entered enough money for this selection. Try again.{dots}")
            dots += "."
            sleep(1)
        continue

    subtract_resources(selection)
    profit_and_change(selection)

    print(f"Your {selection} has been dispensed. Thank you and enjoy!")

    sleep(3)