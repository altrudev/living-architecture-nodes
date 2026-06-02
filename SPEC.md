# Living Architecture Nodes Protocol v0.1.0

## 1. Definition

**Living Architecture Nodes** is a repository-level maintenance protocol for multifile software projects. It requires every significant module, component, or architectural unit to have a companion `.node.md` file that records its architectural role, current operational state, and append-only diagnostic memory.

The protocol is designed for human developers, AI coding agents, maintainers, auditors, and reviewers who need to understand a codebase before changing it.

## 2. Purpose

The protocol exists to reduce architecture drift, repeated regressions, hidden coupling, undocumented side effects, and unsafe AI-assisted patches.

Its primary goal is to keep the following synchronized:

- source code
- intended architecture
- actual architecture
- module responsibility boundaries
- dependency relationships
- known fragile points
- bug history
- regression triggers
- AI/dev handoff context

## 3. Required repository artifacts

Every compliant multifile project MUST include:

### 3.1 `.node.md` companion files

Each meaningful source module/component MUST have a corresponding node file.

Examples:

```text
src/auth/session.ts
src/auth/session.node.md

src/components/CheckoutPanel.jsx
src/components/CheckoutPanel.node.md
```

A node file MAY represent a folder, service, route, subsystem, UI component, or module when one-to-one source mapping is impractical.

### 3.2 `ARCH.md`

`ARCH.md` is the system map. It MUST describe:

- the system intent
- current implementation reality
- timestamped gaps between intent and reality
- module index
- current health status per node

`ARCH.md` MUST itself be treated as a node and include static, dynamic, and diagnostic layers.

### 3.3 `CHANGELOG.node.md`

`CHANGELOG.node.md` is the cross-cutting iteration log. It records changes that affect more than one module, architectural decision, or diagnostic pattern.

### 3.4 `NERVE.md`

`NERVE.md` is the central nervous-system hub. It MUST aggregate:

- dirty flags
- stale nodes
- dependency cascade risks
- cross-node pattern detection
- temporal pattern log
- troubleshooting playbooks
- health score per node
- likely culprit nodes

### 3.5 Diagnostic export interface

Every project MUST include a mechanism such as a command, script, CI job, app button, or developer action that exports a single diagnostic artifact containing:

- all node current states
- dirty flag status
- NERVE hub patterns
- cascade maps
- recent changelog entries
- health scores
- flagged likely culprit nodes

The export MUST support two modes:

1. structured JSON/Markdown optimized for AI context-window ingestion
2. human-readable summary with suggested investigation order

## 4. Node file structure

Each `.node.md` file MUST include three layers.

### 4.1 Static layer

The static layer is set at creation and updated only on structural change.

Required fields:

- purpose
- responsibility boundary
- dependencies: what this module calls
- dependents: what calls this module
- contracts: expected inputs, outputs, and side effects

### 4.2 Dynamic layer

The dynamic layer is updated on every relevant trigger.

Required fields:

- current stability state: stable, unstable, under active change
- recent mutations: what changed and why
- known fragile points
- interaction warnings
- performance observations
- security notes

### 4.3 Diagnostic layer

The diagnostic layer is append-only and MUST NOT be rewritten to erase prior diagnostic history.

Required fields:

- past bug patterns
- near misses
- regression triggers
- suspected hidden coupling

## 5. Update triggers

Any of the following requires updating affected nodes:

- function signature change
- bug fix
- new dependency added
- dependency removed
- file touched in a session lasting more than 30 minutes
- new external API introduced
- new permission introduced
- security boundary changed
- persistence/storage behavior changed
- diagnostic export behavior changed

## 6. Dirty flag rule

A node is dirty/stale when its source file has been modified and the corresponding `.node.md` file has not been updated in the same session.

Dirty nodes MUST be surfaced in `NERVE.md`.

When dependency changes create risk beyond the directly changed module, dependent nodes SHOULD be marked at-risk.

## 7. Debug protocol

On any bug or regression, maintainers and AI agents MUST follow this sequence:

1. Read `ARCH.md`.
2. Identify suspected blast radius.
3. Read `.node.md` files for modules in the blast radius.
4. Consult `NERVE.md` for cascade, temporal, and pattern warnings.
5. Review recent entries in `CHANGELOG.node.md`.
6. Only then change source code.
7. After the fix, update affected nodes and append diagnostic notes.

## 8. Health scoring

Each node SHOULD have a health score derived from:

- bug frequency
- stale status
- fragile-point count
- dependency count
- dependent count
- unresolved warnings
- recent mutation density
- security sensitivity

Suggested score bands:

```text
90-100  healthy
70-89   watch
50-69   fragile
0-49    critical
```

## 9. AI handoff behavior

When used with AI coding agents, the project SHOULD require AI agents to read repository nerve artifacts before editing code.

Minimum AI handoff context:

- `ARCH.md`
- `NERVE.md`
- relevant `.node.md` files
- recent `CHANGELOG.node.md` entries
- current diagnostic export

## 10. Security and trust principles

Living Architecture Nodes tooling SHOULD be local-first.

Tools SHOULD NOT collect telemetry by default.

Diagnostic exports SHOULD redact secrets, tokens, private keys, credentials, personal data, and unrelated user content.

Exports SHOULD distinguish public project data from private implementation internals when used in products with public/private boundaries.

## 11. Canonical terminology

- **Living Architecture Node**: a module-level architectural memory file
- **Node file**: a `.node.md` companion file
- **NERVE**: Node Evidence & Regression Visibility Engine
- **Dirty flag**: stale state caused by source changes without node updates
- **Cascade map**: dependency-based at-risk map
- **Diagnostic layer**: append-only bug and regression memory
- **Reality layer**: current implementation truth, even when it contradicts intent

## 12. Non-goals

Living Architecture Nodes is not:

- generic project documentation
- a replacement for tests
- a replacement for version control
- a replacement for security review
- a proprietary lock-in format
- an excuse to generate excessive documentation

It is a protocol for keeping architecture memory synchronized with code and maintenance reality.

