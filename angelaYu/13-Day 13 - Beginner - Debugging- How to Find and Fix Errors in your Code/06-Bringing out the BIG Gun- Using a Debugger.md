# Bringing out the BIG Gun- Using a Debugger

---

### 1. Tip #6: Use a Real Debugger

When prints get noisy, upgrade to a **debugger** — a tool that pauses the program and lets
you walk through it line by line, watching every variable live. PyCharm has one built in
(and you met it conceptually back on Day 5 with Thonny):

1. **Set a breakpoint** — click in the gutter next to the suspicious line.
2. **Debug instead of Run** — execution stops at the breakpoint.
3. **Step through** — the controls:

| Button | Action |
|--------|--------|
| Step Over | run the current line (stay in this function) |
| Step Into | enter a function called on this line |
| Step Out | finish the current function and return |
| Resume | run until the next breakpoint |

4. **Watch the variables pane** — every value updates as you step.

---

### 2. Why It Beats Prints

* You see **all** variables at once, not just the ones you remembered to print.
* No code changes needed — nothing to clean up afterwards.
* Loop iterations can be inspected one at a time.

---

### Summary Checklist

1. Breakpoint + step = slow-motion replay of your program.
2. The variables pane shows the program's true state at every instant.
3. Use prints for quick checks; use the debugger for real hunts.
