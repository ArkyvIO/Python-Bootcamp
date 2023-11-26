import sys, os, time
from prettytable import PrettyTable

def make_table(menu, menu_options, menu_options_prices):
    
    menu_table = PrettyTable()

    for drink in menu_options:
        if menu.find_drink(drink) != "none":
            menu_options_prices.append(menu.find_drink(drink).cost)

    for x in range(len(menu_options)):
        menu_options[x] = menu_options[x].capitalize()

    menu_table.add_column("Drinks", menu_options)
    menu_table.add_column("Prices", menu_options_prices)

    return menu_table

def check_selection_errors(selection, menu_options):
    while True:
        if not selection:
            selection = input("I'm sorry, that is not a valid selection. Please try again: ").strip().lower()
            continue
        if selection not in menu_options:
            if selection[0].lower() == "o":
                return selection[0]
            elif selection[0].lower() == "r":
                return selection[0]
            elif selection[0].lower() == "l":
                return "latte"
            elif selection[0].lower() == "e":
                return "espresso"
            elif selection[0].lower() == "c":
                return "cappuccino"
            else:
                return "latte"
        if selection.capitalize() not in menu_options and selection[0] != "o" and selection[0] != "r":
            selection = input("I'm sorry, that is not a valid selection. Please try again: ").strip().lower()
            continue
        if selection in menu_options:
            return selection
        else:
            return "latte"

def clear_Screen():
    os.system("cls" if os.name == "nt" else "clear")

def sleep(seconds):
    time.sleep(seconds)