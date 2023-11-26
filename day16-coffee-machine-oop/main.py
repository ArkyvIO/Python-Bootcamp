from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from defs import *

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_options = menu.get_items().strip('/').split('/')
menu_options_prices = []
menu_table = make_table(menu, menu_options, menu_options_prices)

while True:
    # Clear screen each iteration
    clear_Screen()

    # Print menu for user
    print(menu_table)

    # Get user input for selection
    selection = input("Please make a selection: ").strip().lower() 

    # Check for errors in input and keep attempting til correct
    selection = check_selection_errors(selection, menu_options) 

    # Handle reports and exiting
    if selection == "r":
        for x in range(3, 0, -1):
            clear_Screen()
            coffee_maker.report()
            money_machine.report()
            print(f"Returning in {x} seconds...")
            sleep(1)
        continue
    elif selection == "o":
        sys.exit()

    # Assign drink selection once validated
    drink = menu.find_drink(selection)

    # Check if resources are available to make drink
    if not coffee_maker.is_resource_sufficient(drink):
        print("This machine does not have the required resources to make that selection. Please try again.")
        continue

    