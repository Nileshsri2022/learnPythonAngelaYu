# Step 1 - Create a Sharable Form linked to your Sheet

---

### 1. Google Forms → Sheet

1. Add a second tab (`users`) to the flight-deal spreadsheet.
2. Create a Google Form with First name / Last name / Email.
3. In the Form's *Responses* tab, link it to the spreadsheet — every submission becomes
   a row automatically.
4. Share the form link with anyone who wants deal alerts.

---

### 2. Why This Matters

You just built a **sign-up flow with zero backend**: form (frontend) → sheet (database)
→ Sheety (API) → your script (server). For a weekend project this stack is unbeatable.

---

### Summary Checklist

1. Form responses land in the `users` tab in real time.
2. The sheet is now a two-table database: destinations + users.
