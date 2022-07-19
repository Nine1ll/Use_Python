MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}


def is_sufficient(ordered_menu):
    if ordered_menu == "espresso":
        if resources["water"] < MENU[ordered_menu]["ingredients"]["water"] or resources["coffee"] < MENU[ordered_menu]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough resources")
            return False
    else:
        for resource in resources:
            if resource == "Money":
                return
            else:
                if resources[resource] < MENU[ordered_menu]["ingredients"][resource]:
                    print(f"Sorry there is not enough {resource}")
                    return False


def resources_management(ordered_menu):
    if is_sufficient(ordered_menu):
        if ordered_menu == "espresso":
            resources["water"] -= MENU[ordered_menu]["ingredients"]["water"]
            resources["coffee"] -= MENU[ordered_menu]["ingredients"]["coffee"]
        else:
            resources["water"] -= MENU[ordered_menu]["ingredients"]["water"]
            resources["coffee"] -= MENU[ordered_menu]["ingredients"]["coffee"]
            resources["milk"] -= MENU[ordered_menu]["ingredients"]["milk"]
        resources["Money"] += MENU[ordered_menu]["cost"]


def insert_coin():
    total_price = 0
    print("Please insert coins.")
    for coin in coins:
        number = int(input(f"how many {coin}?: "))
        total_price += (number*coins[coin])
    return round(total_price, 3)


def refund(ordered_menu, paid_money):
    if MENU[ordered_menu]["cost"] > paid_money:
        return True
    else:
        return False


def changes(ordered_menu_price, paid_money):
    change = round(paid_money - ordered_menu_price, 3)
    if change > 0:
        print(f"Here is ${change} in change.")


resources["Money"] = 0

while True:
    order = input("  What would you like? (espresso/latte/cappuccino): ")
    if order == "break":
        break
    else:
        if order == "report":
            print(
                f" Water: {resources['water']}\n Milk: {resources['milk']}\n Coffee: {resources['coffee']} \n Money: {resources['Money']}$")
        else:
            insert_price = insert_coin()
            if refund(order, insert_price):
                print("Sorry that's not enough money. Money refunded.")
            else:
                changes(MENU[order]["cost"], insert_price)
                resources_management(order)
                print(f"Here is {order} ☕. Enjoy!")


print("Thank you for use our service! :)")
