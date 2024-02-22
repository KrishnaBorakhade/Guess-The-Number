import random as r
import logo
EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5

def set_difficulty(level_choosen):
    if level_choosen == 'easy':
        return EASY_LEVEL_ATTEMPT
    else:
        return HARD_LEVEL_ATTEMPT

def check_ans(guessed, answer, attempted):
    if guessed < answer:
        print("Your guess is too low.")
    elif guessed > answer:
        print("Your guess is too high.")
    else:
        print(f"Your guess is right... The answer was {answer}")
        return True
    return False

def game():
    print(logo.logo)
    print("Let me think a number between 1 to 50")
    ans = r.randint(1, 50)
    level = input("Enter the level of difficulty... Type 'easy' or 'hard' : ")
    attempts = set_difficulty(level)
    
    while attempts > 0:
        print(f"You have {attempts} remaining attempts to guess the number.")
        guess = int(input("Guess a number : "))
        attempts -= 1
        if check_ans(guess, ans, attempts):
            return
        elif attempts == 0:
            print("You are out of guesses... You lose!")

game()
