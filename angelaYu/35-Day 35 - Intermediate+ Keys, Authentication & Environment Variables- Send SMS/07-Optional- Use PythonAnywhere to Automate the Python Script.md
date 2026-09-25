Here is a structured breakdown of this lesson on PythonAnywhere automation.

---

### 1. The Goal

A script that must run *every* morning can't live in PyCharm. **PythonAnywhere** hosts it
in the cloud:

1. Upload the project (or pull from GitHub).
2. Open a **console** and test it there.
3. Add a **Scheduled task** with cron syntax: `30 1 * * * python3 /home/you/rain_alert.py`
4. Set your keys as environment variables in the web app's config.

---

### 2. The Free Tier

A free account includes scheduled daily tasks — enough for this project (though the
lesson notes availability has changed over time; GitHub Actions — next lesson — is the
reliable free option).

---

### Summary Checklist

1. Cloud + cron = automation without your laptop.
2. Same rule everywhere: secrets as env vars, never in uploaded code.
