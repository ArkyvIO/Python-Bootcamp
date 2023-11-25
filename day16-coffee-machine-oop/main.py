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

    if selection == "r":
        clear_Screen()
        coffee_maker.report()
        sleep(3)
        continue
    elif selection == "o":
        sys.exit()

    
    
