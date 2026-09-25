Here is a structured breakdown of everything covered in this lesson on number manipulation and f-Strings.

---

### 1. Flooring vs. Rounding

Given a long decimal like a BMI of `30.8539…`, there are two ways to trim it:

* **`int()` floors** — chops off everything after the decimal point:

```python
bmi = 30.8539
print(int(bmi))    # 30  (floored — always down)
```

* **`round()` rounds** — to the nearest whole number, mathematically:

```python
print(round(bmi))       # 31  (0.5 and above rounds up)
print(round(3.3))       # 3
print(round(3.9))       # 4
```

`round()` also takes a **second argument** — how many decimal places you want:

```python
print(round(bmi, 2))    # 30.85
```

---

### 2. The Assignment Operators (`+=`, `-=`, …)

Shortcuts for updating a variable in place:

```python
score = 0
score += 1    # same as: score = score + 1
score -= 1    # same as: score = score - 1
score /= 2    # same as: score = score / 2
```

---

### 3. f-Strings

An **f-String** embeds values directly inside a string — prefix the string with `f` and
wrap variables in `{curly braces}`:

```python
name = "Angela"
age = 30
print(f"My name is {name} and I am {age} years old.")
# My name is Angela and I am 30 years old.
```

* No more `+` concatenation, no `str()` conversions, no space headaches.
* It even works with **expressions** and keeps types intact:

```python
print(f"Your bill is {round(124.56 * 1.12, 2)}")
```

> **Note:** f-Strings are the modern, preferred way to format output in Python —
> use them instead of concatenation wherever you mix text and variables.

---

### Summary Checklist

1. `int()` **floors**; `round()` rounds — optionally to N decimal places with `round(x, n)`.
2. `+=`, `-=`, `*=`, `/=` update variables in place.
3. **f-Strings**: `f"Hello {name}"` — mix any variables into text cleanly.
