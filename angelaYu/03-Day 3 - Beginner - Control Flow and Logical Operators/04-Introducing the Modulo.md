# Introducing the Modulo

---

### 1. What is the Modulo Operator?

The **modulo** `%` is a binary operator (it sits between two numbers) that gives the
**remainder after division**:

```python
print(10 % 5)   # 0  — 5 divides into 10 exactly twice, no remainder
print(10 % 3)   # 1  — 10 / 3 is 3.33…, i.e. 3 remainder 1
```

---

### 2. Why It's Useful: Odd vs. Even

An even number always divides cleanly by 2, so its modulo is `0`:

```python
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

* `12 % 2` → `0` → **even**
* `7 % 2` → `1` → **odd**

> **Note:** `number % 2 == 0` uses `==` (comparison), while `%` does the maths.
> Combining an operator and a comparison like this is a very common Python idiom.

---

### 3. Other Uses to Remember

* **Divisibility checks** — `year % 4 == 0` (part of leap-year logic later in the course).
* **Cycling through values** — `i % 3` gives `0, 1, 2, 0, 1, 2, …` as `i` increases.

---

### Summary Checklist

1. `%` returns the **remainder** of a division.
2. `n % 2 == 0` is the standard **even-number** test.
3. Modulo works on integers and is your go-to for divisibility questions.
