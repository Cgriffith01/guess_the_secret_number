#
#SEC290.13767.FA2022
#Christine Griffith
#Hwk #3
#

import random

number = random.randint(1, 20)
guess = None

num_lives = 3

print("Guess the secret number!")
print("You start out with 3 lives and you lose one with each wrong guess.")

while num_lives != 0:
    guess = input("Guess a number between 1 and 20: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a whole number between 1 and 20.\n")
        continue

    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.\n")
        continue

    if guess > number:
        print("Too High! Try again.")
        num_lives -= 1
        print(f"\nTotal lives remaining: {num_lives}\n")

    elif guess < number:
        print("Too Low! Try again.")
        num_lives -= 1
        print(f"\nTotal lives remaining: {num_lives}\n")

    else:
        print(f"Congratulations! YOU WIN! You guessed the secret number {number}!")
        break

if num_lives == 0:
    print(f"The correct number was {number}.")
    print("Better luck next time!")

print("Have a great day!")
