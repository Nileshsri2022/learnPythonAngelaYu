# Day 10 Goals- what we will make by the end of the day

---

### 1. Skills Covered on Day 10

* **Functions with outputs** — the `return` keyword
* **Multiple return values** and early exits
* **Docstrings** — documenting your own functions
* Dictionary of functions (storing functions as values)

This completes the three "flavours" of functions: plain → with inputs → **with outputs**.

---

### 2. The End-of-Day Project: Calculator

```text
What's the first number?: 5
+
+
Pick an operation: *
What's the next number?: 3
5.0 * 3.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation:
```

The result feeds the next calculation until the user starts fresh — all orchestrated by
functions that **return** their results.

---

### Summary Checklist

1. `return` sends a value back to wherever the function was called.
2. Functions can return multiple values and decide early.
3. Docstrings make your functions as discoverable as Python's built-ins.
4. The calculator chains results through returned values.
