import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Create the blanks — done ONCE, before the game loop, so revealed letters persist.
display = []
for _ in range(word_length):
    display += "_"

print(f"Psst, the solution is {chosen_word}.")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check the guess against every position of the chosen word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # A wrong guess costs a life.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("****************************")
            print("You lose.")
            print(f"The word was {chosen_word}.")

    # Join the display list into a readable string.
    print(f"{' '.join(display)}")

    # Check whether the player has won.
    if "_" not in display:
        end_of_game = True
        print("****************************")
        print("You win.")

    print(stages[lives])
