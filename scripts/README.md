# Scripts

Phase 1 tooling for repository hygiene. No network scraping by default.

## Commands

```bash
# Structure check (exit 0 = pass)
python scripts/check_structure.py

# List open tasks from TASKS.md
python scripts/list_open_tasks.py
python scripts/list_open_tasks.py --all

# Scaffold a research note (does not write legal content)
python scripts/new_research_note.py --domain statutes --slug cpa-2019-overview --title "CPA 2019 overview"
```

On Windows with the Python launcher:

```powershell
py -3 scripts/check_structure.py
```

## Notes

- `new_research_note.py` only copies templates; authors must add verified sources.
- Do not commit secrets. See root `.gitignore`.

---
*Phase 1*
