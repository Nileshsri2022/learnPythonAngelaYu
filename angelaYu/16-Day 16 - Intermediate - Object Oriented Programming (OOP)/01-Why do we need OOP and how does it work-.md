Here is a structured breakdown of this lesson on why we need OOP and how it works.

---

### 1. The Problem OOP Solves

Real programs model real-world things — users, cars, coffee machines — each with
**state** (data) and **behaviour** (actions). Scattered lists and functions get tangled
fast. **Object-Oriented Programming** bundles state + behaviour into **objects**.

---

### 2. The Mental Model

* A **class** is a *blueprint* — it defines what data and actions every instance will have.
* An **object** is a *thing built from that blueprint* — each with its own state.

Analogy: one car blueprint (class); many cars built from it (objects) — each with its own
colour and mileage, all able to *drive* (behaviour).

```python
import turtle
timmy = turtle.Turtle()     # object built from the Turtle blueprint
timmy.color("coral")        # attribute: its state
timmy.forward(100)          # method: its behaviour
```

Everything in Python is an object — lists, strings, even functions have methods you've
been calling all along.

---

### Summary Checklist

1. OOP = organising code into objects that hold **attributes** (data) and **methods** (actions).
2. Class = blueprint; object = one concrete instance.
3. You've used OOP already: `"hi".upper()`, `my_list.append(x)`.
