#!/usr/bin/env python3
"""List open (- [ ]) tasks from TASKS.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "TASKS.md"


def main() -> int:
    if not TASKS.is_file():
        print("TASKS.md not found", file=sys.stderr)
        return 1
    text = TASKS.read_text(encoding="utf-8")
    open_tasks = re.findall(r"^- \[ \] \*\*(T\d+)\*\* (.+)$", text, flags=re.M)
    done_tasks = re.findall(r"^- \[x\] \*\*(T\d+)\*\* (.+)$", text, flags=re.M | re.I)
    print(f"open: {len(open_tasks)}")
    print(f"done: {len(done_tasks)}")
    limit = 50
    if "--all" in sys.argv:
        limit = len(open_tasks)
    for tid, title in open_tasks[:limit]:
        print(f"{tid}\t{title}")
    if len(open_tasks) > limit:
        print(f"... and {len(open_tasks) - limit} more (use --all)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
