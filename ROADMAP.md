# Research roadmap

The repository will grow through evidence, not by adding a large number of shallow entries.

## 0.1: Research baseline

Status: complete

- reference system and trust boundaries
- evidence levels and review rule
- initial control catalog
- machine-readable threat schema
- dependency-free validation
- three source-supported records
- first controlled experiment plan

## 0.2: Indirect instruction study

- build EXP-001 with synthetic mail, documents, and tool results
- compare ordinary execution, provenance labels, intent binding, and content isolation
- measure task completion and unauthorized action rates separately
- publish all failed, ambiguous, and safe runs
- move ATA-001 to E2 only if the committed package reproduces the result

## 0.3: Tool authority study

- define a small tool broker with narrow, broad, and step-specific scopes
- measure how task decomposition changes requested authority
- test explicit approval for target and scope expansion
- document revocation and cancellation behavior

## 0.4: Memory integrity study

- create isolated user and workspace fixtures
- test provenance, expiry, deletion, and semantic retrieval boundaries
- measure cross-session and cross-tenant contamination
- distinguish malicious influence from ordinary summarization error

## 0.5: Crosswalks

- map atlas records to OWASP agentic risks
- map relevant techniques to MITRE ATLAS
- map controls to NIST lifecycle functions
- document where the atlas adds detail and where it duplicates existing work

## Release rule

A release is ready when the validator passes, primary sources are current, limitations are visible, and no evidence level is stronger than the committed material supports.
