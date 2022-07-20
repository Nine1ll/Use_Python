from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if money_machine.make_payment(drink.cost) and coffee_machine.is_resource_sufficient(drink):
            coffee_machine.make_coffee(drink)




