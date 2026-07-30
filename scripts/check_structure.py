#!/usr/bin/env python3
"""Phase 1 structure checker for National-Smartphone-Software-Support-Regulation."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "PROJECT_SPECIFICATION.md",
    "ROADMAP.md",
    "TASKS.md",
    "AGENTS.md",
    "VALIDATION.md",
    "MASTER_PROMPT.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".gitignore",
    "CITATION_POLICY.md",
    "LEGAL_STRATEGY.md",
    "REPOSITORY_STRUCTURE.md",
    "RESEARCH_GUIDELINES.md",
]

REQUIRED_DIRS = [
    "docs",
    "research",
    "research/constitution",
    "research/statutes",
    "research/judgments",
    "research/government",
    "research/manufacturers",
    "research/cybersecurity",
    "research/environment",
    "research/international",
    "research/economics",
    "research/technical",
    "research/consumer-law",
    "research/forum",
    "evidence",
    "evidence/charts",
    "evidence/tables",
    "evidence/timelines",
    "evidence/annexures",
    "litigation",
    "litigation/pil",
    "litigation/affidavit",
    "litigation/synopsis",
    "litigation/prayers",
    "litigation/drafts",
    "templates",
    "prompts",
    "prompts/agents",
    "automation",
    "validation",
    "scripts",
    "output",
    "logs",
    ".github",
]

REQUIRED_PHASE1_FILES = [
    "research/README.md",
    "evidence/README.md",
    "litigation/README.md",
    "templates/README.md",
    "validation/research-gate-checklist.md",
    "validation/litigation-gate-checklist.md",
    "validation/source-tier-definitions.md",
    "validation/banned-patterns.md",
    "validation/citation-schema.json",
    "scripts/check_structure.py",
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_ROOT_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing file: {rel}")
    for rel in REQUIRED_DIRS:
        if not (ROOT / rel).is_dir():
            errors.append(f"missing dir: {rel}")
    for rel in REQUIRED_PHASE1_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing Phase 1 file: {rel}")

    if errors:
        print("STRUCTURE CHECK: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("STRUCTURE CHECK: PASS")
    print(f"  root: {ROOT}")
    print(f"  checked_root_files: {len(REQUIRED_ROOT_FILES)}")
    print(f"  checked_dirs: {len(REQUIRED_DIRS)}")
    print(f"  checked_phase1_files: {len(REQUIRED_PHASE1_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
