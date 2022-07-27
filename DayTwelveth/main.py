from art import logo
from random import randint
continue_playing="y"
EASY_LEVEL =10
HARD_LEVEL =5
def check_answer(guess, answer,turns):
    if guess>answer:
        print("Too High")
        return turns-1
    elif answer>guess: 
        print("too Low")
        return turns-1
    else:
        print(f"you have got the answer {answer} you have won")
def set_dificulty():
    """Set the dificulty of the game base on answer"""
    level=input("which level do you want to play easy/hard: ")
    if level=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():
    print(logo)
    print("You have to guess a random number from 1 to 100")
    answer = randint(1,100)
    turns=set_dificulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} remaining to guess the correct number")
        guess= int(input("guess the number: "))
        turns =(check_answer(guess,answer,turns))
        if turns==0:
            print("You've run out of tries, you lose")
            continue_playing=input("Do you want to continue playing? y/n: ")
            return
        if answer!=guess:
            print("Try again")
        elif answer==guess:
            continue_playing=input("Do you want to continue playing? y/n: ")
            return

while continue_playing=="y":
    game()