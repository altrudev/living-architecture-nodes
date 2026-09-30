# Living Architecture Nodes Adapter Contract v1

The adapter contract defines how an official or compatible host surface translates host-specific evidence into Living Architecture Nodes without embedding host policy into LAN semantics.

## Architectural rule

An adapter SHOULD be thin.

It MAY:
- collect host-specific inputs;
- normalize paths and host events;
- provide dirty/change evidence;
- request a canonical LAN operation;
- translate canonical findings into host UI, annotations, exit codes, or summaries.

It MUST NOT:
- redefine canonical LAN findings;
- turn an unexecuted semantic check into PASS or FAIL;
- silently upload repository contents;
- silently invoke remote compute;
- treat a host health score as semantic architecture proof.

## Contract layers

1. Adapter request: host -> canonical LAN engine.
2. Adapter result: canonical LAN engine -> host.
3. Mutation receipt: canonical LAN mutation -> host.

The request is runtime-local. Fields such as workspace roots are authority inputs and MUST NOT be copied into client-visible diagnostics by default.

## Host evidence

Supported v1 dirty-evidence modes:

- `mtime` — local source/node modification-time comparison;
- `changed-paths` — host supplies changed repository-relative paths;
- `none` — dirty-state evidence is intentionally not evaluated.

A host MAY provide stronger evidence in a future contract version, but it must not reinterpret v1 fields.

Workspace filtering MAY be expressed as simple directory exclusions and/or host-compatible glob exclusions. Official adapters must preserve user-configured exclusions rather than silently narrowing them.

## Canonical findings

The v1 result reports:

- required artifacts and missing required artifacts;
- source-file and node-file counts;
- missing node companions;
- dirty node companions according to declared evidence mode;
- orphan node files;
- executed basic verification scope;
- semantic architecture status.

For the Free basic-local scope:

```text
semanticArchitecture.status = NOT_VERIFIED
semanticArchitecture.executed = false
```

A host must preserve that meaning.

## Host policy

Health scoring, CI failure thresholds, colors, badges, tree views, annotations, and notification style are host policy. They are deliberately outside the canonical finding semantics.

## Security boundary

Adapters SHOULD use repository-relative paths in results.

Adapters MUST NOT export:
- absolute workspace paths;
- source contents unless a separately authorized operation requires them;
- full environment variables;
- billing secrets;
- entitlement signing private keys;
- unrelated repository identity metadata.

Mutation-capable adapters MUST enforce a workspace authority boundary and SHOULD produce a postcondition receipt.

## Official host kinds

The initial registered host kinds are:

- `cli`
- `vscode`
- `github-action`

Future host kinds can include GitLab CI, JetBrains, browser, MCP, desktop, or other developer surfaces without changing canonical LAN semantics.

## Schemas

- `schema/adapter-request.schema.json`
- `schema/adapter-result.schema.json`
- `schema/adapter-receipt.schema.json`

These schemas are protocol contracts. Official Altru.dev product implementations may use proprietary internal engines behind them.

Copyright 2026 Valentyn Rukhaylo / Altru.dev.
