# M1: Playable number guessing game

## Goal and outcome

M1 set out to deliver a tested Python CLI game that chooses an integer from 1
to 100, accepts guesses until the player succeeds, provides directional hints,
rejects invalid input, reports the valid-guess count, and exits after one game.

The milestone delivered that behavior in
[PR #3](https://github.com/davison/numberguess/pull/3). The implementation is a
standard-library-only Python module with a direct CLI entry point, deterministic
unit tests, a GitHub Actions test workflow, and player instructions in the
README. The human operator independently played the game and
[recorded a satisfied QA verdict](https://github.com/davison/numberguess/issues/1#issuecomment-5382567575)
for every requirement.

## Decisions

### Testable boundaries without third-party dependencies

The game function accepts input, output, and secret-selection callables rather
than binding all behavior directly to the terminal and random-number generator.
This small increase in the function's interface makes tests deterministic and
allows them to exercise a whole game without subprocess control or randomness
patching. A shell implementation and exclusively subprocess-driven tests were
rejected because their input validation and deterministic coverage would be
less clear for this first milestone. This choice was
[recorded on task #2](https://github.com/davison/numberguess/issues/2#issuecomment-5382529302).

## Deviations

The task plan called for automated testing but did not explicitly include a CI
workflow. When task completion was attempted, Codecrew refused the merge because
the branch had no reported checks. A minimal GitHub Actions workflow was added
to run the standard-library suite for pull requests and pushes to `main`. The
reason was
[recorded on task #2](https://github.com/davison/numberguess/issues/2#issuecomment-5382550066),
and the workflow passed before PR #3 was merged.

## Requirement outcomes

| Requirement | Outcome | Evidence |
|-------------|---------|----------|
| M1-R1 | Satisfied | The operator started and played a generated 1–100 game. |
| M1-R2 | Satisfied | Incorrect valid guesses produced correct high/low hints. |
| M1-R3 | Satisfied | Text and out-of-range entries were rejected without ending the game. |
| M1-R4 | Satisfied | A win reported the valid-guess count and excluded invalid entries. |
| M1-R5 | Satisfied | The process exited after the win without starting another round. |
| M1-R6 | Satisfied | Deterministic tests cover the agreed behaviors and passed in CI. |

The complete QA evidence is preserved in the
[milestone verdict comment](https://github.com/davison/numberguess/issues/1#issuecomment-5382567575).
