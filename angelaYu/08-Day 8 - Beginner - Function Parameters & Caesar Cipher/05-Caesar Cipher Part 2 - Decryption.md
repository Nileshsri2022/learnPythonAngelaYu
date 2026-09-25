# Caesar Cipher Part 2 - Decryption

---

### 1. The Reverse Operation

Decryption shifts **backwards**: `G` with shift 3 came from `D`. So the decrypt function is
nearly identical to `encrypt` — it just **subtracts** the shift:

```python
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:               # before 'a'? wrap around
            new_position += 26
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
```

* Same index → shift → wrap pattern as encryption.
* The wrap goes the other way: `a - 1` must become `z` (`+26`).

**Ask which direction the user wants** and call the right function:

```python
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
```

---

### Summary Checklist

1. Decryption = encryption with the shift **negated**.
2. Wrap under `a` with `% 26` / `+ 26`.
3. An `if`/`elif` on the direction picks the function to call.
4. Two functions that differ by one sign — a strong hint they should be merged
   (that's exactly what Part 3 does).
