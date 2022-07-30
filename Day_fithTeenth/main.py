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
    "money": 0
}


def checking_resources(coffee_type):
    if coffee_type == MENU["espresso"]:
        if resources["water"] > coffee_type["ingredients"]["water"] and resources["coffee"] > \
                coffee_type["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif resources["water"] > coffee_type["ingredients"]["water"] and resources["coffee"] > \
            coffee_type["ingredients"]["coffee"] and resources["milk"] > coffee_type["ingredients"]["milk"]:
        return True
    else:
        return False


def adding_up_values(type_coffee):
    """This function updates the resources values"""
    if type_coffee == MENU["espresso"]:
        resources["coffee"] -= type_coffee["ingredients"]["coffee"]
        resources["water"] -= type_coffee["ingredients"]["water"]
        resources["money"] += type_coffee["cost"]
    else:
        resources["coffee"] -= type_coffee["ingredients"]["coffee"]
        resources["water"] -= type_coffee["ingredients"]["water"]
        resources["milk"] -= type_coffee["ingredients"]["milk"]
        resources["money"] += type_coffee["cost"]


def count_money(type_coffee):
    quarters = int(input(" Enter the amount of quarters please: "))
    dimes = int(input("Enter the amount of dimes please: "))
    nickles = int(input("Enter the amount of dimes please: "))
    pennies = int(input("Enter the amount of pennies please: "))
    total = quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01
    print(f"You have inserted ${total} dollars")
    if total > type_coffee["cost"]:
        if type_coffee["cost"] != total:
            change = "{:.2f}".format(total - type_coffee["cost"])

            print(f"your change is {change}")
        return True
    else:
        return False


def game():
    continue_serving = True
    while continue_serving:
        coffee_served = input("Which drink would you like espresso,latte or cappuccino : ")
        if coffee_served == "off":
            continue_serving = False
            print("Please comeback")
            continue
        elif coffee_served == "report":
            print(resources)
            continue
        elif coffee_served == "espresso" or coffee_served == "latte" or coffee_served == "cappuccino":
            if checking_resources(MENU[coffee_served]):
                print(f"Please enter your money,\n you need {MENU[coffee_served]['cost']}")
                if count_money(MENU[coffee_served]):
                    adding_up_values(MENU[coffee_served])
                    print(f"your coffee ☕ served contains {MENU[coffee_served]}")
                else:
                    print("Not enough money inserted")
            else:
                print("Sorry not enough ingredients")
                continue


game()
# TODO
