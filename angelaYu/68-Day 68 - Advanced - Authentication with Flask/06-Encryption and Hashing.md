# Encryption and Hashing

---

### 1. Level 0: Plain Text

```text
email: angela@example.com   password: qwerty123
```

Anyone who sees the database sees every password. `plaintextoffenders.com` collects real
examples of companies emailing users their own password in plain text — that only works if
the password is stored recoverably, i.e. badly.

---

### 2. Level 1: Encryption (Reversible)

**Encryption** scrambles a message so only someone with the **key** can unscramble it.

* The **Caesar cipher** — shift every letter by a fixed number (hello → khoor with shift 3).
* The **Enigma machine** — a much stronger version of the same idea, broken at Bletchley
  Park by Alan Turing and colleagues.

The flaw for passwords: encryption is *reversible*. Anyone who steals the key (or the
server) can decrypt everything.

```text
password  +  key  →  ciphertext            (and back again)
```

---

### 3. Level 2: Hashing (One-Way)

A **hash function** turns any input into a fixed-length digest — and cannot be run
backwards.

The classic illustration: multiplying 13 × 29 = 377 is instant; finding the factors of 377
takes trial and error. Hash functions work the same way, with far more complexity.

```text
password  →  hash function  →  digest        ✅ easy
digest    →  hash function  →  password      ❌ effectively impossible
```

Login becomes a comparison:

```python
hash(stored_password) == hash(typed_password)   # same input → same digest
```

At no point does the server know the user's password — the only person who does is the user.

> **Note:** "Impossible" means "would take longer than the age of the universe with current
> hardware", which is good enough. Never build your own hash function — use a vetted one.

---

### 4. Side by Side

| | Encryption | Hashing |
|--|-----------|---------|
| Direction | two-way | one-way |
| Needs a key | yes | no |
| Use for | data you must read later (messages, files) | passwords |
| If stolen | everything decrypts | attacker must crack each password |

---

### 5. Where This Leaves Us

Hashing is a big step up, but plain hashes have weaknesses: identical passwords produce
identical hashes, and pre-computed tables (rainbow tables) crack common passwords fast.
Next: **salting**, and then a slow-by-design algorithm like bcrypt.

---

### Summary Checklist

1. Plain text = the worst option; a leak reveals everything.
2. Encryption is reversible — wrong tool for passwords.
3. Hashing is one-way: store the digest, compare digests at login.
4. Use established algorithms; never roll your own.
5. Next: salt + slow hashing to defeat pre-computed attacks.
