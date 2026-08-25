# numberguess

A command-line number guessing game built as a test project for
Codecrew.

The decisions and outcomes from the first delivery are recorded in the
[M1 milestone document](docs/milestones/1-playable-number-guessing-game.md).

## Play

Python 3.9 or newer is required. Run:

```console
python3 numberguess.py
```

The game chooses an integer from 1 to 100. Enter guesses until you find it;
the game reports whether each valid guess is too high or too low. Invalid and
out-of-range entries do not count as attempts. The program reports the final
attempt count, then asks whether you want to play another round. Interactive
terminals get a colourful interface with icons; redirected output automatically
stays plain. Set the standard `NO_COLOR` environment variable to disable
decoration:

```console
NO_COLOR=1 python3 numberguess.py
```

## Test

The test suite uses only Python's standard library:

```console
python3 -m unittest
```
