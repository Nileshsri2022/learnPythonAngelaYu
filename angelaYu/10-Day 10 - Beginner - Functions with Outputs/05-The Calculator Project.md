# The Calculator Project

---

### 1. What the Program Does

```text
What's the first number?: 5
Pick an operation: + - * /   →  *
What's the next number?: 3
5.0 * 3.0 = 15.0
Type 'y' to continue calculating with 15.0, or 'n' to start a new calculation:
```

Results **chain**: the answer becomes the first operand of the next calculation until the
user restarts.

---

### 2. Key Design Ideas

* **A dictionary of functions** — store the operations as `symbol → function` pairs, which
  removes a giant if/elif chain:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
```

* Each operation is a tiny function that **returns** (not prints!) its result.
* A `while` loop keeps the calculator running and feeds results back in.

---

### 3. Solution

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, "
                       "or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            calculator()          # recursion: start a fresh calculation

calculator()
```

Notice `operations[operation_symbol](num1, num2)` — the dictionary returns the *function*,
and the second parentheses call it.

---

### Summary Checklist

1. Operation functions **return** their result — that's what makes chaining possible.
2. A dict of functions replaces branching logic with a lookup.
3. `dict[key](args)` is how you call a function stored in a dictionary.
4. Runnable version: [`calculator.py`](calculator.py)
