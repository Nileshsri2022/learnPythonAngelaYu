Here is a structured breakdown of Caesar Cipher Part 1 — encryption.

---

### 1. How the Cipher Works

Line the alphabet up against a shifted copy of itself. With a **shift of 3**:

```
Plain:  a b c d e f g ...
Cipher: d e f g h i j ...
```

`hello` with shift 5 becomes `mjqqt` — every letter moved 5 places forward.

---

### 2. Shifting with Python Lists

The trick is list **indexing** — find the letter's position, add the shift, and wrap with
modulo:

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:               # past 'z'? wrap around
            new_position -= 26
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)
```

* `alphabet.index(letter)` → the letter's position (0–25).
* `new_position` may overshoot the end — subtracting 26 wraps `z + 1` back to `a`.

> **Tip:** The wrap-around is exactly the modulo idea from Day 3:
> `new_position = (position + shift_amount) % 26` does the same in one line.

---

### Summary Checklist

1. Encryption = **shift forward** by the shift amount.
2. `.index()` finds a letter's position; list indexing rewrites it.
3. Wrap past `z` with `% 26` (or `- 26`).
4. Keyword arguments (`plain_text=text`) make the call read clearly.
