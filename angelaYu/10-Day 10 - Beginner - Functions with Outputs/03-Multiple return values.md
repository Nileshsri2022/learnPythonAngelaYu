Here is a structured breakdown of everything covered in this lesson on multiple return values.

---

### 1. More Than One `return` Statement

A function can have several `return`s in different branches — but **only one ever runs**,
because the first `return` executed ends the function:

```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."   # early exit
    return f"{f_name.title()} {l_name.title()}"     # normal path
```

This is the standard pattern for **validating input**: bail out early with a message, or
proceed to the main logic.

---

### 2. Returning Several Values at Once

Python functions can return **multiple values** as a tuple, unpacked on arrival:

```python
def get_coordinates():
    x = 10
    y = 20
    return x, y

px, py = get_coordinates()   # px = 10, py = 20
```

---

### 3. Days of the Week Exercise

```python
def days_in_month(month, year):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]
```

* Early `return` handles the invalid case.
* The final `return` answers the normal case.

---

### Summary Checklist

1. Multiple `return`s = multiple exit points; the first one hit wins.
2. Early return is the classic validation pattern.
3. `return a, b` returns a tuple; `x, y = f()` unpacks it.
