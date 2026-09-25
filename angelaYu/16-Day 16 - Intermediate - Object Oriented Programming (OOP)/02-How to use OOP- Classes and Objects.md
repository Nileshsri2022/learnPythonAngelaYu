Here is a structured breakdown of this lesson on using OOP: classes and objects.

---

### 1. Defining a Class

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color          # attribute
        self.mileage = mileage      # attribute

    def drive(self, km):            # method
        self.mileage += km
        print(f"Drove {km}km, total {self.mileage}")
```

* `class Name:` — convention: **PascalCase** class names.
* `__init__` — the **initialiser** that runs when an object is created; `self` is the
  object being constructed.
* Attributes live on `self`; methods are functions defined inside the class that take
  `self` as the first parameter.

---

### 2. Creating Objects

```python
my_car = Car("red", 0)
your_car = Car("blue", 100)

my_car.drive(50)      # Drove 50km, total 50
your_car.drive(50)    # Drove 50km, total 150
```

Each object keeps its **own** attributes — `drive()` on one doesn't affect the other.
The method's `self` is *whichever object it was called on*.

---

### Summary Checklist

1. `class` + `__init__(self, ...)` define the blueprint.
2. `Name(args)` constructs an object; `__init__` stores its state on `self`.
3. `self` means "this particular object".
