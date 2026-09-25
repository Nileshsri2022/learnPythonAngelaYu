# 🐍 Hint 9 Solution Walkthrough: Refactoring and calling calculate_score()

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 11 - Beginner - The Blackjack Capstone Project
**Lecture:** Hint 9 Solution Walkthrough: Refactoring and calling calculate_score()
**Level:** Beginner

---

### Summary

Now let&#x27;s move on to Hint 9. So we want to call calculate_score() at some point in our code, and if the computer or the user has a blackjack, or if the user&#x27;s score is over 21, then the game is going to end. This might be a good time to start tidying up our code a little bit, because we&#x27;ve got our function over here, the calculate_score() function, and remember that you can only call a function after it&#x27;s been declared. So for example, if I wanted to call this function over here, then I actually can&#x27;t. I can&#x27;t say, calculate_score() because it hasn&#x27;t yet been declared. So instead what I&#x27;m going to do is I&#x27;m going to take this function, and I&#x27;m going to move it to where we dealt our cards. So now that I&#x27;ve moved my function to above the line where I want to call it, it&#x27;s now become valid code. And this is the place where I want to call it, because it&#x27;s only after I&#x27;ve dealt the user and the computer some cards can I actually calculate their scores. Firstly, I want to calculate the score using the user&#x27;s cards. So this list of cards from the user gets passed into this function and uses all of the logic to output some sort of score. And then I&#x27;m going to store that score in a variable, which I&#x27;ll call user_score. And I&#x27;m going to do the same thing for the computer. So computer score = calculate_score()... and remember it&#x27;s always helpful to add a little bit of a Docstring to tell ourselves and other programmers what this function does. Let&#x27;s quickly summarize it. So this function is going to, &quot;&quot;&quot;Take a list of cards and return the score calculated from the cards.&quot;&quot;&quot; So now when I open that parentheses, I know that I probably have to pass in my list of cards in order to get back the score. And now we&#x27;ve got the user_score and the computer_score. So this score could equal 0 if they got a blackjack, or it could just simply be the value of the cards that they hold all added up together. Now that we&#x27;ve called calculate_score(), we also want to make sure that if the computer, or the user has a blackjack, or if the user scores over 21, then we have to end the game. Let&#x27;s write our if statements. If the user_score is equal to 0, or the computer_score is equal to 0, or the user_score is greater than 21, then in this case we&#x27;re going to tell the game to end. So we could create a new variable called is_game_over, and we start out with False of course, but then when this happens we&#x27;re going to change that variable to True instead. Our is _game_over variable is just a simple boolean, It starts out as False, and when certain conditions are met, then we change it to True. Now at the moment our program is not finished, so it&#x27;s not really obvious how we&#x27;re going to be using this is_game_over variable, but we&#x27;re setting ourselves up for the next steps. Now that we&#x27;re tracking if the game should end, we can look at this value to determine what to do next. So that&#x27;s Hint 9 completed. Let&#x27;s test our code and see how everything works so far. I&#x27;m going to add some print statements here so that I can see what the user&#x27;s cards are, and what the user&#x27;s score is. Using an f-string I&#x27;m going to show, &quot;Your cards,&quot; so the user&#x27;s cards, and the &quot;current score&quot;. And I&#x27;m also going to print the, &quot;Computer&#x27;s first card.&quot; Remember when I first explained the rules of Blackjack? The dealer will reveal their first card, so you get a little bit of a clue as to what kind of hand they might have. So in here, we&#x27;re going to insert the computer&#x27;s cards, and we&#x27;re only going to pick out the first item. So the one at index 0, and we do that using a square bracket after the name of the list. Let me just change that typo there. And now we&#x27;re ready to give this program a run to see how it works. Now we&#x27;ve got our first cards showing which is the user_cards, and it&#x27;s a list of two cards, a 3 and a 2. A 3 and 2 adds up, of course, to 5. So the current score for the user is 5. Next, it shows us the computer&#x27;s first card, and that is a 4. Now we can be reasonably assured that our code is working, and it&#x27;s a good idea to regularly test your code so that you don&#x27;t wait until the end, when there are a lot of problems and you don&#x27;t know which part of the code is responsible.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |

---
