#  Number Guessing Game
# This program generates a random number and lets the user guess it
# Concepts: loops, conditions, random module

import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break

print("Total attempts:", attempts)
