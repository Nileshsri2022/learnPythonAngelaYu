# 🐍 Play Computer and Evaluate Each Line

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 13 - Beginner - Debugging: How to Find and Fix Errors in your Code
**Lecture:** Play Computer and Evaluate Each Line
**Level:** Beginner

---

### Summary

Very often I&#x27;ve asked you in the quizzes especially to play computer, and the reason is because this skill of pretending to be a computer, reading through your code and imagining what you&#x27;re going to do each time is really, really useful, especially when you&#x27;re debugging. Take a look at this code. It takes an input in the form of an integer, and it asks the user for their year of birth, and then it uses an if statement to check if they were born between 1980 and 1994, in which case they&#x27;re classified as a Millennial. But if they were born later than 1994, then they&#x27;re classified as a Gen Z. So depending on which country you&#x27;re from, there&#x27;s different classifications for your particular generation. This is just the typical words that you hear on the internet, &quot;You&#x27;re a Millennial, you&#x27;re a Gen Z, you&#x27;re a Baby boomer.&quot; And this comes from a lot of the history of the US. But nonetheless, I want you to run the code, and I want you to see what happens when I put in 1994 absolutely nothing. So we have our bug right there. Run through the code line by line and evaluate each statement and follow the logic and check what it will evaluate to. So I want you to play computer and figure out what is the problem, and then go ahead and fix the bug. Pause the video now. All right. So let&#x27;s pretend that we got 1994 as the input. So now I&#x27;m the computer and I know that this year is equal to 1994. Now with this year being equal to 1994, I go into this if statement. So is 1994 greater than 1980? Yes it is. So this actually becomes True. Now I have to check the second condition, and it also has to be True for this if block to be triggered. So is 1994 less than 1994? No it&#x27;s not. It&#x27;s actually less than equal to 1994 or it&#x27;s equal to 1994. So in this case, this condition becomes False, and we know that if we try to combine a True and a False, then it actually just becomes a False. So this gets skipped. Now next we look at the next statement, right? If 1994 is greater than 1994 well that&#x27;s also not True. It could be greater or equal to, or it could just be equal to. So this condition is also False. So that means it&#x27;s also going to skip this next line and there&#x27;s no more lines of code left, which is why the computer doesn&#x27;t print anything. So let&#x27;s restore our code to before we started playing computer. And we can identify that this problem occurs because there is no bucket that actually catches the 1994. We could simply fix this code by changing one of these conditions to be greater than, or equal to, either here or here. And that means that the year 1994 is not skipped over in our conditions. And when we hit Run, it&#x27;ll actually tell us that we are, in fact, a Gen Z.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |

---

### 🏋️ Practice Exercise

Very often I&#x27;ve asked you in the quizzes especially to play computer, and the reason is because this skill of pretending to be a computer, reading through your code and imagining what you&#x27;re going to do each time is really, really useful, especially when you&#x27;re debugging. Take a look at this code. It takes an input in the form of an integer, and it asks the user for their year of birth, and then it uses an if statement to check if they were born between 1980 and 1994, in which case they&#x27;re classified as a Millennial. But if they were born later than 1994, then they&#x27;re classified as a Gen Z. So depending on which country you&#x27;re from, there&#x27;s different classifications for your particular generation. This is just the typical words that you hear on the internet, &quot;You&#x27;re a Millennial, you&#x27;re a Gen Z, you&#x27;re a Baby boomer.&quot; And this comes from a lot of the history of the US. But nonetheless, I want you to run the code, and I want you to see what happens when I put in 1994 absolutely nothing. So we have our bug right there. Run through the code line by line and evaluate each statement and follow the logic and check what it will evaluate to. So I want you to play computer and figure out what is the problem, and then go ahead and fix the bug. Pause the video now. All right. So let&#x27;s pretend that we got 1994 as the input. So now I&#x27;m the computer and I know that this year is equal to 1994. Now with this year being equal to 1994, I go into this if statement. So is 1994 greater than 1980? Yes it is. So this actually becomes True. Now I have to check the second condition, and it also has to be True for this if block to be triggered. So is 1994 less than 1994? No it&#x27;s not. It&#x27;s actually less than equal to 1994 or it&#x27;s equal to 1994. So in this case, this condition becomes False, and we know that if we try to combine a True and a False, then it actually just becomes a False. So this gets skipped. Now next we look at the next statement, right? If 1994 is greater than 1994 well that&#x27;s also not True. It could be greater or equal to, or it could just be equal to. So this condition is also False. So that means it&#x27;s also going to skip this next line and there&#x27;s no more lines of code left, which is why the computer doesn&#x27;t print anything. So let&#x27;s restore our code to before we started playing computer. And we can identify that this problem occurs because there is no bucket that actually catches the 1994. We could simply fix this code by changing one of these conditions to be greater than, or equal to, either here or here. And that means that the year 1994 is not skipped over in our conditions. And when we hit Run, it&#x27;ll actually tell us that we are, in fact, a Gen Z.

---
