# Day 2 Project- Tip Calculator

---

### 1. What the Program Does

```text
Welcome to the tip calculator!
What was the total bill? 124.56
What percentage tip would you like to give? 12
How many people to split the bill? 7
Each person should pay: $19.93
```

---

### 2. The Maths Behind It

For a $150 bill with a 12% tip:

1. `12% of 150` → `150 * 12 / 100` = **18**
2. Add the tip to the bill → `150 + 18` = **168**
3. Shorthand: `150 * 1.12` (the `1` is the bill, the `.12` is the tip)

Then divide by the number of people and **round to 2 decimal places**.

> **Note:** `150 * 1.12` may produce `168.00000000000003` — that's just how
> floating-point numbers work in every language. `round()` cleans it up for display.

---

### 3. Building It Step by Step

**Step 1 — Greeting and inputs** (convert immediately — `input()` gives strings):

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
```

**Step 2 — Calculate** the tip, total and share per person:

```python
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
```

**Step 3 — Output** with an f-String:

```python
print(f"Each person should pay: ${final_amount}")
```

---

### 4. Full Solution

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip / 100)
final_amount = round(total_bill / people, 2)

print(f"Each person should pay: ${final_amount}")
```

> **Tip:** If your answer looks like `$19.9` instead of `$19.93`, format the float
> with an f-String: `f"${final_amount:.2f}"`.

---

### Summary Checklist

1. **Convert on capture:** `float(input(...))` for the bill, `int(input(...))` for counts.
2. Percentage maths: `bill * (1 + tip / 100)`.
3. `round(x, 2)` for money; `:.2f` in f-Strings forces two decimals.
4. Runnable version: [`tip_calculator.py`](tip_calculator.py)
