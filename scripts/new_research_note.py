#!/usr/bin/env python3
"""Scaffold a research note from a Phase 1 template."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"

DOMAIN_TEMPLATE = {
    "constitution": "constitutional_provision_note.md",
    "statutes": "statute_section_note.md",
    "judgments": "judgment_brief.md",
    "government": "government_policy_memo.md",
    "manufacturers": "oem_policy_capture.md",
    "cybersecurity": "cybersecurity_note.md",
    "environment": "environment_ewaste_note.md",
    "international": "comparative_jurisdiction_note.md",
    "economics": "economics_model_note.md",
    "technical": "technical_explainer.md",
    "consumer-law": "consumer_law_issue_note.md",
    "forum": "forum_analysis_memo.md",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a research note scaffold")
    parser.add_argument("--domain", required=True, choices=sorted(DOMAIN_TEMPLATE))
    parser.add_argument("--slug", required=True, help="filename slug, e.g. article-21")
    parser.add_argument("--title", default="", help="optional title substitution")
    args = parser.parse_args()

    tpl_name = DOMAIN_TEMPLATE[args.domain]
    tpl_path = TEMPLATES / tpl_name
    if not tpl_path.is_file():
        print(f"template missing: {tpl_path}", file=sys.stderr)
        return 1

    out_dir = ROOT / "research" / args.domain
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.slug}.md"
    if out_path.exists():
        print(f"refusing to overwrite: {out_path}", file=sys.stderr)
        return 1

    text = tpl_path.read_text(encoding="utf-8")
    today = dt.date.today().isoformat()
    text = text.replace("YYYY-MM-DD", today)
    text = text.replace('domain: ""', f'domain: "{args.domain}"')
    if args.title:
        text = text.replace('title: ""', f'title: "{args.title}"')

    out_path.write_text(text, encoding="utf-8")
    print(f"created: {out_path.relative_to(ROOT)}")
    print("Remember: no fabricated citations. Fill Sources before marking VERIFIED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
