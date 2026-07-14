# Evidence standard

The atlas separates an interesting mechanism from a demonstrated result. Every threat record carries an evidence level and enough context for another researcher to challenge it.

## Evidence levels

| Level | Meaning | Minimum requirement |
|---|---|---|
| E0 | Proposed | Clear mechanism and testable conditions, but no supporting source or reproduction yet |
| E1 | Source-supported | Supported by a primary paper, official specification, vendor documentation, or public incident record |
| E2 | Controlled reproduction | Reproduced in a documented local environment with retained inputs, outputs, versions, and checks |
| E3 | Independent reproduction | Reproduced by a separate researcher or implementation using the published method |
| E4 | Field-confirmed | Confirmed in an authorized production assessment, coordinated disclosure, or verified incident |

A higher level means stronger evidence for existence. It does not automatically mean higher severity.

## Required record fields

Every entry must state:

- the affected layers and trust boundaries
- the conditions required for the failure
- the sequence from input to effect
- the security properties at risk
- signals that a defender could observe
- controls placed at the relevant boundary
- known limitations and counterexamples
- open questions
- primary references

## Risk language

The atlas avoids unsupported numerical scoring. Impact depends heavily on permissions, connected systems, user role, and reversibility.

The `risk_band` field therefore accepts:

- `context-dependent`
- `low`
- `moderate`
- `high`
- `critical`

A record should remain `context-dependent` until the deployment assumptions are explicit.

## Reproduction package

An E2 claim should include the following under `experiments/`:

```text
experiment-id/
  README.md
  environment.json
  cases/
  results/
  checksums.txt
  limitations.md
```

The experiment note should identify:

1. System and model versions.
2. Tool definitions and permission scopes.
3. Initial state and test data.
4. Exact test sequence.
5. Expected safe behavior.
6. Observed behavior.
7. Independent verification checks.
8. Failed or ambiguous runs.

Secrets, live credentials, private user data, and harmful payloads must not be committed.

## Review rule

A threat entry is ready for `active` status when:

- its mechanism is understandable without private context
- its evidence level is justified
- its references are primary where possible
- its controls are specific enough to implement
- its limitations are not hidden
- the validator passes

## Correction policy

Corrections are part of the research record. A disputed entry should be marked `contested`, not silently rewritten. A retired entry remains in version history with the reason for retirement documented in the commit or pull request.