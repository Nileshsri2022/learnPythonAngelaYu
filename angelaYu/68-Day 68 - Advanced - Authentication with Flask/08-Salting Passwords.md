Here is a structured breakdown of this lesson on salting passwords.

---

### 1. What Salting Is

Before hashing, generate a **random string (the salt)** and combine it with the password:

```
hash(password + salt)  →  stored digest
salt                  →  stored next to the digest (it's not secret)
```

Each user gets a *different* salt, so identical passwords produce different hashes.
The salt is not a key — it can sit in plain view in the database.

---

### 2. Why It Works

Without salt:

```
angela: qwerty  →  5f4dcc3b5aa765d61d8327deb882cf99
emily:  qwerty  →  5f4dcc3b5aa765d61d8327deb882cf99     ← identical
```

With salt:

```
angela: hash("qwerty" + "x7Kd2…")  →  a1b2c3…
emily:  hash("qwerty" + "9pQz4…")  →  7f8e9d…          ← different
```

* A rainbow table of `qwerty` is now useless — the attacker would need a table for every
  possible salt.
* One cracked password no longer reveals that others share it.

---

### 3. Logging In With Salt

The server never stores the original password:

```python
# registration
salt = generate_random_salt()
stored_hash = hash(password + salt)

# login (user types the password again)
if hash(typed_password + stored_salt) == stored_hash:
    # authenticated
```

The same salt goes into the same calculation, so the digests match — while the password
itself stays unknown to the server forever.

---

### 4. Salting Isn't Enough on Its Own

Even with salts, fast algorithms (MD5) remain a problem:

| Algorithm | Hashes per second (2019-era GPU) |
|-----------|----------------------------------|
| MD5 | ~20,000,000,000 |
| bcrypt | ~17,000 |

A fully salted rainbow table that takes ~3 seconds to build for MD5 takes roughly **8
months** with bcrypt. Hackers move on to easier targets.

**Salt rounds:** bcrypt re-runs its internal loop many times, making each hash deliberately
expensive. More rounds = slower to verify (milliseconds for you) and dramatically slower to
crack (months for them). Libraries pick a sane default and raise it as hardware improves.

---

### 5. The Takeaway

| Layer | Stops |
|-------|-------|
| Hashing | storing the actual password |
| Salting | rainbow tables, identical-hash leaks |
| Slow algorithm (bcrypt) + rounds | brute force at scale |

Never implement this yourself — use `werkzeug.security` (next lesson).

---

### Summary Checklist

1. Salt = random per-user string, stored with the hash, not secret.
2. Identical passwords then produce different digests.
3. Login re-computes `hash(typed + stored_salt)` and compares.
4. Salting alone is insufficient against fast GPUs — pair it with bcrypt and salt rounds.
5. Use a library; hand-rolled crypto is how breaches happen.
