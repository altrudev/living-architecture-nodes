# Living Architecture conformance

The public protocol owns semantic conformance cases. Individual implementations may remain independent, use different languages, expose different UI surfaces, and maintain implementation-specific features, but they must agree on the protocol-level cases defined here.

This is deliberately **not** a shared runtime library. Core, CLI, GitHub Action, VS Code and future adapters should not be coupled merely to avoid duplicated code. Instead, they consume or pin the same conformance evidence so semantic drift is detected before release.

## Scanner v0.1

`scanner/v0.1-cases.json` defines the minimum shared semantics for:

- required root artifacts;
- source-to-companion mapping;
- missing companions;
- orphan companions;
- exclusion of `.node.md` files from source classification;
- special treatment of `CHANGELOG.node.md` as a root protocol artifact, never an orphan companion.

Implementation-specific features such as dirty-node timestamps, health scoring, export formatting, redaction and UI presentation remain outside this fixture unless promoted into the public protocol.

A consumer that copies the fixture should record the exact upstream repository commit and path so the copy is auditable and can be refreshed deliberately rather than silently.
