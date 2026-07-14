# Atlas index

The atlas records security failures at the point where information, identity, permission, state, or execution crosses a trust boundary.

## Entry status

- `draft`: mechanism is still being written or reviewed
- `active`: meets the repository review rule
- `contested`: credible counterevidence or disagreement is unresolved
- `retired`: kept for history but no longer represents the current model

## Current records

| Record | Evidence | Focus |
|---|---:|---|
| [ATA-001](entries/ATA-001.json) | E1 | untrusted content influencing privileged action |
| [ATA-002](entries/ATA-002.json) | E1 | permission growth during task decomposition |
| [ATA-003](entries/ATA-003.json) | E1 | unverified state influencing later sessions |

## Reading a record

A threat record is not an exploit recipe. It is a structured argument:

```text
preconditions -> boundary failure -> external effect -> observable evidence -> control point
```

The record should make it possible to disagree with a claim precisely. A reviewer should be able to point to the precondition, evidence level, control mapping, or limitation that needs correction.

## Naming

`ATA` means Agentic Threat Atlas. Identifiers are stable. Titles and analysis may improve, but an identifier is not reused for a different mechanism.

## Adding an entry

1. Copy an existing JSON record.
2. Assign the next unused identifier.
3. Use the evidence rules in `methodology/evidence-standard.md`.
4. Reference controls already defined in `controls/control-catalog.md`.
5. Add primary sources to `references/sources.md` before citing them.
6. Run `python scripts/validate_entries.py`.
7. Submit the record with a clear review note and known limitations.
