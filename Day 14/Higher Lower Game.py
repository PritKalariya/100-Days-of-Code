import random
from typing import Counter
from game_data import data
from art import logo, vs
from replit import clear


def get_random_account():
    """Get a random account from data"""
    return random.choice(data)

# print(get_random_account())

def format_account_data(account):
    """Format the account details in printable form: name, description and country"""
    name = account["name"]
    description = account["description"]
    Country = account["country"]
    # print(f"{name}: {account['follower_count']}")
    return f"{name}, a {description} from {Country}."

# format_account_data(get_random_account())

def check_answer(guess, a_follower, b_follower):
    """Chcek if the user guessed the correct option"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)

    score = 0
    continue_game = True
    option_a = get_random_account()
    option_b = get_random_account()

    while continue_game:
        option_a = option_b
        option_b = get_random_account()

        while option_a == option_b:
            option_b = get_random_account()

        print(f"Compare A: {format_account_data(option_a)}")
        print(vs)
        print(f"Compare B: {format_account_data(option_b)}")
            
        user_guess = input("\nWhich one has more instagram followers? Type 'A' or 'B': ").lower()
        a_follower_count = option_a["follower_count"]
        b_follower_count = option_b["follower_count"]

        is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"You are correct. Current score: {score}.")
        else:
            continue_game = False
            print(f"Oops! That's wrong. Final score: {score}.")


game()