# 🔧 How to create your own Class in Python

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 17 - Intermediate - The Quiz Project & the Benefits of OOP
**Lecture:** How to create your own Class in Python
**Level:** Intermediate

---

### Summary

Throughout all of yesterday, we&#x27;ve been using other people&#x27;s Classes, and we said that a class is simply just a Blueprint for creating an eventual object. In this lesson, we&#x27;re going to talk about how we can create our own classes. So our own blueprints, which we can use to create our own objects. Now let&#x27;s go ahead and create our own custom classes in code. Go ahead and create a new project and we&#x27;re going to name it day-17-start. And then hit create. And again, as always, once you&#x27;ve created your project, it&#x27;s time to create your first file, which we&#x27;re going to name main.py. And then we can collapse our project sidebar and focus on the code. So how do we create a class? The syntax looks very simple. You have the &#x27;class&#x27; keyword followed by the name of your class, and then a semicolon. And then all of the code that&#x27;s in your class will follow this and it will be indented. Let&#x27;s create our very first class in Python. As I mentioned, the way that we would create a class is first by using the &#x27;class&#x27; keyword, and then we get to give our class a name. Let&#x27;s say that we&#x27;re building a website, and we need a class to model our website&#x27;s users. So this class is basically going to be the blueprint to represent what our users have and what they can do on our website. So let&#x27;s call our class, User, and then we finish this declaration with a semicolon as usual. And everything else that&#x27;s going to go inside this class is going to need to be indented after the semicolon. Let&#x27;s start out with a completely empty class. Our User class is going to do absolutely nothing for now. However, because I&#x27;ve created my blueprint, I can already use it to create my first User object. So let&#x27;s say I wanted to create a user_1, and I&#x27;m going to create it using that class which notice it&#x27;s now being recognized by PyCharm, and it&#x27;s got the C symbol next to it. And of course to initialize an object from a class we have to add the parentheses at the end. Now we get an error here because there&#x27;s an indent expected. So basically Python doesn&#x27;t like it when you create something like a class or when you create something like a function and you have a semicolon, but you don&#x27;t have anything inside that function or class. For example, if I just immediately wanted to print(&quot;hello&quot;), afterwards, I get exactly the same error, Indent Expected. It&#x27;s expecting this a function that you&#x27;ve created, or this class you&#x27;ve just created to have some sort of content before you go ahead and do something else. So how can we fix this? Well, if we actually really want to leave this function or this class empty, we can use a keyword which is &#x27;pass&#x27;. And all it does is it just passes. It says, I don&#x27;t want to have a go right now. Just continue to the next line of code. And this gets rid of our errors both in the function declaration, as well as in our class declaration. We&#x27;ve now essentially completed the first step towards creating our custom classes, which is writing the declaration, and then building an object called user_1 out of that class. And we&#x27;ve also seen how to name classes in Python. Now, the name of the class should have the first letter of every word capitalized, and this particular style of naming in programming is known as PascalCase. So if you think of Blaise Pascal as a person, then we know that everybody&#x27;s name, every person&#x27;s name, has the first letter capitalized and also the first letter of their surname or their middle name, and basically every subsequent name capitalized. Now, this is different from another type of casing which you may have come across, which is called camelCasing. And camel casing is only different from pascal case because the first word is lowercase, but every subsequent word has its first letter capitalized in exactly the same way as pascal case. And finally, we&#x27;ve also come across snake_case, where all the words are lowercase, but they&#x27;re separated by an underscore. In Python programming, you won&#x27;t see a lot of camel casing. You will see pascal case being used for the class names, snake_case being used pretty much to name everything else.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **print() function** | Introduced/used in this lecture |
| 2 | **Class definitions (class)** | Introduced/used in this lecture |
| 3 | **if/elif/else conditionals** | Introduced/used in this lecture |

---
