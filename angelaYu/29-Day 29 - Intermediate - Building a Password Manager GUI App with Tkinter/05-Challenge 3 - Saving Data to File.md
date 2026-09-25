# Challenge 3 - Saving Data to File

---

### 1. The Add Function

```python
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, tkinter.END)     # clear for the next entry
    password_entry.delete(0, tkinter.END)
```

* `.get()` reads all three fields; `"a"` mode appends a pipe-separated line per entry.
* `delete(0, tkinter.END)` clears a field completely.
* The website field is also cleared, but the email stays — you usually reuse it.

---

### 2. Validation (introduced here, formalised Day 30)

Before writing, the lesson asks: what if the user leaves a field empty? The next lesson's
`messagebox.showwarning` handles it properly — a preview of Day 30's exceptions work.

---

### Summary Checklist

1. `"a"` append mode; one `website | email | password` line per save.
2. `delete(0, END)` resets fields after saving.
3. Empty-field validation arrives with dialogs next.
