Here is a structured breakdown of rebuilding the Coffee Machine in OOP.

---

### 1. From Functions to Objects

Day 15's coffee machine was functions + dictionary state. The OOP redesign bundles the
state and behaviour into a **`CoffeeMaker`**, **`Menu`** and **`MenuItem`** class
(provided as starting files in the course):

* `CoffeeMaker` — owns `resources`; exposes `report()` and `is_resource_sufficient(drink)`
  and `make_coffee()`.
* `Menu` — owns the drink list; exposes `get_items()` and `find_drink(order_name)`.
* `MenuItem` — one drink: `name`, `cost`, `ingredients`.

---

### 2. Why This Is Better

* **State is encapsulated** — only the `CoffeeMaker` touches `resources`.
* The main loop reads like the real world:

```python
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
```

Compare that with Day 15's loop — the *what* is now separated from the *how*.

---

### Summary Checklist

1. Objects own their data; the main loop just coordinates them.
2. Class boundaries = real-world parts of the machine (maker, menu, money box).
3. The top-level code becomes a readable story.
