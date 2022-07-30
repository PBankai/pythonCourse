from operator import truediv
from secrets import choice
from turtle import clear
from art import logo, vs
import random
from game_data import data


def get_option():
    """Select a random option from game data"""
    return random.choice(data)


def print_option(option):
    """Format the option as a printable String"""
    name = option["name"]
    occupation = option["description"]
    from_c = option["country"]
    return f"{name}, a {occupation} from {from_c}"


def check_answer(guess, account_a, account_b):
    """Check if the answer is right and return a boolean"""
    if account_a < account_b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_option()
    account_b = get_option()
    while game_should_continue:
        account_a = account_b
        account_b = get_option()

        while account_a == account_b:
            account_b = get_option()
            print(f"Compare A: {print_option(account_a)}")
            print(vs)
            print(f"Compare B: {print_option(account_b)}")
            guess = input("Who has more followers A or B : ").lower()
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]
            guess_result = check_answer(guess, a_follower_count, b_follower_count)
            clear()
            print(logo)
            if guess_result:
                score += 1
                print(f"You're right current score: {score}")
            else:
                game_should_continue = False
                print(f"That's not right  you're final score was {score}")


game()
