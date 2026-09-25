Here is a structured breakdown of this lesson on the TinDog startup website project.

---

### 1. The Brief

A startup called **TinDog** — "Tinder for dogs" — wants a landing page:

* title/hero with headline, download buttons and an iPhone image,
* features section (easy, elite, love),
* testimonials with dog photos,
* pricing plans,
* footer with links and social icons.

Reference: `appbrewery.github.io/tindog`.

---

### 2. Starter Files and Workflow

Download and unzip the project:

```
tindog/
├── index.html      # section placeholders + comments
├── style.css       # includes the .gradient-background class
└── images/         # iphone.png, dog images, ...
```

`index.html` comes pre-divided into `<section>` elements — semantically "an area of the
page", and a clean way to organise code:

```html
<section id="title">  … hero …       </section>
<section id="features"> … cards …    </section>
<section id="testimonials"> … quotes </section>
<section id="pricing"> … plans …     </section>
<footer> … links …                   </footer>
```

The README provides the SVG icons (Apple/Google logos) and all the marketing copy — in
real life the client writes the copy, you place and style it.

---

### 3. Build Order

| Step | What |
|------|------|
| 1 | Add the Bootstrap **CSS link** in `<head>` — without it everything renders as plain HTML |
| 2 | Hero: copy a Bootstrap *Hero* example, replace text and images |
| 3 | Features: three cards in a `row` of `col-lg-4` |
| 4 | Testimonials: a carousel or a simple press-logo section |
| 5 | Pricing: three cards, middle one emphasised |
| 6 | Footer: nav links + SVG icons |
| 7 | Add the Bootstrap **JS bundle** before `</body>` so interactive pieces work |
| 8 | Style overrides in `style.css` (gradient background, fonts, colours) |

---

### 4. The Gradient Background

`style.css` ships with a `.gradient-background` class (adapted from a CodePen by Manuel
Pinto) that animates between three colours:

```css
.gradient-background {
    background: linear-gradient(300deg, #00bfff, #ff4c68, #ef8172);
    background-size: 180% 180%;
    animation: gradient-animation 18s ease infinite;
}
```

Add the class to a section (`<section class="gradient-background">`) and it animates
immediately.

---

### 5. Definition of Done

* [ ] Bootstrap CSS + JS both linked (check the hamburger menu works).
* [ ] Every section matches the reference page.
* [ ] Layout is responsive: three cards on desktop, stacked on mobile.
* [ ] Copy, images and icons from the README are in place.
* [ ] Your own CSS only *overrides* Bootstrap — no fighting it.

> **Tip:** Give the project an hour, and expect to spend most of it exploring the docs
> looking for the snippet that matches. That exploration *is* the skill.

---

### Summary Checklist

1. `<section>` per area of the page; build them one at a time.
2. Bootstrap CSS first, JS bundle last — check both.
3. Hero, cards, carousel, pricing and footer all come from snippets.
4. Layout responsiveness comes from the 12-column grid (`col-lg-4`, etc.).
5. Customise with your own CSS loaded after Bootstrap's.
