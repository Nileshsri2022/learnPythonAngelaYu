# 🐍 Does Python Have Block Scope?

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 12 - Beginner - Scope & Number Guessing Game
**Lecture:** Does Python Have Block Scope?
**Level:** Beginner

---

### Summary

Now, unlike some other programming languages, if you&#x27;ve come from, say, C++, or Java, there is no such thing as Block Scope in Python. What this means is that if you were to create an if statement, say if 3 &gt; 2: and if you were to create a new variable inside an if block, or a while loop, or a for loop, basically any sort of block of code that&#x27;s indented, this does not count as a fence. It still has the same scope as its enclosing function, or if there&#x27;s no enclosing function, then it has global scope. So let me show you a full example. Let&#x27;s say we had a list of enemies so the enemies could be [&quot;skeletons&quot;, &quot;zombies&quot;, &quot;aliens&quot;]. So now if I was to define a game_level, right? Like the level that the user is currently playing at, let&#x27;s say they&#x27;re on Level 3 and I create an if statement and I check if the game_level is less than Level 5, well, in that case, I want to create a new_enemy, but I don&#x27;t want the enemy to be too difficult to beat. So I&#x27;m going to pick from the list of enemies and I&#x27;m going to pick the first one. Notice how even though this new_enemy is a variable that&#x27;s created within this if block if I go outside the if block, so I&#x27;m not indented at all anymore and I try to print this new_enemy, this is perfectly valid code. And if I run the code you&#x27;ll see &#x27;Skeleton&#x27; being printed. But notice how as soon as I embed this within a function. So let&#x27;s define a new function. And now this line error is out because within the function there is local scope, so now this new_enemy is available anywhere within this function, because blocks like if, while, for, all of these blocks of code with colons and indentation, they don&#x27;t count as creating a local scope. So in order to print this new_enemy, I actually have to be within the boundary of this function, which means my code has to be here. The most important thing to remember from this is if you create a variable within a function, then it&#x27;s only available within that function. But if you create a variable within an if block, or a while loop, or a for loop or anything that has the indentation and the colon, then that does not count as creating a separate local scope. But one thing you might see when you&#x27;re using some variable that is defined within a block, such as an if or a for is, you might get this warning from the linter, which reminds us how to write good Python code that the local variable might be referenced before assignment. So it&#x27;s basically saying, well, what if the game_level is not less than five? What if it was like ten? Well, in this case, if we try to run this code, this print statement will never be executed because this if statement is not true. So this variable new_enemy is never created. So then what are we printing here? We&#x27;re printing nothing. Just air. Right? So in order to get rid of this warning, what you can do is outside of any blocks, such as if, for, or while you can declare and create that variable and initialize it. So let&#x27;s create new_enemy and set it to empty. Well, in this case, what it sees now is that there is a new_enemy variable. It has been already created, and depending on these conditions it might be modified, but it will always be able to be accessed. So the outcome doesn&#x27;t really change. but the linter sees these situations where something could potentially go wrong and is just reminding you. So you have two choices. You can ignore it if you know what it&#x27;s saying is complete rubbish because you know your code better than it does, or you can follow its orders and simply initialize the variable before you ever use it, and instead of creating the variable inside a block that may not be accessed.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **while loops** | Introduced/used in this lecture |
| 2 | **if/elif/else conditionals** | Introduced/used in this lecture |

---
