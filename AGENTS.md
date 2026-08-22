# Agents

This repository is part of a CodeCrew project — coordination state lives in
GitHub issues and PRs, per the protocol at
https://github.com/radiusred/gh-codecrew (SPEC.md).

- `.codecrew.yml` names the hub; the hub's `roles/` holds the role
  contracts. Read the contract for the role you were dispatched as before
  doing anything else.
- `gh codecrew status` shows where the project is; `gh codecrew help`
  lists the workflow verbs. Blocked gates refuse with
  `refused[CODE]: detail` — act on the code, don't work around it.
- Plans before commits, decisions recorded when made, and the verifier is
  never the doer.
