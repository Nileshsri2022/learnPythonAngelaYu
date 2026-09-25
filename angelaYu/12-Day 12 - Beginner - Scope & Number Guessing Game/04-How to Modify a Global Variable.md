# 🐍 How to Modify a Global Variable

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 12 - Beginner - Scope & Number Guessing Game
**Lecture:** How to Modify a Global Variable
**Level:** Beginner

---

### Summary

Coming back to our original example, I want to talk more about the Global Scope, and the concept of modifying something within the global scope. Here we have enemies, which is a variable that has global scope, and here we have a function which creates a local scope. Now we think that we&#x27;re tapping into this variable and setting it to 2, but in fact, we&#x27;re actually creating a completely new variable that&#x27;s entirely separate from this one. And this is why when we printed it here, it showed it was equal to 2, but when we printed it here, it showed it was actually equal to 1. If you want to make this a little bit more obvious, I can call this a &quot;Skeleton&quot;, and I can set this to be a &quot;Zombie&quot;. And when I hit Run, you can see again, this prints &#x27;Zombie&#x27;, this prints &#x27;Skeleton&#x27;. Because these two variables are actually entirely different things. And we&#x27;re not changing this right here at all, we&#x27;re just creating a new variable that has a local scope. Now, it&#x27;s usually a terrible idea to call your local variables and your global variables the same name. But in this case, what we actually wanted to do was we wanted to modify this variable. We wanted to do something like maybe + = 1. And notice how as soon as I write + = 1, then my editor starts going crazy and tells me that this local variable &#x27;enemies&#x27; is defined in an enclosing scope is referenced before assignment. What does that mean? It means that the editor thinks you&#x27;re trying to tap into a local variable that you defined somewhere around here, and then you try to modify it by adding one to the previous value, but you actually haven&#x27;t defined it. What we wanted to do, though, is we wanted to tap into this variable and change it here. In order to do this, we actually have to explicitly say that we have a global variable which is called enemies, that&#x27;s defined somewhere outside of this function, and that is the enemies that we want to use inside this function. So it basically takes that global enemies into the function and allows you to modify it. Without this line of code, we cannot modify something that is global within a local scope. Now, there&#x27;s a reason why it&#x27;s so difficult to modify something that has global scope. You probably don&#x27;t actually want to do this very often because it&#x27;s confusing and it&#x27;s prone to creating bugs and errors, because this variable with global scope could have been created anywhere in your code, right? And you would be modifying it completely independent of when you created it. So it might have been days between when you wrote this code and when you wrote this code, and it just makes everything more fallible, more easy to fail. This is why very often people will tell you when they&#x27;re teaching you Python to avoid modifying global scope. You can read it, that&#x27;s not a problem, you can use it within your code like we are here but don&#x27;t try to modify it within a function that has local scope. But what can you do instead? What if you wanted to have this functionality like a function that changes the number of enemies? How can you achieve this without modifying the global scope within the function? Well, you could use what we learned about return statements instead, right? What if instead of modifying the enemies, you actually just simply returned it as the output? So return the current value of enemies + 1. Now, once you call this function, you&#x27;ll get hold of the outputs and you can save it to the global variable enemies. So this now means that this function can be taken away and placed anywhere in your code, and you don&#x27;t actually need to know how it works, as long as you know that this is how you increase enemies, then all you have to do is just call it.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |

---
