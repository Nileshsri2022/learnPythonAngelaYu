Here is a structured breakdown of Step 1 — studying how the game plays.

---

### 1. Watch Before You Build

Run the finished demo and note the *observable* behaviour — this defines your
requirements:

* Turtle starts bottom-centre; `Up` nudges it one step north. No other movement.
* Cars only ever spawn on the **right edge** at random lanes and drive **left**.
* Car stream is continuous but not wall-to-wall — gaps exist (random spawn timing).
* Collision looks forgiving: a squish only when genuinely overlapping.
* Crossing the top: instant reset to the start, all cars visibly faster.
* Score top-right increments per crossing; collision shows GAME OVER.

---

### 2. Turning Observation Into Specs

Each observed behaviour maps to a feature: input handling, spawn logic, randomisation,
collision box, level-up, score state. Writing the list *before* coding is the Step 2
decomposition lesson in disguise.

---

### Summary Checklist

1. Play the demo like QA: what exactly happens, when, in what order?
2. Observable behaviour = your requirements list.
