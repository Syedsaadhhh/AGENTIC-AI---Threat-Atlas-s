# Contributing

Contributions are welcome when they improve the evidence, method, controls, or reproducibility of the atlas.

## Good contributions

- a primary source that changes or strengthens an entry
- a controlled reproduction with complete environment notes
- a concrete limitation or counterexample
- a clearer trust-boundary description
- a control that can be implemented and tested
- a validator improvement with a focused test case

## Before opening a pull request

1. Read `methodology/evidence-standard.md`.
2. Keep claims within the evidence level actually supported.
3. Use synthetic data and authorized environments.
4. Do not include live targets, secrets, personal data, or harmful operational payloads.
5. Run `python scripts/validate_entries.py`.
6. Explain what changed, why it changed, and what remains uncertain.

## Writing standard

Use direct language. State the mechanism before the conclusion. Prefer exact conditions over broad warnings. Separate observation, interpretation, and recommendation.

Avoid promotional claims, invented metrics, and severity labels without deployment assumptions. A negative result is useful and should be retained.

## New threat records

A new entry should identify a distinct boundary failure. Do not create a new identifier for a minor variation that fits an existing mechanism.

The pull request should include:

- proposed identifier and title
- evidence level with justification
- affected trust boundaries
- primary references
- mapped controls
- limitations and counterevidence
- reproduction package when claiming E2 or higher

## Source corrections

Where possible, cite the original paper, specification, vendor documentation, or disclosure. Secondary reporting may be included as context, but it should not carry the main claim.

## Review

Review may challenge the evidence level, scope, terminology, control mapping, or reproducibility. That is expected. The goal is a record that remains useful when read by someone who disagrees with it.