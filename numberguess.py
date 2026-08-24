"""A small command-line number guessing game."""

from collections.abc import Callable
import os
import random
import sys
from typing import Optional, TextIO


MINIMUM = 1
MAXIMUM = 100

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"


def supports_terminal_style(stream: TextIO) -> bool:
    """Return whether a stream should receive colours and Unicode icons."""
    return (
        hasattr(stream, "isatty")
        and stream.isatty()
        and os.environ.get("TERM") != "dumb"
        and "NO_COLOR" not in os.environ
    )


def decorate(message: str, icon: str, colour: str, styled: bool) -> str:
    """Add an icon and ANSI styling when rich terminal output is enabled."""
    if not styled:
        return message
    return f"{colour}{icon}  {message}{RESET}"


def play_game(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
    secret_picker: Callable[[int, int], int] = random.randint,
    styled: Optional[bool] = None,
) -> int:
    """Play one game and return the number of valid guesses made."""
    if styled is None:
        styled = input_fn is input and output_fn is print and supports_terminal_style(
            sys.stdout
        )

    secret = secret_picker(MINIMUM, MAXIMUM)
    attempts = 0

    if styled:
        output_fn(f"{BOLD}{MAGENTA}NUMBER GUESS{RESET}")
    output_fn(
        decorate(
            f"I'm thinking of a number from {MINIMUM} to {MAXIMUM}.",
            "🎯",
            CYAN,
            styled,
        )
    )

    while True:
        prompt = decorate("Enter your guess: ", "➜", BOLD + CYAN, styled)
        raw_guess = input_fn(prompt)

        try:
            guess = int(raw_guess)
        except ValueError:
            output_fn(
                decorate("Please enter a whole number.", "⚠", YELLOW, styled)
            )
            continue

        if not MINIMUM <= guess <= MAXIMUM:
            output_fn(
                decorate(
                    f"Please enter a number from {MINIMUM} to {MAXIMUM}.",
                    "⚠",
                    YELLOW,
                    styled,
                )
            )
            continue

        attempts += 1

        if guess < secret:
            output_fn(decorate("Too low.", "↑", RED, styled))
        elif guess > secret:
            output_fn(decorate("Too high.", "↓", RED, styled))
        else:
            noun = "attempt" if attempts == 1 else "attempts"
            output_fn(
                decorate(
                    f"Correct! You guessed the number in {attempts} {noun}.",
                    "🎉",
                    BOLD + GREEN,
                    styled,
                )
            )
            return attempts


def main() -> None:
    """Run the command-line game."""
    play_game()


if __name__ == "__main__":
    main()
