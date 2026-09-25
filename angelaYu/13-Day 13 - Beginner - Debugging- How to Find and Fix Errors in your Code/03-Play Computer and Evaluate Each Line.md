# Play Computer and Evaluate Each Line

---

### 1. Tip #3: Play Computer

Pretend *you* are the computer: read the code line by line, and **evaluate every variable**
by hand, exactly as Python would — top to bottom, inside the loops, keeping a table of
values:

```python
def sum_odd_numbers(numbers):
    total = 0                    # total = 0
    for number in numbers:       # number takes 1, 2, 3, 4...
        if number % 2 != 0:      # odd numbers only
            total += number
    return total

print(sum_odd_numbers([1, 2, 3, 4, 5]))   # expect 9
```

Playing computer with `[1, 2, 3, 4, 5]`:

| step | number | odd? | total |
|------|--------|------|-------|
| 1 | 1 | yes | 1 |
| 2 | 2 | no | 1 |
| 3 | 3 | yes | 4 |
| 4 | 4 | no | 4 |
| 5 | 5 | yes | 9 ✅ |

If your hand-trace and the program's output disagree, the *exact line* where they diverge
is your bug.

---

### 2. Evaluate Each Line Honestly

Don't read what you *meant* to write — read what's **actually there** (including the
operator you typed wrong, the indentation level, the variable that's never updated).

---

### Summary Checklist

1. Hand-trace the code with a variable table.
2. The divergence point between expectation and reality locates the bug.
3. Trace the code as written, not as intended.
