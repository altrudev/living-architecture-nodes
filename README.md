# Living Architecture Nodes

**A repository nervous-system protocol for AI-assisted software maintenance.**

Living Architecture Nodes gives every module in a multifile project its own architectural memory, tracks drift between intended and actual behavior, records diagnostic history where regressions happen, and exports context for humans or AI agents before source code is changed.

## Core idea

Modern codebases often fail because source files change faster than architectural memory. AI-assisted coding amplifies this problem: an agent can patch a file without knowing what that module is responsible for, what depends on it, what recently broke, or which hidden coupling has already been discovered.

Living Architecture Nodes addresses that by making architectural memory a required repository artifact.

Every multifile project contains:

- one `.node.md` companion file per module/component
- `ARCH.md` as the system map
- `CHANGELOG.node.md` as the cross-cutting iteration log
- `NERVE.md` as the central nervous-system hub
- a diagnostic export interface for AI/dev handoff

## Claim

Living Architecture Nodes is not general documentation. It is a maintenance protocol for synchronizing code, architecture, bug memory, dependency risk, and AI handoff context.

## Required files

```text
.node.md                       one companion file per module/component
ARCH.md                        system map; itself treated as a node
CHANGELOG.node.md              cross-cutting iteration log
NERVE.md                       central architecture nervous system
diagnostic export interface    command, script, or button that exports repository state
```

## Node layers

Each `.node.md` file contains three layers:

1. **Static layer** — purpose, responsibility boundary, dependencies, contracts
2. **Dynamic layer** — current stability, recent mutations, fragile points, warnings, performance and security notes
3. **Diagnostic layer** — append-only bug patterns, near misses, regression triggers, suspected hidden coupling

## Debug protocol

On any bug or regression:

1. Read `ARCH.md`.
2. Read the `.node.md` files for modules in the suspected blast radius.
3. Consult `NERVE.md` for cascade and pattern data.
4. Only then touch source code.

## Repository contents

```text
SPEC.md
templates/
  node.template.md
  ARCH.template.md
  NERVE.template.md
  CHANGELOG.node.template.md
schema/
  diagnostic-export.schema.json
examples/
  small-web-app/
tools/
  lan.py
NOTICE.md
TRADEMARK.md
LICENSE
```

## Status

This is the initial public specification package: **Living Architecture Nodes Protocol v0.1.0**.

## Author

Created by Valentyn Rukhaylo / Altru.dev.

Copyright 2026.

