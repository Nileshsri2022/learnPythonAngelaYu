Here is a structured breakdown of the Day 5 final project — the PyPassword Generator.

---

### 1. What the Program Does

```
Welcome to the PyPassword Generator!
How many letters would you like in your password? 14
How many symbols would you like? 3
How many numbers would you like? 4
```

* **Easy Level** — output in sequence: `llllllllllllllssssnnnn` (letters, then symbols, then numbers).
* **Hard Level** — the same characters **shuffled into a random order** every run.

---

### 2. Easy Level — Building Blocks

```python
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Here is your password: {password}")
```

Each loop runs `range(1, n + 1)` times and appends one **random** character with
`random.choice(list)`.

---

### 3. Hard Level — Random Order

Collect the characters in a **list**, then shuffle the list and join it:

```python
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)          # shuffle in place

password = ""
for char in password_list:
    password += char

print(f"Your hard level password is: {password}")
```

`random.shuffle()` reorders a list **in place** — the same technique reappears when
shuffling decks of cards.

---

### Summary Checklist

1. `range(1, n + 1)` loops exactly `n` times.
2. `random.choice(list)` picks one random element.
3. Hard level: **build a list → `random.shuffle()` → join** into a string.
4. Runnable version: [`password_generator.py`](password_generator.py)
