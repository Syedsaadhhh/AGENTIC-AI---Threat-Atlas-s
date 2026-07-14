# Agentic Threat Atlas

[![Atlas validation](https://github.com/Syedsaadhhh/AGENTIC-AI---Threat-Atlas-s/actions/workflows/validate.yml/badge.svg)](https://github.com/Syedsaadhhh/AGENTIC-AI---Threat-Atlas-s/actions/workflows/validate.yml)

A field guide to security failures in systems that can plan, call tools, retain state, and act on behalf of a user.

**Release:** 0.1.0 research baseline  
**Last reviewed:** 14 July 2026  
**Maintainer:** Syed Saad

## Why this exists

Most security discussions stop at the prompt. That is too narrow for a system that can read files, choose tools, use credentials, remember earlier work, and change something outside the chat window.

This atlas follows authority across the full execution path:

```text
user intent -> planner -> model decision -> tool call -> runtime -> external effect -> stored state
```

The central question is not only whether hostile content can influence a model. The harder question is what the surrounding system allows that influence to become.

## Current release

The first release establishes the research method, system model, control catalog, machine-readable schema, and three initial threat records:

| ID | Threat | Primary boundary |
|---|---|---|
| ATA-001 | Indirect instruction injection through trusted content | content to decision |
| ATA-002 | Tool authority drift after task decomposition | decision to tool |
| ATA-003 | Persistent memory contamination across user sessions | state to future decision |

Read the records in [`atlas/entries`](atlas/entries).

## Research position

The working thesis is simple:

> Security in agentic systems is largely an authority-routing problem.

Instructions, data, identity, permissions, memory, and execution are often carried through the same context. When those categories blur, a system can make a locally reasonable decision that produces an unauthorized global effect.

The longer argument is documented in [`docs/research-position.md`](docs/research-position.md).

## Method

Each threat record must include:

1. A defined trust boundary.
2. Preconditions that can be checked.
3. A plain-language attack path.
4. Observable evidence.
5. Controls mapped to the point where authority changes.
6. Limits, counterexamples, and unresolved questions.

Claims are labelled by evidence status. A plausible mechanism is not presented as a reproduced result. See [`methodology/evidence-standard.md`](methodology/evidence-standard.md).

## Repository map

```text
atlas/entries/              machine-readable threat records
controls/                   control definitions and mappings
docs/                       research notes and system model
experiments/                reproducible test plans and results
methodology/                evidence and review rules
references/                 primary sources and reading notes
schemas/                    threat record specification
scripts/                    local validation tools
```

## Validate the atlas

The validator uses only the Python standard library.

```bash
python scripts/validate_entries.py
```

A GitHub Actions workflow runs the same check on every push and pull request.

## Boundaries

This is an early research repository, not a security standard, product certification, or claim that every listed failure has been reproduced against every vendor. The atlas avoids operational exploit payloads and does not publish credentials, live targets, or instructions designed to cause harm.

## Responsible use

Use this material for defensive design, testing in systems you own or are authorized to assess, and responsible disclosure. Report repository security concerns through [`SECURITY.md`](SECURITY.md).

## Attribution

The taxonomy and analysis in this repository are original working research by Syed Saad. External frameworks and papers are credited in [`references/sources.md`](references/sources.md).