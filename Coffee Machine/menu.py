from prettytable import PrettyTable # type: ignore


class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self, currency):
        """Returns all the names of the available menu items"""
        selection = 1
        menu_table = PrettyTable()
        menu_table.field_names = ["Name", "Cost", "Selection"]
        items = []
        for item in self.menu:
            items.append([item.name, f"{currency}{item.cost}", selection])
            selection += 1
        menu_table.add_rows(items)
        return menu_table

    def select_drink(self, selected):
        return self.menu[selected-1].name

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item


