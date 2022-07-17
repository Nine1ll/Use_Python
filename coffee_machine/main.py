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
# input("What would you like? ():") 에 입력값이  report일시 ,
# 지금 기계에 남은 resources + Money 를 보여줘야함,
#
# 가격보다 coin을 적게 넣으면, 모두 환불
# 가격보다 많이 넣으면 남은 돈을 계산해서 환불해줌.


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


order = input("  What would you like? (espresso/latte/cappuccino): ")
insert_price = insert_coin()

if refund(order, insert_price):
    print("Sorry that's not enough money. Money refunded.")
else:
    changes(MENU[order]["cost"], insert_price)
    print(f"Here is {order} ☕. Enjoy!")