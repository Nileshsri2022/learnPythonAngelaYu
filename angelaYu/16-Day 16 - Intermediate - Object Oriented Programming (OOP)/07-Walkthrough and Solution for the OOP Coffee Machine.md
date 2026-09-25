Here is a structured walkthrough of the OOP Coffee Machine solution.

---

### 1. The Classes in Brief

```python
class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    def get_items(self):
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        for name, amount in self.resources.items():
            unit = "ml" if name != "coffee" else "g"
            print(f"{name.capitalize()}: {amount}{unit}")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕. Enjoy!")
```

---

### 2. Wiring It Together

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
```

(A `MoneyMachine` class with `make_payment(cost)` completes the course version.)

---

### Summary Checklist

1. Each class owns one responsibility — menu knowledge, resources, money.
2. `find_drink` returns a `MenuItem` object the maker consumes.
3. Runnable self-contained version: [`oop_coffee_machine.py`](oop_coffee_machine.py)
