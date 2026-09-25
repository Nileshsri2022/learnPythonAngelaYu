"""Day 26 project: NATO Alphabet — spell any word in NATO code words.

Requires nato_phonetic_alphabet.csv (letter,code) in the same folder.
"""

import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Dictionary comprehension: {letter: code}
phonetic_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet, please.")
else:
    print(output_list)
