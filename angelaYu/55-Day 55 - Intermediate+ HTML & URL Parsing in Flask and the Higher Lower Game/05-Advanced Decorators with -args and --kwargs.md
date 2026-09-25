Here is a structured breakdown of this lesson on advanced decorators with `*args` and `**kwargs`.

---

### 1. The Problem

Yesterday's decorators wrapped **no-argument** functions:

```python
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function
```

Decorate a function that takes inputs and it breaks:

```
TypeError: wrapper_function() takes 0 positional arguments but 1 was given
```

The wrapper doesn't accept the arguments the original function expects.

---

### 2. The Setup: A Logged-In Check

```python
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


user = User("Angela")
create_blog_post(user)
```

We want a decorator that only allows the call when `user.is_logged_in` is `True`.

---

### 3. The Fix: Accept Anything, Forward Everything

```python
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):          # accept any arguments
        if args[0].is_logged_in:           # args[0] is the `user` argument
            function(*args, **kwargs)      # hand them to the real function
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
```

| Piece | Meaning |
|-------|---------|
| `*args` | all **positional** arguments, as a tuple |
| `**kwargs` | all **keyword** arguments, as a dictionary |
| `args[0]` | the first positional argument — here, the `user` object |
| `function(*args, **kwargs)` | pass everything through unchanged |

```python
user = User("Angela")
create_blog_post(user)         # nothing printed - not logged in

user.is_logged_in = True
create_blog_post(user)         # "This is Angela's new blog post."
```

---

### 4. Why `args[0]` Is a Bit Sloppy

Indexing into `args` assumes the user is always the first positional argument. More robust
names the parameter explicitly:

```python
def requires_login(function):
    @wraps(function)
    def wrapper(user, *args, **kwargs):
        if user.is_logged_in:
            return function(user, *args, **kwargs)
    return wrapper
```

Same behaviour, clearer contract, and it breaks loudly for a wrong call instead of
silently reading the wrong object.

---

### 5. Real-World Value

This is the shape of real authorisation decorators — Flask's `@login_required`, Django's
`@permission_required`, API key checks. The pattern:

```
inspect the arguments → make a decision → maybe call the original function
```

Bonus: if you want the decorator itself to take options (`@retry(times=3)`), you add a
**third** layer of nesting — a function that returns the decorator.

---

### Summary Checklist

1. Wrappers for functions with inputs need `*args, **kwargs`.
2. `args[0]` reaches the first positional argument; `kwargs["name"]` a keyword one.
3. Forward everything: `function(*args, **kwargs)`.
4. This is how auth/retry/permission decorators work in real frameworks.
5. Name parameters explicitly when you know them — it's clearer than `args[0]`.
