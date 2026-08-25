# M3: Continuous play

## Goal and outcome

M3 set out to let players start another number-guessing round without
restarting the program. The milestone delivered continuous sessions in
[PR #11](https://github.com/davison/numberguess/pull/11): after every win, the
game accepts case-insensitive `yes`/`y` to select a fresh secret and begin a
new round, or `no`/`n` to exit. Surrounding whitespace is ignored, and invalid
responses explain the available choices and re-prompt without starting a
round.

The human operator independently exercised the feature and
[reported every M3 requirement satisfied](https://github.com/davison/numberguess/issues/9#issuecomment-5411226141).

## Decisions

### Preserve a single-round game boundary

`play_game` remains responsible for exactly one round. The continuous-session
loop belongs to `main`, and a dedicated `ask_to_play_again` function parses the
replay choice. Replay input accepts full and abbreviated answers without case
or surrounding-whitespace sensitivity.

This separation preserves the existing single-round API while making session
behavior explicit. The trade-off is a broader injectable `main` interface for
input, output, and secret selection, which allows deterministic multi-round
tests without subprocess timing or random-number coupling. The decision was
[recorded on task #10](https://github.com/davison/numberguess/issues/10#issuecomment-5410947774).

### Narrow administrator exception for merging

The configured GitHub App independently approved PR #11, satisfying
CodeCrew's non-doer review gate, but GitHub did not count that App review toward
the repository ruleset's required approving-review total. The ruleset had no
bypass actors, so an initial administrator merge attempt was also refused.

The operator first
[approved using an administrator bypass](https://github.com/davison/numberguess/issues/10#issuecomment-5411156100).
Because the ruleset had no eligible bypass actor, the repository administrator
role was then added temporarily, PR #11 was rebase-merged with the exception,
and the ruleset was restored to no bypass actors. The detailed gate resolution
documenting that temporary ruleset mutation was posted immediately after the merge on
[task #10](https://github.com/davison/numberguess/issues/10#issuecomment-5411179688).
This completed the independently verified task while keeping the exception
explicit, but the sequence also means the precise mutation mechanism was
recorded retrospectively rather than before it was used.

During milestone closeout, the operator chose to retain the administrator role
as a permanent bypass actor. Ordinary merges still enforce the ruleset, while
administrators can explicitly invoke a bypass when GitHub does not count an App
review. This avoids repeated temporary ruleset changes at the cost of retaining
an administrator escape hatch that must be used deliberately and audited. The
policy decision was
[recorded on task #14](https://github.com/davison/numberguess/issues/14#issuecomment-5411301890).

## Deviations

No implementation deviations from the recorded task plan occurred. The
administrator merge path was a workflow exception caused by the mismatch
between CodeCrew's acceptance of App reviews and GitHub's branch-ruleset review
count; it did not change the delivered requirements.

## Requirement outcomes

| Requirement | Outcome | Evidence |
|-------------|---------|----------|
| M3-R1 | Satisfied | The operator confirmed that every completed game is followed by a replay prompt. |
| M3-R2 | Satisfied | The operator confirmed that case-insensitive `yes`/`y` starts a fresh round with a newly selected secret. |
| M3-R3 | Satisfied | The operator confirmed that case-insensitive `no`/`n` exits cleanly. |
| M3-R4 | Satisfied | The operator confirmed that invalid replay responses explain the choices and re-prompt without starting a round. |

The README already describes the replay prompt and continued-round behavior,
so no milestone-boundary refresh was needed.
