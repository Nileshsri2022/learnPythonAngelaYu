Here is a structured breakdown of this lesson on breaking a complex problem down into a flow chart.

---

### 1. Big Problems Need Planning

Before writing a single line of Hangman code, the lesson does something professionals do
for every project: **draw the logic as a flowchart** (pen and paper, or draw.io).

Ask yourself:

* What needs to happen **first**?
* What happens when the user makes a **guess**?
* What happens when the guess is **wrong**?
* When does the game **end**?

---

### 2. The Hangman Logic, Flowcharted

1. **Start:** pick a random word → show blanks `_ _ _ _`.
2. **Ask** the player for a letter.
3. **Is the letter in the word?**
   * Yes → reveal it in every position it occurs.
   * No → lose a life; draw the next stage of the hangman.
4. **Won or lost?**
   * All blanks filled → **You win**.
   * Lives reach 0 → **You lose**.
   * Otherwise → loop back to step 2.

That loop-back arrow in the flowchart is literally the `while` loop in the code.

---

### 3. The Steps of the Build

The project is split into five progressive steps:

| Step | Adds |
|------|------|
| 1 | Random word + check a guess |
| 2 | Blanks that fill in with correct guesses |
| 3 | Keep guessing until the word is complete |
| 4 | Lives + hangman ASCII art |
| 5 | Polish: modules, already-guessed feedback, UX |

---

### Summary Checklist

1. Flowcharts turn "build a game" into a list of small, answerable questions.
2. The while-loop back-edge is visible in the flowchart before it's in the code.
3. Five small steps beat one giant leap.
