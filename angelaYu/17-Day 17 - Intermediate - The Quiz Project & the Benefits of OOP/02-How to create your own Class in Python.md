# How to create your own Class in Python

---

### 1. The `class` Keyword

Creating your own class is the same syntax you've *used* since Day 16:

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0          # a default attribute
```

* Class names in **PascalCase**.
* `__init__` runs automatically when an object is constructed.

---

### 2. Constructing and Using It

```python
user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.followers += 1          # modify an attribute
print(user_1.username)         # angela
```

Each object carries its **own** copies of the attributes — two users, two independent
follower counts.

---

### Summary Checklist

1. `class Name:` + `__init__(self, ...)` = your own blueprint.
2. Every attribute assigned in `__init__` becomes per-object state.
3. Defaults (`self.followers = 0`) give new objects sensible starting state.
