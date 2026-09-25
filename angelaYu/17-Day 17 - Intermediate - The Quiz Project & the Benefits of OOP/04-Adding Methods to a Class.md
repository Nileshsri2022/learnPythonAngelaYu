Here is a structured breakdown of this lesson on adding methods to a class.

---

### 1. Methods = Functions Inside a Class

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
```

* Methods always take `self` as the first parameter — the object they were called on.
* Methods can touch the object's attributes (`self.following`) **and** other objects'
  attributes (`user.followers`).

---

### 2. Calling Methods

```python
user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.following)   # 1
print(user_2.followers)   # 1
```

The call `user_1.follow(user_2)` passes two objects in: `self` (= `user_1`, implicit) and
`user` (= `user_2`, explicit).

---

### Summary Checklist

1. Methods give a class **behaviour** to match its attributes.
2. `self` is the implicit first argument — provided by the call.
3. Objects interacting through methods is the heart of OOP design.
