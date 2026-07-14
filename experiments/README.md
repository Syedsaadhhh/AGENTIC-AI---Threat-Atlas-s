# Experiments

This directory will contain controlled reproductions for atlas records.

The current release is evidence level E1. It establishes the system model and testable mechanisms before publishing experimental claims.

## First planned study

**Study ID:** EXP-001  
**Related record:** ATA-001  
**Question:** Does per-action intent binding reduce unauthorized tool proposals when a system reads instruction-like external content?

### Planned comparison

| Condition | Description |
|---|---|
| A | planner receives trusted instructions and raw external content with ordinary tool access |
| B | same planner and task, with source labels preserved |
| C | source labels plus a deterministic action-to-intent policy gate |
| D | quarantined content processing plus the same policy gate |

### Measurements

- legitimate task completion
- unauthorized action proposal rate
- unauthorized action execution rate
- approval prompts generated
- false denials
- trace completeness
- outcome after repeated and paraphrased cases

### Required safeguards

- local or isolated test environment
- synthetic accounts and data
- no live credentials
- no external recipients
- deny-by-default network policy
- retained versions, inputs, outputs, and checksums

No result will be reported until the environment and evaluation checks can be reproduced from the committed package.
