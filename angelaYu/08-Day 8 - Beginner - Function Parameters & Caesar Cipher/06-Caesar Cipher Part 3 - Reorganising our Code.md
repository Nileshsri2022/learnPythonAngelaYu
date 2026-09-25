Here is a structured breakdown of Caesar Cipher Part 3 — reorganising the code.

---

### 1. The Three TODOs

1. **Import and print the logo** from `art.py` — your own file as a module (Day 4/7 skill).
2. **Handle non-letters**: numbers, spaces and symbols should pass through *unchanged*
   instead of crashing `.index()`.
3. **Merge** `encrypt()` and `decrypt()` into one `caesar()` function — *refactoring*.

---

### 2. Merging the Two Functions

The only difference was `+` vs `-`. Fold the direction into the shift:

```python
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1          # backwards for decode
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")
```

---

### 3. Passing Through Symbols

Skip anything that isn't in the alphabet:

```python
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char       # keep spaces, numbers, symbols as-is
```

---

### 4. Full Runnable Solution

```python
import caesar_art   # or: from art import logo

print(caesar_art.logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
```

> **Tip:** `shift % 26` also fixes shifts larger than 26 — the user can type `200`
> and the maths still works. A `while` loop around the program lets users encode
> repeatedly without restarting.

---

### Summary Checklist

1. Refactoring = restructuring code without changing behaviour — here, merging
   two near-identical functions.
2. `shift_amount *= -1` makes one function serve both directions.
3. Non-alphabet characters pass through with an `if char in alphabet` check.
4. Runnable version: [`caesar_cipher.py`](caesar_cipher.py)
