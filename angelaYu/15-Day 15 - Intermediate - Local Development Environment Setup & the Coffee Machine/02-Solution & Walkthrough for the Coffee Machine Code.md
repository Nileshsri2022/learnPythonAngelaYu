# Solution & Walkthrough for the Coffee Machine Code

---

### 1. The Data Structures

Menu and machine state as dictionaries (Day 9 nesting):

```python
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
```

---

### 2. The Helper Functions

```python
def is_resource_sufficient(order_ingredients):
    """Return True if the machine can make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment accepted; refund if insufficient."""
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients and serve."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
```

---

### 3. The Main Loop

```python
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                resources["money"] += drink["cost"]
                make_coffee(choice, drink["ingredients"])
```

---

### Summary Checklist

1. `MENU` + `resources` dicts hold all state; functions each do one job.
2. Order of checks: resources → payment → make.
3. The `while` loop keeps the machine alive until `off`.
4. Runnable version: [`coffee_machine.py`](coffee_machine.py)
