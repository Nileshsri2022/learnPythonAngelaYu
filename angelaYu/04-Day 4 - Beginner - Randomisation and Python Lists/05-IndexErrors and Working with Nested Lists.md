# 🐍 IndexErrors and Working with Nested Lists

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 4 - Beginner - Randomisation and Python Lists
**Lecture:** IndexErrors and Working with Nested Lists
**Level:** Beginner

---

### Summary

Now, when you&#x27;re working with lists, one of the most common errors you&#x27;ll come across is something called the index out of range error. In fact, by this point, you might have already seen it. Now, what does it mean though? Well, let&#x27;s take our states_of_america, and you might remember that there are 50 states in America, but if you don&#x27;t, because you&#x27;re a programmer, it&#x27;s as easy as writing, len(), and then passing over the states_of_america, which will print 50. So now that we know that there are a total of 50 items in this list, and remember, because we start counting from 0, Hawaii is actually at index 49. So if we print states_of_america and then we try to get the item at 49, we hit print, you&#x27;ll see that we get Hawaii printed. Now what if we went one beyond that? What if we tried to get the one at index 50? What do we get instead? Well, we get an error. It&#x27;s called an IndexError. And this is because it&#x27;s beyond Hawaii and there&#x27;s nothing there, as we can see with our own eyes. But when you&#x27;re working with large lists and you&#x27;re not always looking at the data, then these errors can be a little bit more confusing. Very frequently when you&#x27;re working with lists, you&#x27;ll end up with an off-by-one error. So it&#x27;s unusual that you&#x27;ll try to get something at index number 90, because that&#x27;s just way beyond your list size, but very frequently you might end up in a situation where you have some sort of value, say number_of_states = len(), and then we pass over the states_of_america. So this is going to be equal to 50. And then we pass that inside here as the index num_of_states, and then we hit Run, and we get the same error, right? In this list. It&#x27;s again list index out of range. And this is an off-by-one error because all we need to do is just simply -1, so that 1 becomes 0, and 50 becomes 49. And then we get rid of that error. Now it might be easier if we work with something a little bit simpler. Recently I was reading online, and I came across the so-called &quot;Dirty Dozen,&quot; where the Environmental Working Group, a bunch of people crunched through a whole lot of data, probably using Python, and they released their Dirty Dozen, a list of the fruits and vegetables that have the most pesticides. And it&#x27;s kind of crazy that they actually washed and peeled all of these foods and then tested them for pesticides. And the list looks something like this, where strawberries are apparently one of the worst offenders for pesticides. So let&#x27;s create a list of the dirty_dozen. But you&#x27;ll notice that some of these are fruits like strawberries, apples, and other ones are vegetables. So how can we use our lists to still keep them inside the same sort of container? The dirty_dozen, but somehow separate them out into fruits and vegetables? Well, we could just simply create two lists fruits and vegetables. But these two lists kind of have a relationship, right? They&#x27;re kind of related because they&#x27;re all on the list of high pesticide foods. So how can we have lists within a list? Well, that&#x27;s what&#x27;s called a nested list. Instead of our original dirty_dozen, we could create a new list called dirty_dozen, and we set it equal to a list that contains two lists. It contains fruits and it contains vegetables. So now what effectively has happened is we&#x27;ve inserted this list inside here, and then we&#x27;ve inserted this list inside here. So we now have a list that contains two lists. And if I go ahead and print out this list you&#x27;ll be able to see its structure. And it looks like this. You&#x27;ll notice that there&#x27;s two brackets at the beginning and at the end. And the reason is because this is one list, this is another list, and this is also a list. So this is yet another way of using lists and just showing you the flexibility of this particular data structure. It&#x27;s something that you&#x27;re going to use a lot when you&#x27;re writing Python code.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 2 | **len() function** | Introduced/used in this lecture |

---
