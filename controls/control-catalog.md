# Control catalog

These controls are written for system architects and reviewers. They are intentionally placed outside model-only prompting because the highest-impact failures occur when a model decision reaches a privileged action.

## CTL-001: Preserve source and authority labels

**Purpose:** Prevent retrieved data from silently becoming control input.

Every context item should carry its source, owner, trust class, and whether it is allowed to influence planning or only provide facts. The label must survive summarization and handoff.

**Evidence to retain:** context manifest, source identifiers, trust labels, transformation history.

## CTL-002: Bind actions to explicit user intent

**Purpose:** Stop a proposed action that is unrelated to the user's request.

Before execution, compare the action, target, arguments, and expected effect with the original task. A retrieved document, tool result, or stored memory item cannot create new task authority by itself.

**Evidence to retain:** intent identifier, action rationale, policy decision, denied alternatives.

## CTL-003: Enforce least privilege at the tool broker

**Purpose:** Reduce the blast radius of a bad decision.

Expose only the tools and scopes needed for the current step. Prefer task-specific credentials, resource allowlists, read-only modes, and short-lived grants. Do not give a narrow subtask a broad inherited session.

**Evidence to retain:** tool manifest, granted scopes, credential audience, expiry, resource constraints.

## CTL-004: Require approval for authority expansion

**Purpose:** Prevent silent permission growth during planning.

Any step that adds a new target, identity, data class, tool, or irreversible effect should pause for a fresh policy decision. Human approval may be appropriate for high-impact actions, but the request must show the exact effect rather than a vague summary.

**Evidence to retain:** requested expansion, approver identity, decision time, approved parameters.

## CTL-005: Separate untrusted-content processing from privileged execution

**Purpose:** Limit the ability of hostile content to steer tools.

Use a quarantined path for parsing or summarizing untrusted material. A privileged planner should receive structured facts, provenance, and uncertainty, not raw instruction-like content where practical.

**Evidence to retain:** isolation boundary, transformation output, rejected fields, promotion decision.

## CTL-006: Make memory provenance-aware and time-bounded

**Purpose:** Reduce persistent contamination.

Every durable memory item should record who or what created it, the source material, the owning user or workspace, confidence, creation time, last use, and expiry. Sensitive or action-shaping memory should require stronger review than ordinary preferences.

**Evidence to retain:** memory record, source link, owner, expiry, updates, deletions.

## CTL-007: Record an execution-grade trace

**Purpose:** Distinguish model claims from system events.

Log the requested action, policy result, exact tool call, acting identity, runtime response, external confirmation, and retained state. Protect the trace from ordinary application writes.

**Evidence to retain:** ordered event log, timestamps, request identifiers, hashes, external receipts.

## CTL-008: Constrain network and file-system reach

**Purpose:** Contain unsafe execution and data exfiltration.

Use explicit egress rules, private-address blocking where appropriate, path allowlists, isolated workspaces, and deny-by-default access to secrets. Local tool servers should run with minimal host privileges.

**Evidence to retain:** sandbox policy, egress decisions, mounted paths, denied access events.

## CTL-009: Provide cancellation, revocation, and rollback

**Purpose:** Keep recovery possible after execution begins.

High-impact workflows should support stopping future steps, revoking temporary credentials, cancelling queued work, and reversing changes where the external service permits it.

**Evidence to retain:** recovery capability, invocation result, rollback receipt, unrecoverable effects.

## CTL-010: Test policy failure separately from model failure

**Purpose:** Identify which layer actually prevented or allowed the effect.

Experiments should record whether the model resisted, the policy gate denied, the tool broker rejected, the runtime contained, or the external service blocked an action. A safe outcome should not be credited to the wrong control.

**Evidence to retain:** decision at each layer, bypass attempts, false positives, task utility impact.

## Control selection rule

No single control is treated as sufficient. Entries should map controls to the boundary where they operate and explain the residual risk after deployment.