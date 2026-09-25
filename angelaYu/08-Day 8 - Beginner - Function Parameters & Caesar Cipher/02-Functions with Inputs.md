# Functions with Inputs

---

### 1. Parameters vs. Arguments

A function becomes far more useful when it can receive **inputs**:

```python
def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet("Angela")
```

* **Parameter** — the name in the function definition: `name`.
* **Argument** — the actual value you pass in the call: `"Angela"`.

Think of the parameter as a *placeholder* that gets filled with the argument's value.

---

### 2. How the Data Flows

1. `greet("Angela")` is called.
2. Python jumps to the definition and assigns `name = "Angela"`.
3. The indented body runs *with that value substituted everywhere `name` appears*.

> **Note:** The variable `name` exists **only inside** the function — this is your
> first taste of scope (explored fully on Day 12).

---

### 3. Literals vs. Variables as Arguments

You can pass values directly, or pass variables:

```python
user = "Jack"
greet(user)      # the variable's value is what gets passed
```

---

### Summary Checklist

1. Define inputs in the parentheses: `def greet(name):`.
2. Supply values in the call: `greet("Angela")`.
3. Parameter = placeholder name; argument = real value.
4. One function + different arguments = many different outputs.
