#!/usr/bin/env python3
"""
Living Architecture Nodes starter CLI.

Commands:
  python tools/lan.py init
  python tools/lan.py check
  python tools/lan.py export

This starter tool is intentionally local-first and does not transmit data.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
from pathlib import Path
from typing import Dict, List


ROOT = Path.cwd()


NODE_TEMPLATE = """# {name}.node.md

## Node identity

- Node name: {name}
- Source file/folder: {source}
- Node owner:
- Created: {date}
- Last updated: {date}
- Current health score: 80
- Current dirty flag: clean

---

# Static layer

## Purpose

TODO

## Responsibility boundary

Responsible for:

- TODO

Not responsible for:

- TODO

## Dependencies

| Dependency | Type | Reason | Risk |
|---|---|---|---|
|  |  |  |  |

## Dependents

| Dependent | Relationship | Risk if this changes |
|---|---|---|
|  |  |  |

## Contracts

### Inputs

- TODO

### Outputs

- TODO

### Side effects

- TODO

### Error behavior

- TODO

---

# Dynamic layer

## Stability state

Under active change

## Recent mutations

| Date | Change | Reason | Affected dependents |
|---|---|---|---|
| {date} | Initial node created | LAN init | unknown |

## Known fragile points

- TODO

## Interaction warnings

- TODO

## Performance observations

- TODO

## Security notes

- TODO

---

# Diagnostic layer

Append-only. Do not overwrite past entries.

## Past bug patterns

| Date | Bug pattern | Root cause | Resolution | Regression test/check |
|---|---|---|---|---|
|  |  |  |  |  |

## Near misses

| Date | Near miss | Why it almost broke | Preventive action |
|---|---|---|---|
|  |  |  |  |

## Regression triggers

- TODO

## Suspected hidden coupling

| Date | Coupled module/behavior | Evidence | Confidence |
|---|---|---|---|
|  |  |  | observed / likely / inferred |
"""


def now_date() -> str:
    return _dt.datetime.now().date().isoformat()


def source_files() -> List[Path]:
    ignored_dirs = {".git", "node_modules", "dist", "build", ".venv", "__pycache__"}
    allowed = {".js", ".ts", ".jsx", ".tsx", ".py", ".html", ".css", ".json"}
    found = []
    for path in ROOT.rglob("*"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        if path.is_file() and path.suffix in allowed and not path.name.endswith(".node.md"):
            found.append(path)
    return found


def node_path_for(source: Path) -> Path:
    return source.with_name(f"{source.stem}.node.md")


def init_project() -> None:
    for name in ["ARCH.md", "NERVE.md", "CHANGELOG.node.md"]:
        target = ROOT / name
        if not target.exists():
            target.write_text(f"# {name}\n\nInitialized by Living Architecture Nodes.\n", encoding="utf-8")
            print(f"created {target}")

    for source in source_files():
        node = node_path_for(source)
        if not node.exists():
            rel_source = source.relative_to(ROOT).as_posix()
            content = NODE_TEMPLATE.format(
                name=source.stem,
                source=rel_source,
                date=now_date(),
            )
            node.write_text(content, encoding="utf-8")
            print(f"created {node}")


def check_project() -> int:
    problems = []
    required = ["ARCH.md", "NERVE.md", "CHANGELOG.node.md"]
    for name in required:
        if not (ROOT / name).exists():
            problems.append(f"missing required file: {name}")

    for source in source_files():
        node = node_path_for(source)
        if not node.exists():
            problems.append(f"missing node file for {source.relative_to(ROOT)}")
            continue
        text = node.read_text(encoding="utf-8", errors="replace")
        for heading in ["# Static layer", "# Dynamic layer", "# Diagnostic layer"]:
            if heading not in text:
                problems.append(f"{node.relative_to(ROOT)} missing heading: {heading}")

    if problems:
        print("Living Architecture Nodes check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Living Architecture Nodes check passed.")
    return 0


def export_project() -> None:
    export = {
        "protocol": "Living Architecture Nodes",
        "version": "0.1.0",
        "exported_at": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "project": {
            "name": ROOT.name,
        },
        "nodes": [],
        "nerve": {
            "dirty_nodes": [],
            "at_risk_nodes": [],
            "cascade_map": [],
            "cross_node_patterns": [],
            "temporal_patterns": [],
            "likely_culprit_nodes": [],
        },
        "suggested_investigation_order": ["ARCH.md", "relevant .node.md files", "NERVE.md", "CHANGELOG.node.md"],
    }

    for node_file in ROOT.rglob("*.node.md"):
        if ".git" in node_file.parts:
            continue
        export["nodes"].append({
            "name": node_file.stem.replace(".node", ""),
            "source": "",
            "node_file": node_file.relative_to(ROOT).as_posix(),
            "health_score": 0,
            "dirty_status": "unknown",
            "stability": "unknown",
            "dependencies": [],
            "dependents": [],
            "fragile_points": [],
            "security_notes": [],
            "diagnostic_summary": "See node file."
        })

    out_dir = ROOT / "diagnostic-export"
    out_dir.mkdir(exist_ok=True)
    json_path = out_dir / "living-architecture-nodes-export.json"
    md_path = out_dir / "living-architecture-nodes-summary.md"

    json_path.write_text(json.dumps(export, indent=2), encoding="utf-8")
    md_path.write_text(
        "# Living Architecture Nodes Diagnostic Summary\n\n"
        f"- Exported at: {export['exported_at']}\n"
        f"- Node count: {len(export['nodes'])}\n\n"
        "## Suggested investigation order\n\n"
        "1. Read `ARCH.md`.\n"
        "2. Read relevant `.node.md` files.\n"
        "3. Consult `NERVE.md`.\n"
        "4. Review `CHANGELOG.node.md`.\n",
        encoding="utf-8",
    )

    print(f"wrote {json_path}")
    print(f"wrote {md_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Living Architecture Nodes starter CLI")
    parser.add_argument("command", choices=["init", "check", "export"])
    args = parser.parse_args()

    if args.command == "init":
        init_project()
        return 0
    if args.command == "check":
        return check_project()
    if args.command == "export":
        export_project()
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
