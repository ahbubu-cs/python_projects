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

machine_on = True
money_in_machine = 0


def resource_check(order):
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print("Insufficient resources to fulfil order. Returning money.")
            return False
        else:
            return True


def check_coins(money, order):
    total_money = float(money[0]) * 0.25 + float(money[1]) * 0.1 + float(money[2]) * 0.05 + float(money[3] * 0.01)
    if total_money < float(MENU[order]["cost"]):
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def calculate_change(money, order):
    total_money = float(money[0]) * 0.25 + float(money[1]) * 0.1 + float(money[2]) * 0.05 + float(money[3] * 0.01)
    print(f"sum of coins: {total_money}")
    total_money += float(money_in_machine)
    change_new = round(total_money - float(MENU[order]["cost"]), 2)
    return change_new


def update_resources(order):
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] = int(resources[ingredient]) - int(MENU[order]["ingredients"][ingredient])


while machine_on:

    # TODO 1 : Take in order of (espresso,latte,cappuccino,off,report)

    answer = input("What would you like? (espresso,latte,cappuccino): ")
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        print("tada")
        if resource_check(answer):
            # TODO 5 : process coins
            coins = []
            print("Please insert coins.")
            coins.append(int(input("how many quarters?: ")))
            coins.append(int(input("how many dimes?: ")))
            coins.append(int(input("how many nickles?: ")))
            coins.append(int(input("how many pennies?: ")))
            # TODO 6 : Validate if coins is enough for order
            if check_coins(coins, answer):
                change = calculate_change(coins, answer)
                print(f"Here is ${change} in change.")
                print(f"Here is your {answer}. Enjoy!")
                # TODO 7 : Make coffee
                update_resources(answer)
    elif answer == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}ml")
        print(f"money: ${money_in_machine}")
    # TODO 3 : print report when input is "report"
    elif answer == "off":
        machine_on = False
    else:
        print("Command not recognized. Please enter your response again.")
