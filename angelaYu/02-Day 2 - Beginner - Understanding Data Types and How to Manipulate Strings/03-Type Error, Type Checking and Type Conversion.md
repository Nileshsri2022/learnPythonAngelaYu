# Type Error, Type Checking and Type Conversion

---

### 1. Functions Are Machines

Think of a function as a **machine in a factory**: potatoes go in, chips come out. Feed it
a rock (the wrong input type) and the machine breaks — that's exactly what a **TypeError**
is: `len()` receiving an `int` instead of a string.

---

### 2. Checking a Type with `type()`

Before converting, you can inspect what type a piece of data is:

```python
print(type("abc"))      # <class 'str'>
print(type(123))        # <class 'int'>
num_char = len(input("What is your name? "))
print(type(num_char))   # <class 'int'>
```

> **Tip:** Hover over any function in PyCharm to see which data type it expects,
> and click through to the official docs at docs.python.org.

---

### 3. Converting Types (Type Casting)

Python has three conversion functions named after the types themselves:

```python
print(int("5") + 5)        # 10  — string → int
print(int(3.7))            # 3   — float → int (chops off decimals)
print(float("3.14"))       # 3.14 — string → float
print(str(70) + " days")   # 70 days — number → string
```

Without `str()`, `70 + " days"` is a `TypeError` — Python never guesses whether `70`
should be read as text.

---

### 4. Common Gotcha: Numeric Strings

`input()` **always** returns a string — even if the user types digits:

```python
two_digit_number = input()        # user types "55"
print(type(two_digit_number))     # <class 'str'>
result = int(two_digit_number[0]) + int(two_digit_number[1])   # convert before maths
```

A string can also be subscripted **then** converted: `int("9"[0])` works fine.

---

### Summary Checklist

1. **TypeError** = wrong data type passed to a function.
2. Check types with `type()`; convert with `int()`, `float()`, `str()`.
3. `input()` gives you a **string** — convert it before doing maths.
4. `int()` on a float truncates (floors) the decimal part.
