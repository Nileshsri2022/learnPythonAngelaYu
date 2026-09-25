Here is a structured breakdown of this lesson on using website templates.

---

### 1. The Challenge

Take a fully designed personal site (with CSS, images and GIFs) and get it running on your
Flask server — reviewing everything from the last two lessons.

Steps:

1. Download and unzip the provided site files.
2. Move pieces to the right places:

| Files | Destination |
|-------|-------------|
| `index.html` | `templates/` |
| `styles.css`, `images/`, `favicon` | `static/` |

3. Update every local path in the HTML so it points inside `static/`.
4. Restart the server and refresh.

---

### 2. Fixing the Paths (Find & Replace)

Instead of editing each `src` by hand, use Find & Replace:

| Find | Replace with |
|------|--------------|
| `src="images/` | `src="static/images/` |
| `href="styles.css"` | `href="static/styles.css"` |
| `href="favicon` | `href="static/favicon` |

> **Tip:** Careful with trailing slashes in replacements — dropping a `/` is the classic way
> to break one image (or all of them). The task in the next lesson revisits exactly this.

---

### 3. Free Templates Are the Real Payoff

Sites like **HTML5 UP** publish beautiful, responsive, free HTML/CSS templates. Download
one, and:

```
downloaded-template/
├── index.html     → templates/
├── assets/        → static/assets/
└── images/        → static/images/
```

Now find-and-replace `assets/` → `static/assets/` and `images/` → `static/images/`, restart,
hard-reload, and you've served a professional-grade site with a free design.

| Model | Cost | You need to know |
|-------|------|------------------|
| HTML5 UP template | Free (attribution) / $19 commercial | HTML, CSS, Flask |
| Website builder (e.g. Squarespace) | $10–30 / month | nothing |

> **Note:** Free templates usually ship with placeholder images (often just gradients)
> because the designer can't license photos. Swap in your own — or use Unsplash — and
> rename the file to match the original (`bg.jpeg`, `avatar.png`) so the CSS keeps working.

---

### 4. Attribution

If you use a free template, **credit the designer** (usually a link in the footer — leave
it). Buy the $19 licence if you need it for commercial work.

---

### Summary Checklist

1. HTML → `templates/`, everything else → `static/`.
2. Find & replace every local asset path to include the `static/` prefix.
3. Free, beautiful templates exist — you only need to fix the paths.
4. Placeholder images are normal; matching filenames beats editing CSS.
5. Keep the credit in the footer unless you buy a commercial licence.
