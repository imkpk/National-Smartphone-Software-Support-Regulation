#!/usr/bin/env python3
"""List open (- [ ]) tasks from tasks/phase-*.md (dashboard is TASKS.md)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"


def main() -> int:
    files = sorted(TASKS_DIR.glob("phase-*.md"))
    if not files:
        print("no tasks/phase-*.md files found", file=sys.stderr)
        return 1
    open_tasks: list[tuple[str, str, str]] = []
    done_count = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        for tid, title in re.findall(r"^- \[ \] \*\*(T\d+)\*\* (.+)$", text, flags=re.M):
            open_tasks.append((path.name, tid, title))
        done_count += len(re.findall(r"^- \[[xX]\] \*\*T\d+", text, flags=re.M))
    print(f"open: {len(open_tasks)}")
    print(f"done: {done_count}")
    limit = 50
    if "--all" in sys.argv:
        limit = len(open_tasks)
    for fname, tid, title in open_tasks[:limit]:
        print(f"{fname}\t{tid}\t{title}")
    if len(open_tasks) > limit:
        print(f"... and {len(open_tasks) - limit} more (use --all)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
