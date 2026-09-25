"""Day 14 project: the Higher Lower Game."""

import os
import random

from game_data import data


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


LOGO = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __ / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
        /____/        __    
   ____  _____________/ /___
  / __ `/ ___/ ___/ __  / __ \
 / /_/ / /  / /  / /_/ / /_/ /
 \__, /_/  /_/   \__,_/\____/ 
/____/                        
"""

VS = r"""
     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____/  
"""


def get_random_account():
    """Return a random account (dict) from the data."""
    return random_choice()


def random_choice():
    import random
    return random.choice(data)


def format_data(account):
    """Format an account dict into a printable description."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Return True if the guess matches the account with more followers."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()

    while game_should_continue:
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(LOGO)
        print(f"Compare A: {format_data(account_a)}.")
        print(VS)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, a_followers, b_followers)

        clear_screen()
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
