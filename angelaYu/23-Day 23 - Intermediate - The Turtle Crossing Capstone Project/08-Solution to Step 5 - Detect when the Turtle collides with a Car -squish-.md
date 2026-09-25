# 🔧 Solution to Step 5 - Detect when the Turtle collides with a Car *squish*

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 23 - Intermediate - The Turtle Crossing Capstone Project
**Lecture:** Solution to Step 5 - Detect when the Turtle collides with a Car *squish*
**Level:** Intermediate

---

### Summary

Now in the last lesson we created these rectangular cars randomly along the Y- axis. And then we managed to get them to move across to the left side of the screen. The next step is to detect when the turtle collides with the car. So that way, when the turtle hits one of the cars, we can stop the game and prevent further cars from moving. Inside our while loop I&#x27;m going to detect the collision with the car here. So I&#x27;m going to get hold of all the cars in the car_manager object and I&#x27;m going to use a for loop to loop through each of the cars in that list of cars. And then we&#x27;re going to detect whether if the car has a distance to the player object that is less than 20. Remember that our cars are 20 pixels in height by 40 pixels in width. If the player is less than 20 pixels from the center of the car, then it probably means that it&#x27;s collided with the car. So if this distance is less than 20, then we&#x27;re going to stop the game. And the way that we stopped the game is of course, by turning this game_is_on from true to false. Let&#x27;s run our code again and let&#x27;s see this in action. So we can move our turtle, we&#x27;ve got randomly generated cars moving across and let&#x27;s just park our turtle right here. When that car hit our turtle it immediately stopped the game. Now, if we want to take a look at what&#x27;s happening so for the screen to stay open instead of closing once the process is finished, we can tell it to exitonclick. So now let&#x27;s run our code again and notice this time if we collide with one of the cars you can see that it stops and it waits for further instruction, which eventually is going to be just the game over text showing up on screen and we also the final level showing up on screen. That&#x27;s it. That&#x27;s how we detect collision between the car and our player.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **while loops** | Introduced/used in this lecture |
| 2 | **if/elif/else conditionals** | Introduced/used in this lecture |

---
