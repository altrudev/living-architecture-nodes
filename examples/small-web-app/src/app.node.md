# app.node.md

## Node identity

- Node name: app
- Source file/folder: src/app.js
- Node owner: project maintainer
- Created: 2026-06-02
- Last updated: 2026-06-02
- Current health score: 90
- Current dirty flag: clean

---

# Static layer

## Purpose

Provides the public note actions used by the app.

## Responsibility boundary

Responsible for validating user note text and calling storage.

Not responsible for persistence implementation or UI rendering.

## Dependencies

| Dependency | Type | Reason | Risk |
|---|---|---|---|
| storage.js | local module | persist and load notes | storage changes can break note actions |

## Dependents

| Dependent | Relationship | Risk if this changes |
|---|---|---|
| UI layer | calls addNote and listNotes | UI may fail if contract changes |

## Contracts

### Inputs

- `addNote(text: string)`
- `listNotes()`

### Outputs

- saved note object
- array of note objects

### Side effects

- writes through storage module

### Error behavior

- throws when note text is empty

---

# Dynamic layer

## Stability state

Stable

## Recent mutations

| Date | Change | Reason | Affected dependents |
|---|---|---|---|
| 2026-06-02 | Initial node | Example protocol setup | UI layer |

## Known fragile points

- Input validation must stay aligned with UI error messaging.

## Interaction warnings

- Storage contract changes affect this module.

## Performance observations

- No known issues.

## Security notes

- Receives user text; storage layer should avoid unsafe rendering assumptions.

---

# Diagnostic layer

## Past bug patterns

| Date | Bug pattern | Root cause | Resolution | Regression test/check |
|---|---|---|---|---|
|  |  |  |  |  |

## Near misses

| Date | Near miss | Why it almost broke | Preventive action |
|---|---|---|---|
|  |  |  |  |

## Regression triggers

- Changing storage return shape.

## Suspected hidden coupling

| Date | Coupled module/behavior | Evidence | Confidence |
|---|---|---|---|
|  |  |  | observed / likely / inferred |
