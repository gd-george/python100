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

stash=0

def check_r(choice):
    for i in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][i] >= resources[i]:
            return False
        else:
            resources[i] -= MENU[choice]["ingredients"][i]
    return True


def check_money(choice,total_money):
    global stash
    if MENU[choice]["cost"] < total_money:
        stash=MENU[choice]["cost"]
        return print(f"Enjoy you {choice} 🍵")
    else:
        return print(f"Sorry not coins. Money refunded")


def ask_money():
    n_penny = int(input("No of pennys: "))
    n_nickel =  int(input("No of Nickels: "))
    n_dime =  int(input("No of Dimes: "))
    n_quarters =  int(input("No of quarters: "))

    total_money = (n_penny*0.01) + (n_dime*0.10) + (n_nickel*0.05) + (n_quarters*0.25)
    return total_money

is_one=True
while is_one:
    choice= input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"stash={stash}")
    elif choice == "off":
        is_one=False

    elif choice in MENU:
        if check_r(choice):
             total_money = ask_money()
             check_money(choice,total_money)
        else:
            print("Sorry not enough resources")
            for i in resources:
                print(f"{i}: {resources[i]}")
    else:
        print("Invalid Input")




#todo
# the money collection and resource deplition