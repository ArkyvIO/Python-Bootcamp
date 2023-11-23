MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": {
        "amount": 300,
        "cost": 0,  # Tap water
        "max_amount": 300
    },
    "milk": {
        "amount": 200, # In mL
        "cost": 0.105,  # $.105 per mL, average $4 per gallon
        "max_amount": 200
    },
    "coffee": {
        "amount": 100, # In g
        "cost": 0.015,  # $.015 per g, average $6 per 400g
        "max_amount": 100
    }
}

money = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
}

profit = 0