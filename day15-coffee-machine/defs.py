import os, sys, time
from info import MENU, resources, money, profit

def clear_Screen():
    os.system("cls" if os.name == "nt" else "clear")

def sleep(seconds):
    time.sleep(seconds)

def display_menu():
    clear_Screen()
    print("What kind of coffee would you like?")
    print("Espresso: $1.50")
    print("Latte: $2.50")
    print("Cappuccino: $3.00")
    print_money()
    

def display_resources_and_profits():
    clear_Screen()
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}")
    input("Press enter to continue...")

def calculate_cost(selected_coffee):
    return MENU[selected_coffee]['cost']

def get_user_choice():
    while True:
        clear_Screen()
        display_menu()
        print("")
        print("Please type $ to enter funds, or type the name of your selection.")
        selection = input("Selection: ").strip().lower()

        if not selection:
            clear_Screen()
            display_menu()
            print("Please enter a valid selection.")
            continue

        selection = selection[0]

        if selection == "e":
            return "Espresso"
        elif selection == "l":
            return "Latte"
        elif selection == "c":
            return "Cappuccino"
        elif selection == "r":
            display_resources_and_profits()
            display_menu()
        elif selection == "$":
            get_money()
            continue
        elif selection == "o":
            clear_Screen()
            print("Turning off...")
            exit()
        else:
            print("That is not an available item. Try again.")

def check_resources(selection_ingredients):
    insufficient_resources = [ingredient for ingredient, amount in selection_ingredients.items() if ingredient != "water" and amount > resources[ingredient]["amount"]]

    if insufficient_resources:
        print("Too low on:")
        for ingredient in insufficient_resources:
            print(ingredient)
        return False
    else:
        return True

def get_money():
    while True:
        clear_Screen()
        print("This machine takes the following types of currency:")
        print("Quarters")
        print("Dimes")
        print("Nickels")
        print("-----------")
        print_money()
        print("-----------")
        selection = input("Enter money or 'R' to return: ").strip().lower()

        if not selection:
            clear_Screen()
            print("Please enter a valid selection.")
            continue

        if selection == "q":
            money["quarters"] = money["quarters"] + 1
        elif selection == "d":
            money["dimes"] = money["dimes"] + 1
        elif selection == "n":
            money["nickels"] = money["nickels"] + 1
        elif selection == "r":
            break
        else:
            print("That's not a menu option, try again.")


def print_money():
    total_Money = (.25 * money["quarters"]) + (.10 * money["dimes"]) + (.05 * money["nickels"])
    print(f"You have ${total_Money} available.")

def refill_ingredients():
    global profit
    while True:
        refill_cost = calc_refill_cost()
        if refill_cost < profit:
            leftover_profit = profit - refill_cost
            print(f"Refilling machine using profits. ${refill_cost} will be taken from our profit total of ${profit}, leaving ${leftover_profit}.")
            profit = leftover_profit
            for resources, details in resources.items():
                details["amount"] = details["max_amount"]
            break
        else:
            clear_Screen()
            print("Unfortunately, there is not enough resources to continue. Please contact your management.")
            exit()

def calc_refill_cost():
    total_refill_cost = 0

    for resource, details in resources.items():
        amount_to_refill = details["max_amount"] - details["amount"]
        cost_per_unit = details["cost"]
        money_needed = amount_to_refill * cost_per_unit

        total_refill_cost += money_needed

    return total_refill_cost

def profit_and_change(choice_of_beverage):
    global profit
    cost_of_beverage = MENU[choice_of_beverage]["cost"]
    money_entered = (.25 * money["quarters"]) + (.10 * money["dimes"]) + (.05 * money["nickels"])
    profit += money_entered - cost_of_beverage
    if money_entered > cost_of_beverage:
        refund = money_entered - cost_of_beverage
        print(f"You are being refunded a totaling of ${refund}. Please check the coin return.")
    for funds in money:
        money[funds] = 0

def check_funds_available(choice_of_beverage):
    cost_of_beverage = MENU[choice_of_beverage]["cost"]
    money_entered = (.25 * money["quarters"]) + (.10 * money["dimes"]) + (.05 * money["nickels"])
    if money_entered > cost_of_beverage:
        return True
    else:
        return False
    
def subtract_resources(choice_of_beverage):
    ingredients_needed = MENU[choice_of_beverage]["ingredients"]

    for ingredient, amount_needed in ingredients_needed.items():
        if ingredient != "water":
            resources[ingredient]["amount"] -= amount_needed
            

def exit():
    sys.exit()