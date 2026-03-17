from prettytable import PrettyTable # type: ignore


class CoffeeMaker:

    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        report_table = PrettyTable()
        report_table.align = 'l'
        report_table.field_names = ["Ingredients", "Quantity(In ml/g)"]
        quant = []
        for ingredient in self.resources:
            quant.append([ingredient, self.resources[ingredient]])
        report_table.add_rows(quant)
        print(report_table)

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
