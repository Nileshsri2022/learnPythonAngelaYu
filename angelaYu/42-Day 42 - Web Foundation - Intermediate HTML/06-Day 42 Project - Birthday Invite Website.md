Here is a structured breakdown of the Day 42 project — Birthday Invite Website.

---

### 1. The Requirements

A single page combining *everything* from Day 41–42: headings, paragraphs, lists
(ordered + unordered + nested), images, anchor, `<br>` and `<hr>`.

---

### 2. The Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Birthday Invite</title>
</head>
<body>
    <h1>Today is Nilesh's Birthday 🎉</h1>
    <h2>You're invited to celebrate!</h2>
    <img src="birthday-cake.jpg" alt="Birthday cake" height="250">

    <h3>The Plan</h3>
    <ol>
        <li>Arrive by 7 PM</li>
        <li>Dinner &amp; cake</li>
        <li>Games until late</li>
    </ol>

    <h3>What to Bring</h3>
    <ul>
        <li>Your dancing shoes
            <ul>
                <li>Backup socks too</li>
            </ul>
        </li>
        <li>A big appetite</li>
    </ul>

    <h3>Where</h3>
    <p>
        42 Gomti Nagar,<br>
        Lucknow, Uttar Pradesh
    </p>
    <a href="rsvp.html">RSVP here</a>
    <hr>
    <p>This invite was hand-coded in HTML.</p>
</body>
</html>
```

---

### Summary Checklist

1. Every element from two days of HTML in one page.
2. Runnable version: [`birthday_invite.html`](birthday_invite.html)
