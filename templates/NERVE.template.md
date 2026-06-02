# NERVE.md

**Node Evidence & Regression Visibility Engine**

Central hub for dirty flags, cascade risk, pattern detection, temporal correlations, and troubleshooting playbooks.

---

# Current nerve summary

- Last updated:
- Overall system health:
- Highest-risk node:
- Current dirty nodes:
- Current at-risk cascade nodes:

---

# Dirty flag aggregation

| Node | Source changed? | Node updated? | Dirty status | Dependent count | Priority |
|---|---|---|---|---:|---|
|  | yes/no | yes/no | clean / dirty / at-risk |  | low / medium / high / critical |

---

# Cascade map

When a node is dirty or fragile, list all dependent nodes that may be affected.

| Flagged node | Direct dependents | Indirect dependents | Risk summary |
|---|---|---|---|
|  |  |  |  |

---

# Cross-node pattern detection

Same bug class appearing in multiple modules may indicate an architectural issue.

| Pattern | Nodes affected | Evidence | Architectural suspicion | Confidence |
|---|---|---|---|---|
|  |  |  |  | observed / likely / inferred |

---

# Temporal pattern log

Correlate changes with later failures in non-obvious dependents.

| Date range | Change event | Later failure | Suspected link | Confidence |
|---|---|---|---|---|
|  |  |  |  | observed / likely / inferred |

---

# Troubleshooting playbooks

## Playbook: regression after module change

1. Read `ARCH.md`.
2. Read changed module `.node.md`.
3. Read dependent nodes in cascade map.
4. Check diagnostic layer for matching regression triggers.
5. Review `CHANGELOG.node.md`.
6. Patch only after blast radius is understood.
7. Update node files and append diagnostic entry.

## Playbook: repeated bug class across modules

1. Identify all nodes with the same bug class.
2. Look for shared dependency, shared state, shared API, or shared assumption.
3. Add suspected architecture issue to `ARCH.md` gap log.
4. Add cross-node pattern entry here.
5. Create or update tests/checks for the shared failure mode.

---

# Health scores

| Node | Score | Band | Reason |
|---|---:|---|---|
|  |  | healthy / watch / fragile / critical |  |

---

# Likely culprit nodes

Used during active debugging.

| Incident | Likely culprit node | Reason | Confidence | Suggested investigation order |
|---|---|---|---|---|
|  |  |  | observed / likely / inferred |  |

