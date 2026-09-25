# 📖 __name__ and __main__ : Special Attributes built into Python

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 54 - Intermediate+ Introduction to Web Development with Flask
**Lecture:** __name__ and __main__ : Special Attributes built into Python
**Level:** N/A

---

### Summary

Now that we&#x27;ve understood a little bit more about the terminal commands, let&#x27;s come back to our Flask code and understand what the code is doing in a little bit more detail. For example, what is this name? Because we&#x27;re creating this app from this Flask class and in order to initialize a new Flask application, there is only one required input, and that is the import_name. Let&#x27;s go ahead and print it out. So if we print this __name__ and comment out the rest of our code and hit run, then you can see that it prints out __main_ _. This name is one of the special attributes that&#x27;s built into Python. At any given point, you could tap into the name to find out what is the current class, function, method, or descriptor&#x27;s name. And when we get main, what it&#x27;s telling us is basically we&#x27;re executing the code in a particular module. So that means it&#x27;s run as a script or from an interactive prompt, but it&#x27;s not run from an imported module. It gives us this code here, if the name is equal to main, then execute something only if it&#x27;s run as a script. This also takes us to one of the common ways that you&#x27;ll see people run Flask apps. You&#x27;ll see if __name__ is double equal to _ _main__ as a string, so exactly what was printed just now when we printed out this name, well, if this is the case, then that means we&#x27;re running the code from within this current file. We&#x27;re running hello.py. So in that case, we&#x27;re going to tap into our app and we&#x27;re going to call the run method. Now this app.run basically does exactly the same thing as when we went into the terminal and we said flask run. But notice when we say flask run, firstly, we have to provide the FLASK_APP environment variable and secondly, we have to stop the code using control + c instead of using our normal run and stop. But if we use app.run, we can now use our standard controls. So I can simply hit run to run this hello.py, and it will start serving up our Flask app at this address just as it did before, when we did flask run. And instead of using control + c to quit, we can simply use the stop to stop our Flask application, making it a lot easier. Basically by providing the name to Flask, Flask will check that this is the current file where the app code is located. And we&#x27;re not in fact using an imported module. For example, if I was to import the random module and I was to print the random.name, then you can see the first thing that gets printed is the name of that module. But the name that&#x27;s printed from hello.py which is the file that&#x27;s being run is simply __main__. So this basically denotes the file that is currently being run and you say, Run &#x27;hello&#x27; Well then inside hello name is going to be equal to main. Right.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **Class definitions (class)** | Introduced/used in this lecture |
| 2 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 3 | **Module imports** | Introduced/used in this lecture |
| 4 | **Flask web framework** | Introduced/used in this lecture |
| 5 | **random module** | Introduced/used in this lecture |

---
