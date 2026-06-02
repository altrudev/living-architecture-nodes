# storage.node.md

## Node identity

- Node name: storage
- Source file/folder: src/storage.js
- Node owner: project maintainer
- Created: 2026-06-02
- Last updated: 2026-06-02
- Current health score: 85
- Current dirty flag: clean

---

# Static layer

## Purpose

Provides local persistence for example notes.

## Responsibility boundary

Responsible for serializing and deserializing notes in localStorage.

Not responsible for validating note text or rendering note content.

## Dependencies

| Dependency | Type | Reason | Risk |
|---|---|---|---|
| localStorage | browser API | local persistence | unavailable in some non-browser runtimes |
| crypto.randomUUID | browser API | note IDs | unsupported in older browsers |

## Dependents

| Dependent | Relationship | Risk if this changes |
|---|---|---|
| app.js | calls saveNote and loadNotes | app contract breaks if return shape changes |

## Contracts

### Inputs

- `saveNote(note: object)`
- `loadNotes()`

### Outputs

- saved note object with `id`
- array of note objects

### Side effects

- reads/writes localStorage key `lan-example-notes`

### Error behavior

- corrupt JSON returns empty array

---

# Dynamic layer

## Stability state

Stable

## Recent mutations

| Date | Change | Reason | Affected dependents |
|---|---|---|---|
| 2026-06-02 | Initial node | Example protocol setup | app.js |

## Known fragile points

- Browser-only storage API.
- Corrupt storage silently resets to empty array.

## Interaction warnings

- Return shape must stay compatible with app.js.

## Performance observations

- Suitable only for small local datasets.

## Security notes

- Stores user-generated content locally.
- No network transmission.

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

- Changing localStorage key.
- Changing saved note shape.
- Replacing `crypto.randomUUID`.

## Suspected hidden coupling

| Date | Coupled module/behavior | Evidence | Confidence |
|---|---|---|---|
|  |  |  | observed / likely / inferred |
