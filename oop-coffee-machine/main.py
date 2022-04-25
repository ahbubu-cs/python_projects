from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1 : “What would you like? (espresso/latte/cappuccino/):”


new_menu = Menu()
new_moneymachine = MoneyMachine()
new_coffeemaker = CoffeeMaker()


# new_moneymachine.__init__()
# new_coffeemaker.__init__()
# new_menu.__init__()




is_on = True

while is_on:

    answer = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if answer not in new_menu.get_items() and answer not in new_menu.get_items() and answer != "off" and answer != "report":
        print("Response is not recognised. Please try again.")
    else:
        if answer == "off":
            is_on = False
        elif answer == "report":
            new_moneymachine.report()
            new_coffeemaker.report()
        else:
            if new_coffeemaker.is_resource_sufficient(new_menu.find_drink(answer)):
                if new_moneymachine.make_payment(new_menu.find_drink(answer).cost):
                    new_coffeemaker.make_coffee(new_menu.find_drink(answer))




