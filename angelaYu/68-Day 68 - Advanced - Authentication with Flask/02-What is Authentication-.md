Here is a structured breakdown of this lesson on what authentication is.

---

### 1. The Core Idea

Every user who visits your site creates data — likes, messages, posts. Without accounts,
you can't say *whose* data it is. Authentication gives every user an identity:

```
register → create account (username + password)
login    → prove you are that account
session  → the site remembers you while you browse
logout   → forget you
```

Like an ID card: issued once, presented on every visit.

---

### 2. Two Separate Jobs People Confuse

| Term | Question it answers |
|------|---------------------|
| **Authentication** | *who are you?* (login) |
| **Authorisation** | *what are you allowed to do?* (paid tier, admin, owner of a post) |

Today's project is authentication; the "premium content" use case is authorisation layered
on top.

---

### 3. Why Sites Need It

* **Privacy** — your DMs shouldn't be visible to strangers.
* **Personalisation** — "your" feed, "your" saved items.
* **Monetisation** — subscribers see the content they paid for.
* **Safety** — nobody should be able to delete someone else's post.

---

### 4. The Hard Part Is Security, Not Login Forms

Making a login page is easy. Making it *safe* is the discipline:

* never store passwords as they were typed,
* never let one user act as another,
* never expose who exists to someone unauthenticated.

> **Note:** A functional login that stores plain-text passwords is *worse* than no login —
> it invites users to hand you a secret you can't protect.

---

### 5. What You'll Build

A site with `/register`, `/login`, `/logout` and a `/secrets` page that only
authenticated users can reach — then progressively harden the password storage underneath
it.

---

### Summary Checklist

1. Authentication = identity; authorisation = permissions.
2. Accounts exist to attach data to users and to gate content.
3. The valuable skill is doing it securely.
4. Project: register, login, logout and a protected page.
