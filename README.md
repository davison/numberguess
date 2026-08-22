# numberguess

A single-round command-line number guessing game built as a test project for
Codecrew.

## Play

Python 3.9 or newer is required. Run:

```console
python3 numberguess.py
```

The game chooses an integer from 1 to 100. Enter guesses until you find it;
the game reports whether each valid guess is too high or too low. Invalid and
out-of-range entries do not count as attempts. The program reports the final
attempt count and exits after a correct guess.

## Test

The test suite uses only Python's standard library:

```console
python3 -m unittest
```
