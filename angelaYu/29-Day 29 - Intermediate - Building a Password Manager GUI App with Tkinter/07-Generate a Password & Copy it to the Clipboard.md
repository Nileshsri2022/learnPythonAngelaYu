# Generate a Password & Copy it to the Clipboard

---

### 1. Generating

Day 5's generator, refactored into the app (random order = the "hard level"):

```python
import random

def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
               's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
               'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
```

* **Comprehensions** (Day 26) build each character group in one line.
* `"".join(list)` glues characters into a string.
* `insert(0, password)` puts it straight into the password field.

---

### 2. Copy to Clipboard

```python
window.clipboard_clear()
window.clipboard_append(password)
```

The generated password is now pasteable anywhere — Ctrl+V into the site's signup form.

---

### Summary Checklist

1. Random lengths + shuffle = strong passwords (Day 5, upgraded).
2. `"".join()` assembles; `insert(0, ...)` displays.
3. `clipboard_clear()` + `clipboard_append()` = copy button.
4. Runnable version: [`main.py`](main.py) (needs the course's `logo.png`)
