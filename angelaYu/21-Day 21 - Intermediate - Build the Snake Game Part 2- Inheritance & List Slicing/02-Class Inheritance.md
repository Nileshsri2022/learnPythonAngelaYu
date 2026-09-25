# Class Inheritance

---

### 1. The Robot Chef Analogy

You built a **RobotChef** that can `bake()`, `stir()`, `weigh()`. Now you need a
**PastryChef** — it needs all of that *plus* `make_cake()`. Instead of rewriting the
class, **inherit** from it and add only what's new.

---

### 2. The Syntax

```python
class Animal:                       # base (parent) class
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):                 # derived (child) class
    def __init__(self):
        super().__init__()          # run the parent's setup first

    def swim(self):
        print("moving in water.")

    def breathe(self):              # overriding — extend, don't replace
        super().breathe()
        print("doing this underwater.")
```

```python
nemo = Fish()
nemo.swim()              # moving in water.
nemo.breathe()           # Inhale, exhale. / doing this underwater.
print(nemo.num_eyes)     # 2  — inherited attribute!
```

* `class Child(Parent):` — the inheritance declaration.
* `super().__init__()` — run the parent's constructor before adding child state.
* A child gets **all** attributes and methods for free, and may add or *override* some.

---

### 3. In the Snake Game

`Food`, `Scoreboard` and `Snake` all inherit from Turtle's `Turtle` class — they *are*
turtles with extra behaviour.

---

### Summary Checklist

1. `class Child(Parent):` inherits everything; `super()` chains the parent's setup.
2. Override = redefine a method in the child (optionally calling `super().method()`).
3. Inheritance exists so you modify and extend classes **without rewriting them**.
