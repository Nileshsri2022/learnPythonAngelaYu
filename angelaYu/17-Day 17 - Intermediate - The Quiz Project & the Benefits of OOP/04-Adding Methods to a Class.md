# 🔧 Adding Methods to a Class

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 17 - Intermediate - The Quiz Project & the Benefits of OOP
**Lecture:** Adding Methods to a Class
**Level:** Intermediate

---

### Summary

In addition to creating attributes, we know that we can also create methods. The attributes are the things that the object has and the methods are the things that the object does. Let&#x27;s say that we were creating the car class and we&#x27;ve really created the seats attribute. Well, later on we might decide that we want to call a method to change that seats attribute&#x27;s value. So for example, I&#x27;ve been watching a lot of truck racing recently. Yeah. [inaudible] And one of the things that people do when they mod their cars for racing is they take out some of the seats. This way it reduces the weight of the car, and it means that you can go a bit faster. So in our car class, we might, in fact, have a method where the car can enter race mode, where the seats are dropped from 5 to 2. This is what the method would look like. Inside the class declaration, we have a function, but remember when a function is attached to an object then it&#x27;s called a method. This method looks exactly the same as how we&#x27;ve created other functions. We have the Def keyword, we have the name of the method, we have some parentheses which can take inputs, a colon, and then the body of the method. So in this case, all it does is it gets hold of the object and then the object seats attribute and then changes it to 2. So now when you call that method, all you need to do is get hold of the object and then you use the dot notation to call that method enter_race_mode, and of course, with the parentheses at the end. So let&#x27;s say that while we&#x27;re modeling our Instagram user, we want to have a way for the users to follow each other, right? And when they follow each other, their follower counts obviously go up. So let&#x27;s define a new method. So we&#x27;re going to use the def keyword and then we&#x27;re going to name our method follow. Now a method, unlike a function, always needs to have a self parameter as the first parameter. This means that when this method is called, it knows the object that called it. Now, in addition to that self parameter, we&#x27;re also going to pass in the user that we&#x27;ve decided to follow. So now let&#x27;s say that we actually had two attributes, the followers and the following count, right? So they both start from zero, so two default attributes. But when a user decides to follow another user, well in this case, the user who we&#x27;re following, their follower count goes up by one and our own, so the self.following count goes up by one as well. So the self keyword becomes quite important when we&#x27;re working with classes and objects. It&#x27;s a way for us to refer to the object that&#x27;s going to be created from this class inside the class blueprint. So you&#x27;ll never see self when you&#x27;re using objects but you see it a lot when you&#x27;re writing your code inside your class. Now let&#x27;s go ahead and call this. And let&#x27;s say that user_1 decided to follow user_2. This is the user_1 object, and this is the follow method from the user_1 object. And then the user_2 is the person who we&#x27;re going to follow. So now let&#x27;s go ahead and print the user_1&#x27;s follower count and the user_1&#x27;s following count. And let&#x27;s do the same for user_2 as well. You can see once this method has run, then user_1&#x27;s follow account is still zero, but user_1 is now following one person. User_2 has one followers and has zero people that it&#x27;s following. Right?

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **Function definitions (def)** | Introduced/used in this lecture |
| 2 | **Class definitions (class)** | Introduced/used in this lecture |
| 3 | **while loops** | Introduced/used in this lecture |

---
