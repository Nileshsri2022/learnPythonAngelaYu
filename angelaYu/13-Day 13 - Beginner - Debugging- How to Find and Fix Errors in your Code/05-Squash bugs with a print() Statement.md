# Squash bugs with a print() Statement

---

### 1. Tip #5: `print()` Is Your Best Friend

Sprinkle `print()` at key points to see what the program *actually* knows at that moment —
variable values, types, loop passes:

```python
def calculate_mean(numbers):
    total = 0
    for number in numbers:
        total += number
        print(f"DEBUG: number={number}, total={total}")   # watch it accumulate
    mean = total / len(numbers)
    print(f"DEBUG: mean={mean}")
    return mean
```

Effective print-debugging checks **three things**:

1. **Value** — is the variable what you think it is?
2. **Type** — is it a string when you expected an int? (`print(type(x))`)
3. **Flow** — did execution even reach this line? (`print("got here")`)

---

### 2. The Classic Bug It Catches

```python
age = input("How old are you? ")   # input() returns a STRING
print(age + 1)                     # TypeError — print(type(age)) reveals it instantly
```

> **Warning:** After fixing, **remove your debug prints** — or mark them clearly
> (`# DEBUG`) so they're easy to strip later.

---

### Summary Checklist

1. Print values, types and progress markers at suspect points.
2. Compare printed reality against your mental trace.
3. Clean up debug prints once the bug is gone.
