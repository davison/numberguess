# M2: Polished colourful CLI

## Goal and outcome

M2 set out to make the number-guessing CLI visually engaging while preserving
accessibility and testability. The milestone delivered a dependency-free,
colourful interface with icons in
[PR #8](https://github.com/davison/numberguess/pull/8). Compatible interactive
terminals receive styled headings, prompts, hints, validation messages, and
success output. Redirected output and incompatible terminals retain plain text,
and players can opt out with `NO_COLOR`.

The human operator independently exercised the milestone and
[reported it satisfactory](https://github.com/davison/numberguess/issues/6#issuecomment-5411225928).

## Decisions

### Dependency-free, capability-gated presentation

The presentation layer uses ANSI escape sequences and Unicode icons without a
third-party package. Styling is enabled automatically only for the built-in
interactive input/output path when stdout is a compatible TTY. `NO_COLOR` and
`TERM=dumb` disable styling, while injected and redirected I/O remain plain by
default. Tests can explicitly enable styling for deterministic coverage.

This avoids a runtime dependency and keeps non-interactive output clean. The
trade-off is that icons and colours are treated as one presentation mode:
terminals that cannot support the complete mode receive plain output rather
than partial decoration. The decision and trade-off were
[recorded on task #7](https://github.com/davison/numberguess/issues/7#issuecomment-5402742678).

### Independent reviewer App identity

The configured reviewer is the GitHub App `davison-review-bot`, operating with
its own installation token rather than through GitHub's review-request field.
The operator supplied the App and installation identifiers needed to mint that
token, resolving the review-dispatch gates recorded on
[task #7](https://github.com/davison/numberguess/issues/7#issuecomment-5402870376).
The App then independently approved the final implementation on PR #8.

## Deviations

### Verify output encoding before enabling icons

The original compatibility plan considered TTY state and environment opt-outs
but did not explicitly test whether the output encoding could represent the
Unicode icon set. Independent review reproduced a `UnicodeEncodeError` with an
ASCII-configured pseudo-TTY. The implementation was extended to check encoding
capability before enabling styled mode, with a regression test for ASCII
output. This deviation and its rationale were
[recorded on PR #8](https://github.com/davison/numberguess/pull/8#issuecomment-5402848768).

## Requirement outcome

| Requirement | Outcome | Evidence |
|-------------|---------|----------|
| M2-R1 | Satisfied | The operator confirmed the colourful interactive presentation, icons and colours, plain-text fallbacks, and unchanged gameplay behavior. |

The M2 tracking issue retained its generated “add requirements” placeholder
instead of defining a substantive M2-R1 requirement. CodeCrew parsed the ID in
that placeholder as a requirement, and the QA verdict was consequently recorded
against the milestone goal and delivered task behavior. This specification gap
is preserved here rather than reconstructing a requirement after delivery.

The README already describes interactive decoration, redirected-output
fallback, and the `NO_COLOR` opt-out, so no milestone-boundary refresh was
needed.
