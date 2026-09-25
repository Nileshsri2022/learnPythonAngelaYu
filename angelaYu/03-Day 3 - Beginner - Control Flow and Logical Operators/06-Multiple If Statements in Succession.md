Here is a structured breakdown of everything covered in this lesson on multiple `if` statements in succession.

---

### 1. The Problem: Independent Conditions

`if`/`elif`/`else` picks **one** branch. But some things are **independent** of the ticket
price — like the rollercoaster photo. Whatever ticket the rider bought, they can pay an
extra **$3** for a photo. We need to check another condition **even after** the price was
already decided — that requires a second, separate `if` statement.

---

### 2. Multiple `if`s in Succession

```python
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

wants_photo = input("Do you want a photo taken? Y or N. ")
if wants_photo == "Y":
    bill += 3   # add $3 no matter which ticket was bought

print(f"Your final bill is ${bill}")
```

* The first `if`/`elif`/`else` decides the **ticket price** (exactly one branch).
* The second `if` decides the **photo** — checked **always**, independently.

---

### 3. The Shorthand: `+=`

`bill += 3` is exactly `bill = bill + 3` — add to the existing value in place.

---

### Summary Checklist

1. Use **separate `if` statements** when conditions are independent of each other.
2. `if`/`elif`/`else` = exactly one branch; multiple `if`s = each True branch runs.
3. `+=` adds to a variable in place.
