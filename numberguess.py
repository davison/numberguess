"""A small command-line number guessing game."""

from collections.abc import Callable
import random


MINIMUM = 1
MAXIMUM = 100


def play_game(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
    secret_picker: Callable[[int, int], int] = random.randint,
) -> int:
    """Play one game and return the number of valid guesses made."""
    secret = secret_picker(MINIMUM, MAXIMUM)
    attempts = 0

    output_fn(f"I'm thinking of a number from {MINIMUM} to {MAXIMUM}.")

    while True:
        raw_guess = input_fn("Enter your guess: ")

        try:
            guess = int(raw_guess)
        except ValueError:
            output_fn("Please enter a whole number.")
            continue

        if not MINIMUM <= guess <= MAXIMUM:
            output_fn(f"Please enter a number from {MINIMUM} to {MAXIMUM}.")
            continue

        attempts += 1

        if guess < secret:
            output_fn("Too low.")
        elif guess > secret:
            output_fn("Too high.")
        else:
            noun = "attempt" if attempts == 1 else "attempts"
            output_fn(f"Correct! You guessed the number in {attempts} {noun}.")
            return attempts


def main() -> None:
    """Run the command-line game."""
    play_game()


if __name__ == "__main__":
    main()
