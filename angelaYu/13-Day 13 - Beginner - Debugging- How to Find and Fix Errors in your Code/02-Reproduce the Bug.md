# 🐍 Reproduce the Bug

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 13 - Beginner - Debugging: How to Find and Fix Errors in your Code
**Lecture:** Reproduce the Bug
**Level:** Beginner

---

### Summary

Now, the next step is to think about reproducing the bug that you&#x27;ve encountered, because when you encounter it once but you don&#x27;t encounter it the next time, that becomes a really difficult bug to fix. In this section, we&#x27;re going to try and reproduce the bug. So when we run the code, sometimes it will work and it will print out one of the dice_images from this list, but occasionally you will get an error. These types of bugs are really difficult because you might test your code only once or twice and it looks all fine. It works, but then occasionally you get an error. And the important thing is to reproduce that error. When does that error actually happen? And based on that knowledge, we can fix our code. Try to reproduce the bug yourself and try to notice when it happens, and see if you can change the code so that it always produces this error. We&#x27;ve got a list of dice_images which are just emojis, and we&#x27;ve also got this random number, dice_num, between 1 and 6. Now, when we try to pick out of our list, occasionally, we get an error. Now we have to notice when the error occurs, and to reproduce the bug, we have to figure out which of these numbers is actually causing the problem. So we know that this is a random number between 1 and 6. And if we check the documentation, it tells us that randint() works a little bit differently from range(), it will return a random integer in the range of A and B, including both end points. So in our case, both 1 and 6 could be generated and it could be any number. So if that was equal to 1 well does it generate an error? No. It just picks out this particular item. But what if it was 2, or 3, or 4? Or what if we tested 6? Well, now every time we hit run, you can see we get an error. And now that we&#x27;ve got our error to show up consistently, it&#x27;s a lot easier to debug because we know that the &#x27;IndexError: list index out of range,&#x27; happens when this dice_num is 6. So when we go back to our previous code, well, we can&#x27;t use 6 in this list because lists start counting from 0. So to get this Dice 1, we need dice_num to be 0. And then this is 1, 2, 3, 4, 5, and 6 is somewhere out here and it doesn&#x27;t exist. Now go ahead and fix this code so that all the dice_images are represented and we never see this error again. All right. So that is as simple as shifting down these numbers. So instead of making a random number between 1 and 6 we actually want a random number between 0 and 5. And now no matter how many times we run our code, we&#x27;re never going to get that error show up again.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 2 | **range() function** | Introduced/used in this lecture |
| 3 | **random module** | Introduced/used in this lecture |

---
