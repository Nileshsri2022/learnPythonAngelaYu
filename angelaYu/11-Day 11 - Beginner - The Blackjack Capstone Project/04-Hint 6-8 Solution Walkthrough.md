# 🐍 Hint 6-8 Solution Walkthrough

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 11 - Beginner - The Blackjack Capstone Project
**Lecture:** Hint 6-8 Solution Walkthrough
**Level:** Beginner

---

### Summary

All right. So now let&#x27;s tackle Hint Number 6. We&#x27;re going to create a function called calculate_score(), that&#x27;s going to take a list of cards as an input, and then it returns the score after calculation. And it tells us that if we get stuck we can look up the sum() function to help us. So let&#x27;s create a function called calculate_score(). And this calculate_score() is going to take some cards as an input, and then inside the body, it&#x27;s going to calculate the total of all the cards in this list. So if we take a look at the sum() function in Python, the way that it works is you can put an iterable, so like a list, inside the parentheses as an input, and then it&#x27;s going to add up all of the items in the list, and it&#x27;s going to return the total. Back in our code, we can simply write sum(), and then inside these parentheses, we can pass over the cards and we can return this value as the output. Basically, if we had cards equal to a list with [1, 5, 3, 4], then this sum() function is going to end up being equal to 1 + 5 + 3 + 4, which is going to be equal to 13. And then that will become the output of this function. So now let&#x27;s move on to Hint 7. A Blackjack only happens when we have a hand with only 2 cards, and those cards have to be an Ace and a 10-value card. In our deck, we know that an Ace is represented by 11 and we have a number of 10-value cards. So there&#x27;s a number of ways that we can check for this Blackjack. One of the ways is by checking to see if the 11 is in our deck of cards, and then we can combine that with an and, to check if the 10 is also in our deck of cards. And finally, we can check to make sure that we&#x27;ve got a hand size of 2. So we can check that the length of our cards is equal to 2, and this would represent this logic. A hand with only 2 cards, an Ace which is represented by 11 and a 10. Now, on the other hand, we could actually also simplify this, because a hand with only 2 cards that must contain an 11 and a 10, we can instead of checking for both 11 and 10, we can check to see if the total... So if we summed the cards, and if this was equal to 21, then it would be exactly the same thing, right? 10 + 11 is 21, and we&#x27;ve still only got a deck of 2. In this case, what we want to happen is we want to return 0 instead of the actual score. So this way we can indicate that the user or the computer has got a score of Blackjack. That&#x27;s Hint Number 7 sorted, let&#x27;s move on to Hint Number 8. It tells us that inside calculate_score(), we should check also for an 11, which is an Ace. If the score is already over 21, then we should remove the 11 from the cards and we could replace it with a 1, because remember that an Ace can count as an 11 or a 1. So in the beginning, when the user&#x27;s score is very small, then we probably want to count it as an 11, but once the user goes over 21, then we probably want to change it and count it as a 1 instead, so they don&#x27;t go over and they don&#x27;t lose. Let&#x27;s first write the if statement. So if there is the 11 inside our deck of cards and the sum of the cards, so the total score, is already over 21, then we want to do something about it. And the hint tells us to look up the append() and remove() functions. So we&#x27;ve already seen the append() function many times, and we know that it just adds a single element to the end of the list. Now, the one that we haven&#x27;t used a lot of, is the remove() function, and this will search for the first instance of the given element and removes it out of the list. This is kind of what we need to do. We need to go ahead and remove the 11 from the list of cards, so we can write cards.remove(), and inside the parentheses we use the 11. And then we do cards.append() so that we end up adding a 1 instead of the 11. This way we remove the 11 and we replace it with a 1, and hopefully, our cards will now take the user to below 21.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 2 | **List .append() method** | Introduced/used in this lecture |

---
