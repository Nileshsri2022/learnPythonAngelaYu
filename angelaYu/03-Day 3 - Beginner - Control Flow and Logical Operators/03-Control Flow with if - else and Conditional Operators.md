# Control Flow with if - else and Conditional Operators

---

### 1. Why Conditionals Exist

A bathtub doesn't overflow because of its **overflow drain**: *when the water level goes above
80 cm, drain; otherwise keep filling.* That is exactly an **`if` / `else` statement** — do A
if a condition is true, otherwise do B.

---

### 2. The Syntax

```python
water_level = 50

if water_level > 80:
    print("Drain the water")
else:
    print("Continue filling")
```

* The `if` keyword, then the **condition**, then a **colon**.
* The **indented block** underneath runs only when the condition is `True`.
* The `else:` block runs when the condition is `False`.

> **Warning:** Indentation defines what is *inside* the `if` — same as with loops.
> Everything indented after the colon belongs to that branch.

---

### 3. Comparison (Conditional) Operators

| Operator | Meaning |
|----------|---------|
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |
| `==` | equal to (**two** signs — one `=` is assignment!) |
| `!=` | not equal to |

Each comparison evaluates to a **Boolean** — `True` or `False`:

```python
print(90 > 80)   # True
print(50 > 80)   # False
```

---

### 4. Practice: The Rollercoaster Ticket Booth

Check the rider's height before selling a ticket:

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

`input()` returns a string, so we **convert with `int()`** before comparing.

---

### Summary Checklist

1. `if condition:` do something when `True`, `else:` when `False`.
2. Comparisons produce Booleans: `>`, `<`, `>=`, `<=`, `==`, `!=`.
3. `=` assigns; `==` compares — don't mix them up.
4. Indentation decides which lines belong to the branch.
