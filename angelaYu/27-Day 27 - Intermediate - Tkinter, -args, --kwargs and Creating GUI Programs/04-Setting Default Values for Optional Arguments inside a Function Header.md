# 🔧 Setting Default Values for Optional Arguments inside a Function Header

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs
**Lecture:** Setting Default Values for Optional Arguments inside a Function Header
**Level:** Intermediate

---

### Summary

In the last lesson, we saw how different it was when we tried to use the turtle&#x27;s write function and we saw all of the arguments available listed, versus when we tried to use the Tkinter label&#x27;s pack method, and notice how there&#x27;s actually very few arguments that are listed. And yet, somehow there&#x27;s all of these parameters that we can change when we look at the documentation, like expand or side. So let&#x27;s set that side to equal left, and I&#x27;m going to delete the rest of the turtle code. And now you can see our label is placed on the left side of our screen. How is it that these parameters, even though they&#x27;re not listed in the list of properties, how is it that we&#x27;re able to use them just by typing them in? Well, to understand this, we have to learn a bit more about advanced arguments. Not how to argue better, but how to use advanced Python arguments in order to specify a wider range of inputs. We&#x27;ve already seen how keyword arguments work. For example, here I have a function and I have three keyword arguments, a, b, and c. And when I call the function, I can provide those inputs, a, b, and c in any order I want as long as I&#x27;ve got the keyword in front. So c = 3, a = 1, and b = 2. Now what if when I use this function, it&#x27;s nine out of ten times, a is going to be equal to 1, b is 2 and c as 3. Why is it that when I call the function, I always have to put in these values? That seems a bit of a wasted effort, right? Python has a very neat way of solving this by creating arguments that have default values. We can do this by simply changing the function declaration. So when we create our function, we can already give it some values to start off with. So we can say that a should be equal to 1, b = 2 and c = 3, and these are the default values. So that means when I call this function and I want to use the default values, I don&#x27;t actually have to provide any inputs and it will just go along as it would before. Now, if, however, I wanted to modify one of those inputs, let&#x27;s say I wanted to give a custom value for b rather than let it be equal to the default value of 2, well, then I can just change the value of b, b = 5. And the rest, so a and c, will still take on their default values. Notice when I called tim.write, this write method takes five inputs; self, because it&#x27;s a method and associated with the turtle class, it takes an argument which is what it is going to write, move, align and font. Now, if I wanted to use tim.turtle to just write some sort of text, I can actually just put in this. And when I run this code, you&#x27;ll see that I&#x27;ve got some piece of text being written. But how is it that I&#x27;ve got all of these other inputs which I&#x27;ve just basically completely ignored? What about move? What about align? What about fonts? Well, as you can see, they have the =..., which is trying to tell you that they&#x27;ve already got a default value. And in fact, if I hover over this write function, you can see that in the quick docs that pops up, it tells me that the argument, or the arg, which is what it is to be written to the screen, move which is optional which can be set as true or false, align which is optional, font which is optional. The reason why they&#x27;re optional is because all of these actually have a default value. For example, move, by default, is false; align by default is centered, and there&#x27;s also a default font. So that means that all we have to do is just to provide the required arguments. If I don&#x27;t add anything at all when I call this write method, you can see I do in fact get an error here. And it says write is missing one required positional argument, which is that first arg which is the thing that it&#x27;s expecting to write. I mean, if you&#x27;re calling turtle to do some writing and you not telling it what to write, that&#x27;s a bit of a problem. So this ARG is a required argument because it doesn&#x27;t have that =... at the end. So this you have to provide. But once you&#x27;ve done that, then the rest of them all have default values. They already know how to behave and what to do even if you don&#x27;t tell them anything extra. Now, however, if you wanted to modify one of those arguments, let&#x27;s say I decide to change the font to something completely different like Times New Roman, and make the font super large 80 size font and change it to bold, then you can see that that optional setting gets implemented and it&#x27;s now changed the font and its changed the size and also made it bold. But this was completely optional. And this is all down to creating the function with default values.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 2 | **Tkinter GUI framework** | Introduced/used in this lecture |

---
