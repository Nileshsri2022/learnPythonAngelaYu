# How to Hack Passwords 101

---

### 1. Why Think Like an Attacker?

Understanding the attacks tells you exactly which defensive measure matters. Breaches are
routine: Adobe (2013), LinkedIn (2012) — millions of leaked password hashes.

---

### 2. How Leaked Hashes Get Cracked

| Attack | How it works | Beaten by |
|--------|--------------|-----------|
| **Brute force** | try every combination | long passwords |
| **Dictionary attack** | try words from a wordlist | non-dictionary passwords |
| **Rainbow table** | pre-computed hash → password lookup table | **salting** |
| **Credential stuffing** | reuse leaked passwords on other sites | unique passwords + rate limits |

Humans pick terrible passwords: short, dictionary words, or `qwerty`, `password123`.

---

### 3. Speed Is the Attacker's Friend

With a fast hash like MD5, a modern GPU computes roughly **20 billion hashes per second**:

| Password space | Time to brute force |
|----------------|--------------------|
| 6 lowercase letters | seconds |
| 8 lowercase letters | minutes to hours |
| Common dictionary word | instant (already in the table) |

If three users share a password, their stored hashes are **identical** — the attacker
cracks one and knows all three.

---

### 4. Demo: The Same Hash, Three Users

```text
angela  →  5f4dcc3b5aa765d61d8327deb882cf99   ← all three rows
tony    →  5f4dcc3b5aa765d61d8327deb882cf99      have the same
emily   →  5f4dcc3b5aa765d61d8327deb882cf99      hash
```

One rainbow-table lookup reveals all three passwords at once. Identical hashes leak
*information about other users* — a design flaw, not just a weakness.

---

### 5. The Defences That Follow

1. **Salt** — random characters added to each password before hashing, stored alongside the
   digest; two users with `qwerty` now have completely different hashes.
2. **Slow algorithms** — bcrypt does ~17,000 hashes/second instead of 20 billion. A table
   that took 3 seconds with MD5 takes roughly **8 months** with bcrypt.
3. **Salt rounds** — deliberately configurable work factor, increased as hardware gets
   faster.
4. **Rate limiting + lockouts** — stop online guessing entirely.
5. **Password managers / long passphrases** — the user's half of the bargain.

---

### Summary Checklist

1. Attackers crack hashes with dictionaries, rainbow tables and brute force.
2. Fast hashes make all three cheap — speed is the vulnerability.
3. Identical hashes for identical passwords leak information.
4. Salting (random, unique, stored with the hash) breaks pre-computed tables.
5. bcrypt + salt rounds + rate limiting is the modern baseline.
