Here is a structured breakdown of the Day 8 goals and the project you'll have built by the end of the day.

---

### 1. Skills Covered on Day 8

* **Functions with inputs** — parameters and arguments
* **Positional vs. keyword arguments**
* Applying both to build a real program step by step (encryption → decryption → refactor)

---

### 2. The End-of-Day Project: Caesar Cipher

One of the oldest encryption schemes, used by Julius Caesar for military messages:
**shift each letter of the alphabet by a predetermined amount**.

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here is the encoded result: mjqqt
```

Built in three parts:

1. **Encryption** — shift letters forward
2. **Decryption** — shift letters backward
3. **Refactoring** — merge both into one `caesar()` function + handle symbols/numbers

---

### Summary Checklist

1. Parameters let the *same* function work with *different* data.
2. Positional order matters; keyword arguments don't.
3. You'll combine them into a working **encode/decode** app.
