from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "latte" or user_choice == "cappuccino" or user_choice == "espresso":
        drink = menu.find_drink(user_choice)
        resource = coffee_maker.is_resource_sufficient(drink)
        if resource == True:
            print(money_machine.make_payment(drink.cost))
            make_order = coffee_maker.make_coffee(drink)
        elif resource == False:
            is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("Coffee machine off")
        k = input("press anything to exit")
        is_on = False