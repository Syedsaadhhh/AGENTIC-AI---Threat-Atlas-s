# Research position

## Working thesis

Security in agentic systems is largely an authority-routing problem.

A user gives a system a goal. The system then turns that goal into intermediate instructions, retrieves outside material, selects tools, uses credentials, writes state, and may hand work to another component. Every transition carries some amount of authority.

Failures appear when the system loses track of where that authority came from, what it was meant to permit, or when it should end.

## Why prompt-only analysis is incomplete

Prompt injection is important, but the prompt is only one part of the execution chain. The same injected text can be harmless in a read-only summarizer and serious in a system that can send mail, modify code, query private records, or run commands.

The security outcome depends on at least five surrounding facts:

1. Which source supplied the instruction-like content.
2. Which identity and credentials the system is using.
3. Which tools are reachable at that moment.
4. Which checks occur before an external effect.
5. Which state is retained after the task ends.

This is why the atlas records both the manipulation mechanism and the authority available after manipulation.

## Five propositions

### 1. Data must not gain authority by resemblance

External content can contain text that looks like an instruction. A secure design should not promote that text into control flow merely because a model finds it persuasive or relevant.

### 2. Delegation must reduce or preserve scope, never silently expand it

A subtask should inherit no more authority than the original task requires. Broad credentials attached to a narrow subtask create authority drift.

### 3. Tool risk is defined by effect, not interface

A friendly tool name does not describe its real power. Security review should examine the downstream operation, identity, data reach, reversibility, and audit trail.

### 4. Memory is a long-lived input channel

Stored summaries, preferences, plans, and retrieved facts can influence future actions. Memory therefore needs provenance, expiration, ownership, and deletion rules.

### 5. Observability without recovery is incomplete

Logs can explain a failure after it happens. They do not stop the failure. High-impact systems also need revocation, cancellation, rollback, and containment paths.

## Testable hypotheses

The atlas will treat these as research questions rather than settled facts:

- Per-action authorization should reduce the impact of indirect instruction injection more reliably than text filtering alone.
- Provenance-aware memory should reduce cross-session contamination without requiring the complete removal of long-term memory.
- Narrow tool scopes should lower both attack impact and incident investigation time.
- A deterministic policy layer outside the model should be harder to manipulate than a policy expressed only in natural-language instructions.
- Recovery controls should be evaluated as part of security, not as a separate operational concern.

## What would change this position

The thesis should be revised if repeated experiments show that authority tracking does not predict practical impact, if model-level defenses reliably separate instructions from data across realistic environments, or if the proposed controls create unacceptable task failure without a measurable security benefit.

The repository keeps limitations and counterevidence beside supporting evidence for that reason.