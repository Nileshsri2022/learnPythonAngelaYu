# Day 24 Goals: what you will make by the end of the day

Day 24 is about the **local file system** — reading, writing and understanding
directories — and it ends with an automation project that removes a genuinely
tedious job.

---

### 1. What You Will Learn

| Skill | Why it matters |
|-------|----------------|
| Absolute vs relative **paths** | Finding a file reliably from any script |
| `open()` — read / write / append | Saving data *between* runs of a program |
| Reading line by line, writing lines | Processing text files |
| Directories with `os` / `pathlib` | Creating folders, listing what is inside |

---

### 2. The Snake Game Upgrade: A High Score

Right now Snake just ends when you hit a wall or your own tail. After today it will
**remember the best score ever achieved**:

1. On game over, compare the score with the stored `high_score`.
2. If it is higher, write the new value to a file (e.g. `data.txt`).
3. On the next launch, read that file and display the value in the scoreboard.

That is the point of files: **state that survives the program**.

---

### 3. The Project: Mail Merge

Instead of writing the same letter over and over, Python can personalise it for you:

```text
letter.txt          names.txt
Dear [name],        James
I am invited to…    Emily
                    Angela
```

* Read the template → find the placeholder `[name]`
* Loop over the list of names → replace the placeholder
* Write out **one file per person** (`letters/for_james.txt`, …)

The same pattern scales to wedding invitations, invoices and client emails.

---

### Summary Checklist

1. Files give a program memory that outlives a single run.
2. `open(file, mode)` — `"r"` read, `"w"` overwrite, `"a"` append.
3. Paths can be **absolute** (from the root) or **relative** (to the working directory).
4. Mail merge = read template → loop names → write one personalised file each.
5. Snake gets a persistent high score saved to `data.txt`.
