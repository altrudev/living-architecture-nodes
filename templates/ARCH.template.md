# ARCH.md

System map and architectural truth ledger.

`ARCH.md` is itself a Living Architecture Node and must follow the static, dynamic, and diagnostic layers below.

---

# Intent layer

## Product/system intent

Describe what the system is designed to be.

## Architectural principles

- 

## Primary user/audience

- 

## Runtime environment

- 

## Data/security boundaries

- 

---

# Reality layer

## Current actual architecture

Describe what the system actually is right now.

## Known implementation compromises

- 

## Current architecture risks

- 

---

# Gap log

Timestamped divergences between intent and reality.

| Date | Intent | Reality | Risk | Planned resolution |
|---|---|---|---|---|
|  |  |  |  |  |

---

# Module index

| Node | Source | Health | Dirty flag | Notes |
|---|---|---:|---|---|
|  |  |  | clean / dirty / at-risk |  |

---

# Static layer for ARCH.md

## Purpose

`ARCH.md` defines the system-level architecture map, intent/reality distinction, gap log, and node index.

## Responsibility boundary

Responsible for:

- system-level architectural truth
- module index
- architecture drift tracking

Not responsible for:

- per-module implementation details
- complete bug history for individual modules

## Dependencies

- all `.node.md` files
- `NERVE.md`
- `CHANGELOG.node.md`

## Dependents

- maintainers
- AI agents
- diagnostic export tool
- onboarding docs

## Contracts

Inputs:

- node states
- changelog entries
- diagnostic findings

Outputs:

- system architecture map
- gap log
- module index

Side effects:

- directs debugging order
- defines current architecture truth

---

# Dynamic layer for ARCH.md

## Stability state

Stable / unstable / under active change

## Recent mutations

| Date | Change | Reason |
|---|---|---|
|  |  |  |

## Known fragile points

- 

## Interaction warnings

- 

## Performance observations

- 

## Security notes

- 

---

# Diagnostic layer for ARCH.md

Append-only.

## Past bug patterns

| Date | Architecture issue | Root cause | Resolution |
|---|---|---|---|
|  |  |  |  |

## Near misses

- 

## Regression triggers

- 

## Suspected hidden coupling

- 

