from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
machine_running = True

while machine_running:
    print(menu.get_items(money_machine.CURRENCY))

    while True:
        selection = input("Please make your beverage selection: ").lower()
        if selection == 'report':
            coffee_machine.report()
            money_machine.report()

        elif selection == "exit":
            machine_running = False
            break

        else:
            try:
                selection = int(selection)
                if selection > len(menu.menu):
                    print("Please enter a number from the menu \n")

                else:
                    selection = menu.select_drink(selected=selection)
                    break


            except ValueError:
                print("Please enter a numeric value\n")


    drink = menu.find_drink(selection)

    if money_machine.make_payment(drink.cost) == True:
        coffee_machine.make_coffee(order = drink)
        

    else:
        pass

    while True:
        check = input("Do you wish to continue using coffee machine. Type 'Y' for yes and 'N' for no:\n")
        if check == "report":
            coffee_machine.report()
            money_machine.report()
        
        elif check == "y":
            break
        else:
            machine_running = False
            break

