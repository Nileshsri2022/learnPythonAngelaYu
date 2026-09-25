"""Day 16 project: the Coffee Machine rebuilt with classes (self-contained)."""


class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0),
        ]

    def get_items(self):
        """Return the drink names joined by slashes."""
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        """Return the MenuItem matching order_name, or None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None


class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        for name, amount in self.resources.items():
            unit = "g" if name == "coffee" else "ml"
            print(f"{name.capitalize()}: {amount}{unit}")

    def is_resource_sufficient(self, drink):
        """Return True when every ingredient is in stock."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕. Enjoy!")


class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def make_payment(self, cost):
        """Prompt for coins; return True if the payment covers the cost."""
        print("Please insert coins.")
        total = 0
        for coin in self.COIN_VALUES:
            total += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        if total >= cost:
            change = round(total - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        print("Sorry that's not enough money. Money refunded.")
        return False


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
