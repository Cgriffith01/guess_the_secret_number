# Guess the Secret Number

A command line number guessing game. The program picks a random number between 1 and 20, and you have 3 lives to guess it.

## File

- **HWK3_Christine_Griffith.py** - the full game.

## What it does

1. Picks a random secret number between 1 and 20.
2. Prompts you to guess, and gives you 3 lives to work with.
3. After each guess, tells you if it was too high or too low.
4. Each wrong guess costs one life. Guessing correctly wins the game immediately.
5. If all 3 lives run out before you guess correctly, the game reveals the number and wishes you better luck next time.

Entering something that isn't a number, or a number outside the 1 to 20 range, doesn't cost a life, it just asks you to try again.

## Requirements

- Python 3

## Usage

Run it from the command line:

```
python3 HWK3_Christine_Griffith.py
```

Then follow the prompts to guess the number.
