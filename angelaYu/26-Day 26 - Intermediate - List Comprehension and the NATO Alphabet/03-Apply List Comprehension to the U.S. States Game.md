# 🔧 Apply List Comprehension to the U.S. States Game

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 26 - Intermediate - List Comprehension and the NATO Alphabet
**Lecture:** Apply List Comprehension to the U.S. States Game
**Level:** Intermediate

---

### Summary

Now the reason why we&#x27;re learning about list comprehensions is because when we created all US states game, I realized that the code that we were writing could be a lot shorter if only we knew about list comprehensions. So I want you to head back over to your code for the US states game and open it up. And I want you to look at this if statement. So when the user types exit, we create a new list of missing states in order to save it to a CSV file. I want you to change this code using your new knowledge of this comprehension and see if you can cut down this code by three or four lines. Pause the video and complete this challenge now. All right. So instead of all of this, creating a new empty missing state and then going through a for loop, we can simply do this in one line. So again, it&#x27;s going to be called missing_states and this is going to be a new list, but this time it&#x27;s going to be created using our list comprehension; new item for item in list if test. The list in this case that we&#x27;re looping through is all of our states. So we&#x27;re gonna replace that with all states. Now, each of the items is basically a state in that list. And the test that we&#x27;re going to make is to see well if the state is not in the guessed_states which has states added every time the user makes a correct guess so we can basically take this part of our previous code and put it here. And in that case, then we&#x27;re going to add this particular state which pass this test into this new list. This one line basically will replace all four of these lines and it cuts down dramatically on the amount of code. And it reads relatively well as well. Add a state to this new list if we loop through all the states in the list of states and if that state is not in this list of guessed states. List comprehensions are super popular with Python developers and I hope through some of these exercises you can see why, just in terms of the sheer amount of code that it cuts down on and how much it simplifies things. Now, in addition to list comprehensions, we can also do comprehensions with dictionaries. So in the next lesson, that&#x27;s what we&#x27;re going to be looking at.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **for loops** | Introduced/used in this lecture |
| 2 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 3 | **List comprehensions** | Introduced/used in this lecture |

---

### 🏋️ Practice Exercise

Now the reason why we&#x27;re learning about list comprehensions is because when we created all US states game, I realized that the code that we were writing could be a lot shorter if only we knew about list comprehensions. So I want you to head back over to your code for the US states game and open it up. And I want you to look at this if statement. So when the user types exit, we create a new list of missing states in order to save it to a CSV file. I want you to change this code using your new knowledge of this comprehension and see if you can cut down this code by three or four lines. Pause the video and complete this challenge now. All right. So instead of all of this, creating a new empty missing state and then going through a for loop, we can simply do this in one line. So again, it&#x27;s going to be called missing_states and this is going to be a new list, but this time it&#x27;s going to be created using our list comprehension; new item for item in list if test. The list in this case that we&#x27;re looping through is all of our states. So we&#x27;re gonna replace that with all states. Now, each of the items is basically a state in that list. And the test that we&#x27;re going to make is to see well if the state is not in the guessed_states which has states added every time the user makes a correct guess so we can basically take this part of our previous code and put it here. And in that case, then we&#x27;re going to add this particular state which pass this test into this new list. This one line basically will replace all four of these lines and it cuts down dramatically on the amount of code. And it reads relatively well as well. Add a state to this new list if we loop through all the states in the list of states and if that state is not in this list of guessed states. List comprehensions are super popular with Python developers and I hope through some of these exercises you can see why, just in terms of the sheer amount of code that it cuts down on and how much it simplifies things. Now, in addition to list comprehensions, we can also do comprehensions with dictionaries. So in the next lesson, that&#x27;s what we&#x27;re going to be looking at.

---

### Next Steps

Now the reason why we&#x27;re learning about list comprehensions is because when we created all US states game, I realized that the code that we were writing could be a lot shorter if only we knew about list comprehensions. So I want you to head back over to your code for the US states game and open it up. And I want you to look at this if statement. So when the user types exit, we create a new list of missing states in order to save it to a CSV file. I want you to change this code using your new knowledge of this comprehension and see if you can cut down this code by three or four lines. Pause the video and complete this challenge now. All right. So instead of all of this, creating a new empty missing state and then going through a for loop, we can simply do this in one line. So again, it&#x27;s going to be called missing_states and this is going to be a new list, but this time it&#x27;s going to be created using our list comprehension; new item for item in list if test. The list in this case that we&#x27;re looping through is all of our states. So we&#x27;re gonna replace that with all states. Now, each of the items is basically a state in that list. And the test that we&#x27;re going to make is to see well if the state is not in the guessed_states which has states added every time the user makes a correct guess so we can basically take this part of our previous code and put it here. And in that case, then we&#x27;re going to add this particular state which pass this test into this new list. This one line basically will replace all four of these lines and it cuts down dramatically on the amount of code. And it reads relatively well as well. Add a state to this new list if we loop through all the states in the list of states and if that state is not in this list of guessed states. List comprehensions are super popular with Python developers and I hope through some of these exercises you can see why, just in terms of the sheer amount of code that it cuts down on and how much it simplifies things. Now, in addition to list comprehensions, we can also do comprehensions with dictionaries. So in the next lesson, that&#x27;s what we&#x27;re going to be looking at.
