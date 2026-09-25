Here is a structured breakdown of everything covered in this lesson on nested `if` statements and `elif` statements.

---

### 1. Nested `if` Statements

Sometimes a second condition only matters when the first one **already passed** — e.g. first
check the rider is tall enough, *then* decide adult vs. child price. That is a **nested
`if`**: an `if`/`else` written *inside* another one, indented a further level:

```python
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

* The inner `if/else` only runs when the outer condition is `True`.
* Both conditions must hold to reach the innermost code — and note the **double indentation**.

---

### 2. `elif` — Checking Several Alternatives

`elif` (else-if) adds more branches to the *same* check, e.g. mid-life pricing:

```python
if age < 12:
    print("Please pay $5.")
elif age <= 18:
    print("Please pay $7.")
else:
    print("Please pay $12.")
```

Python tests each condition **top to bottom** and runs the **first** one that is `True`,
skipping the rest.

---

### 3. `if` / `elif` / `else` vs. Multiple `if`s

| Pattern | How many branches run? |
|---------|------------------------|
| `if` / `elif` / `else` | **Exactly one** — the first True branch |
| Several separate `if`s | **Every** branch whose condition is True |

---

### Summary Checklist

1. **Nested `if`** = a second check inside a first check (extra indentation).
2. **`elif`** chains multiple exclusive branches; only the first `True` runs.
3. Indentation level shows which `if` a block belongs to.
