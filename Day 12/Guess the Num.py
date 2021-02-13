import random
from art import logo

hard_level_turns = 5
easy_level_turns = 10
number = random.randint(1, 50)

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


# The diffiuclty
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return easy_level_turns   
    else:
        return hard_level_turns


def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 to 50. Can you guess it?")
    
    # testing
    print(f"Psst the number is {number}")

    chances = set_difficulty()
    guess = 0

    while guess != number:
        print(f"Youo have {chances} chances remaining to guess the number.")

        # User input
        guess = int(input("Make a guess: "))

        chances = check_answer(guess, number, chances)
        if chances == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")

game()