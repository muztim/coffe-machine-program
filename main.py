MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 350,
    "coffee": 200,
}


# TODO Check if resources are sufficient
def resources_sufficient(order_ingredients):
    """Return True when the orders can be made and False when ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is no enough {item}")
            is_enough = False
    return is_enough


# TODO Process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = float(input("How many KES 20 coins ?: ")) * 20
    total += float(input("How many KES 10 coins: ")) * 10
    total += float(input("How many KES 5 coins?: ")) * 5
    total += float(input("How many KES 1 coins?: ")) * 1
    return total


# TODO Check transaction successful?
def transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if the money is insufficient"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's KES {change} shillings in change")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕")


# TODO Print report
def report():
    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: KES {profit}")


# TODO Make Coffee
is_on = True

while is_on:
    order = input("Hello! What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        report()
    else:
        drink = MENU[order]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])


