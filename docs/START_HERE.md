# Start here (≈ 5 minutes)

Welcome to **National-Smartphone-Software-Support-Regulation**.

This repository prepares rigorous, citable research on smartphone software support regulation in India. **Phase 3 is complete; Phase 4 is in progress** (see README / TASKS). **Filing forum is not pre-selected** (Article 32 vs Article 226 remain open).

---

## Read in this order

| # | File | Why |
|---|------|-----|
| 1 | [`../README.md`](../README.md) | Vision, problem, progress |
| 2 | [`../VALIDATION.md`](../VALIDATION.md) | **SoT** — validation / anti-hallucination |
| 3 | [`../CITATION_POLICY.md`](../CITATION_POLICY.md) | **SoT** — how to cite |
| 4 | [`../REPOSITORY_OS.md`](../REPOSITORY_OS.md) | **Permanent orchestrator OS** (resume, relevance, gate++) |
| 5 | Active phase spec e.g. [`../PHASE_04_SPECIFICATION.md`](../PHASE_04_SPECIFICATION.md) | Phase workstreams only |
| 6 | [`../TASKS.md`](../TASKS.md) | What to work on next |

Optional: [`../templates/README.md`](../templates/README.md), [`RESEARCH_GUIDELINES.md`](../RESEARCH_GUIDELINES.md), [`ROADMAP.md`](../ROADMAP.md), [`AGENTS.md`](../AGENTS.md).

---

## Your first concrete action

```bash
# From repository root
python scripts/check_structure.py
python scripts/list_open_tasks.py
python scripts/new_research_note.py --domain statutes --slug my-topic --title "My topic"
```

Then fill the note using FACT / LAW / ANALYSIS labels, add **Sources**, and run the research-gate checklist in [`../validation/research-gate-checklist.md`](../validation/research-gate-checklist.md).

---

## Where things live

| Need | Path |
|------|------|
| Research notes | `research/<domain>/` |
| Evidence tables / annexures | `evidence/` |
| Court drafts | `litigation/` (**Phase 9 hard gate — do not populate early**) |
| Phase checkboxes | `tasks/phase-XX.md` |
| Integrity rules | `VALIDATION.md` |
| Citation formats | `CITATION_POLICY.md` |

---

## Do not

- Invent cases, statutes, or statistics  
- Treat EU or other foreign law as binding in India  
- Open a PIL draft before Phase 9 approval  
- Assume the Supreme Court (or any High Court) is the correct forum without `research/forum/` analysis  

---

## More help

- Tour: [`repository-tour.md`](repository-tour.md)  
- Contribute: [`../CONTRIBUTING.md`](../CONTRIBUTING.md)  
- Conduct: [`../CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md)  

---

*If you only read one page after the README, make it VALIDATION.md.*
