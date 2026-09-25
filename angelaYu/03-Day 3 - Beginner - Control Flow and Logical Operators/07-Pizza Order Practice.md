# Pizza Order Practice

---

### 1. The Task

Build a **Python Pizza Delivery** program that calculates the bill:

| Item | Price |
|------|-------|
| Small pizza (S) | $15 |
| Medium pizza (M) | $20 |
| Large pizza (L) | $25 |
| Pepperoni (S) | +$2 |
| Pepperoni (M or L) | +$3 |
| Extra cheese | +$1 |

Example: **L** + pepperoni + no extra cheese → `Your final bill is: $28`.

---

### 2. Thinking It Through

* One **`if`/`elif`/`else`** for the size → sets the base bill (only one size is chosen).
* A **nested `if`/`else`** inside each size branch for pepperoni — its price *depends on the size*.
* One **separate `if`** for extra cheese — it's independent of size.

---

### 3. Solution

```python
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
```

---

### Summary Checklist

1. Size choice → one `if`/`elif`/`else` (exclusive).
2. Pepperoni → nested, because the surcharge **depends on size**.
3. Extra cheese → separate `if`, because it is **independent**.
4. Runnable version: [`pizza_order.py`](pizza_order.py)
