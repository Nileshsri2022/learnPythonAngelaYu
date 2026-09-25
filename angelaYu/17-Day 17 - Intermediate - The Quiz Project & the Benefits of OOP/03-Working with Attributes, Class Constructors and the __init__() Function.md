# Working with Attributes, Class Constructors and the __init__() Function

---

### 1. The Constructor

`__init__()` is the **constructor** — Python calls it automatically during
`ClassName(arguments)`. Its job: receive the initial data and attach it to the object:

```python
class Car:
    def __init__(self, seats):
        self.seats = seats        # attribute created FROM the parameter
```

* The **parameter** `seats` exists only during construction.
* The **attribute** `self.seats` lives on the object forever after.

---

### 2. Accessing Attributes

```python
my_car = Car(5)
print(my_car.seats)     # 5 — attribute access via dot notation
```

`my_car = Car(5)` is shorthand for: *create an empty object, call `Car.__init__(my_car, 5)`* —
`self` **is** `my_car`.

---

### 3. Attributes vs. Parameters — the Common Confusion

```python
def __init__(self, user_id, username):
    self.id = user_id          # attribute name ≠ parameter name: fine!
    self.username = username   # or the same name: also fine — self. disambiguates
```

Inside `__init__`, anything starting with `self.` belongs to the object; anything else is
an ordinary local variable.

---

### Summary Checklist

1. `__init__` = automatic initialiser called on construction.
2. Parameters are construction-time; `self.x` attributes are the object's memory.
3. `obj.attribute` reads that object's stored state.
