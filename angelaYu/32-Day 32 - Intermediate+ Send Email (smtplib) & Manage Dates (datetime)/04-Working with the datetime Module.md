# 📖 Working with the datetime Module

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 32 - Intermediate+ Send Email (smtplib) & Manage Dates (datetime)
**Lecture:** Working with the datetime Module
**Level:** N/A

---

### Summary

In this lesson, I want to talk to you about the Python datetime module. This is a really useful module that helps us work with dates and time. Going back to our day 32 start project, I&#x27;m going to comment out everything that&#x27;s there. And then I&#x27;m going to import our datetime module. Now, again, this is the module that comes preloaded with Python so you don&#x27;t have to install it. Now, one of the most useful things to get with daytime is the current date and time. And you can write Python code to get that from the computer. Inside this date time module, there is a class called datetime as denoted by the c here. And this is how you get to that class. So to get to that class, you tap into the datetime module and then you get to the datetime class. Now this is really confusing. So I prefer to rename the datetime module and give it a as so we can shorten it to just dt. And that way we can say dt.datetime and that looks a little bit more easier to understand than before. Nnow, inside this datetime class, there is a method called now, and this gets you the current date and time. So if we save this into a variable called now, and we go ahead and print now, then when I run this code, you can see it prints a very long string showing you the current year, month, day, as well as time in my local time zone with a high degree of accuracy here. Working with that particular string is not very easy. If you wanted to check something like if now is the year 2020, then you can&#x27;t really do that with just a string like that. That&#x27;s why once you&#x27;ve gotten the now object out of this method because this method of course returns and it gets saved inside here, then we can tap into some of its attributes. So for example, we can tap into the year. So let&#x27;s save that has the year. And if I print that, you can see it just gives us the year as a number. And if I do a type check on that, you can see that it has a class of integer whereas if I do a type check on now it has a class of a datetime object. So this way, if we managed to get hold of the year as a number, then we can say something like, well, if the current year is equal to 2020, then we will print something like, and because this rings out as true, then that gets printed out. In addition to the year, we&#x27;ve also got month, day, hour, minutes. So you can basically tap into anything in that date time string as you need. So when you write &#x27;now.&#x27; you can see that there&#x27;s the year, day, month, hour, minutes, microsecond, second, and you can get to the specific part of that datetime that you need. You can even call other methods like weekday. For example, if we want to know which day of the week it is, so Monday, Tuesday, Wednesday, then we can simply tap into now and call this weekday method. And now if we print out this day of the week, you can see that it gives us a number. So it remember that computers start counting from zero so 1 means that its actually the second day of the week, which is Tuesday as you can see up here. So we&#x27;ve seen how we can get hold of the current day, year, month and whichever property you&#x27;re interested in for today. But what if we wanted to create a daytime object of our own setting it to a particular date of our choosing? Well, let&#x27;s say that I wanted to create a object that stored my date of birth. Well then I would tap into the dt module and create a new datetime object from that class. Now I get to specify, well, what is the year? What is the month? What is the day? And I can even go even more specific like which hour was I born in? And you&#x27;ll notice that in here, when you look at the parameters, the year requires an integer, the month requires an interger and the day requires an integer. But after the hour we&#x27;ve got this ... as does the minute and the second and this is because they have default values. So if I delete this, the only things I&#x27;m required to give when I&#x27;m creating a new datetime object is the year, month and day. Let&#x27;s say that I was born in 1995 and I was born in December the 15th. All right. Now, if I print this date of birth object you can see that we get 1995, 12, 15, and the time in hour, minute and second are set to the default values of zero. If I wanted to be more specific and I wanted to set my hour of birth, let&#x27;s say I was born at 4:00 AM, then we can set the hour and that updates that default value. So now we&#x27;ve seen how we can tap into the current date time and also create any datetime object from scratch then it&#x27;s time to put this into practice and use it in our project.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **Class definitions (class)** | Introduced/used in this lecture |
| 2 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 3 | **Module imports** | Introduced/used in this lecture |
| 4 | **datetime module** | Introduced/used in this lecture |

---
