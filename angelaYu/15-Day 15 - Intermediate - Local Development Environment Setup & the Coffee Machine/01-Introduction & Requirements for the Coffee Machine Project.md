Here is a structured breakdown of the Day 15 project briefing — the Coffee Machine.

---

### 1. The Scenario

You've just been hired — but first, coffee. Your job: program the office coffee machine.
From Day 15 on you work in a **local development environment** (PyCharm + the downloadable
curriculum project) rather than an online IDE.

---

### 2. The Requirements

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.6 in change.
Here is your latte. Enjoy!
```

* **Menu**: `espresso` ($1.50, 50ml water, 18g coffee), `latte` ($2.50, 200ml water,
  150ml milk, 24g coffee), `cappuccino` ($3.00, 250ml water, 100ml milk, 24g coffee).
* The machine tracks **resources** (water, milk, coffee, money) and prints a report
  (`report` command).
* Insufficient resources → *"Sorry, there is not enough water."*
* Coin insert: quarters ($0.25), dimes ($0.10), nickles ($0.05), pennies ($0.01);
  print change if overpaid; refund if insufficient.
* `off` turns the machine off.

---

### Summary Checklist

1. No starter code — requirements only, built fully in your local PyCharm setup.
2. State (resources + money) persists across orders in one run.
3. `report`, `off`, resource checks, change calculation — plan with a flowchart first.
