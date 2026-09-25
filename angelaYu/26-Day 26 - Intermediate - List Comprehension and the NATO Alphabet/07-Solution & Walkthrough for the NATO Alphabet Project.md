# 🔧 Solution & Walkthrough for the NATO Alphabet Project

---

### Overview

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp
**Chapter:** Day 26 - Intermediate - List Comprehension and the NATO Alphabet
**Lecture:** Solution & Walkthrough for the NATO Alphabet Project
**Level:** Intermediate

---

### Summary

Once you&#x27;ve unzipped and opened up the starting file inside PyCharm, this is what you&#x27;d see. There is a CSV file that contains each of the letters and the code word, and there&#x27;s also our main.py with some of the example code that I showed you in the last lesson. Now, if you don&#x27;t know how to complete this challenge, especially step 1, I really urge you to go through this example code and just go through each of the different types of loops and see what it is that you get when you print the key or the value. And in this case, when you print the index or when you print the row. And then see what happens when you get hold of some of the items in the row. And seeing how maybe the row.student or the row. score works. Once you fully understood this, then it should be relatively easy to complete step 1. So essentially the goal is that we want to create a dictionary that looks like this from the CSV. The first thing we have to do is to go ahead and import pandas. And if you need to install it, there should be a squiggly line and then you can click on it and the light bulb will help you install the pandas module. But once we&#x27;ve gotten hold of the pandas, we can go ahead and use it to read CSV from our file which is this file. It&#x27;s under the file path of just nato_phonetic_ alphabet.csv. So it will save this as our data which is basically going to be our data frame. Now, once we&#x27;ve got hold of our data, then you can see that if we print this out, it looks like this. But if we use that method, to_dict, and then we try to print it out, you can see that it&#x27;s not organized the dictionary in the format that we want it to, which is to have the letter as the key, the corresponding code as the value. In order to complete step 1 as I mentioned, we&#x27;re going to have to use dictionary comprehension. And the method is going to be using the iterrows to iterate through each of the rows inside that data frame. So I&#x27;m going to copy that line here, and I&#x27;m going to paste it in here. Now, this is the format, so let&#x27;s go ahead and replace each of the keywords. Our data frame, in our case, is just called data. And then we&#x27;re going to say data iterate through each of the rows, and then for each of the index and the row, we&#x27;re going to do something with it. Now the new key is going to be the row.letter and the new value is going to come from that row as well and it&#x27;s going to be row.code. So this is the code that will create our new dictionary and I&#x27;m going to call this our phonetic_dictionary. Now, if I print that out, you can see that this is the straight up data.to_dict and then the second line is the one where we&#x27;ve actually formatted it using what we&#x27;ve learned about dictionary comprehension. Once we&#x27;ve gotten hold of this phonetic dictionary, then to do step 2 is incredibly easy because all we have to do is to create some sort of inputs, ask the user to enter a word, and then we can save this input to a variable. Now, once they&#x27;ve entered the word, we have to check it against each of the keys inside this phonetic dictionary. So notice how each of the keys all uppercased. So we&#x27;re going to have to change whatever it is that the user has inputted all to upper. So that way, if they entered a lowercase or an uppercase, it doesn&#x27;t really matter because we&#x27;re going to convert the whole string to uppercase. And then we&#x27;re going to use our list comprehension. The way we create our list comprehension is going to be new item for item in list. So in this case, our list or the thing that we&#x27;re going to iterate through is going to be our word. And then we&#x27;re going to go through each of the letters in the word. And once we have each of the letters, we&#x27;re going to go through our phonetic dictionary, this one right here, and pick out the value that corresponds to the particular letter that we&#x27;re iterating on. So we&#x27;re going to use the square brackets and then pass in the letter like this. Now we&#x27;ve created our output list and we can go ahead and print it out. Now let&#x27;s go ahead and comment out this line and run our code. So it&#x27;s going to ask me to enter a word, I&#x27;m going to enter my name. And now it&#x27;s managed to convert that into a list of phonetic alphabets that corresponds to each of the letters in that word. Did you manage to complete this challenge? And if not, which part did you stumble on? Was it the part where you were using the iterrows? If so, then go back to the starting file for this project and go through each of the different ways that we&#x27;re looping through it and use print statements to really understand how the loop is actually going through and looking through the data. Now, if on the other hand, it was the dictionary comprehension or the list comprehension, then be sure to go back to the relevant lesson and just make sure that you review it and you write out the code in the lesson for yourself just to be sure that you understand what&#x27;s going on before you continue to the next day.

---

### Key Concepts

| # | Concept | Description |
|---|---------|-------------|
| 1 | **for loops** | Introduced/used in this lecture |
| 2 | **if/elif/else conditionals** | Introduced/used in this lecture |
| 3 | **Module imports** | Introduced/used in this lecture |
| 4 | **List comprehensions** | Introduced/used in this lecture |
| 5 | **Pandas library** | Introduced/used in this lecture |

---
