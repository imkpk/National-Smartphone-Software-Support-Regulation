# Changelog

All notable changes to this project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).  
Versioning aims to follow [Semantic Versioning](https://semver.org/) for releases after `0.1.0`.

---

## [Unreleased]

### Planned

- Phase 2 **statutes** inventory and consumer-law notes (outstanding)  
- Full Phase 2 close only after statutes DoD  
- Forum analysis memo (Art. 32 vs 226) — still open  
- Phase 3 judgments corpus — **not started** (do not auto-start)  

---

## [0.3.1] — 2026-07-30

### Changed

- `README.md` — badges, roadmap summary, and **Current progress** updated for Phase 2 constitution workstream (statutes still pending; Phase 3 not started)  
- `TASKS.md` — dashboard banner aligned with constitution-complete / statutes-outstanding status  

---

## [0.3.0] — 2026-07-30

### Added — Phase 2: Constitution Research (workstream)

Constitutional provision notes (neutral mapping; no litigation advice):

- Articles **14, 19(1)(a), 19(1)(g), 21, 21A, 38, 39, 48A, 51A(g), 32, 226** under `research/constitution/`
- `coverage-matrix.md`, `fr-dpsp-map.md`, open-questions catalogue, judgment-queue cross-links
- Source / citation / validation agent reports (`_source_quality_report.md`, `_citation_report.md`, `_validation_report.md`)
- PM execution plan; `PHASE_02_COMPLETION_REPORT.md` (constitution workstream; full Phase 2 not closed)

### Changed

- `research/constitution/README.md` — artefact index  
- `tasks/phase-02.md` — constitution tasks checked; statutes remain open  
- `TASKS.md` — Phase 2 status In progress  

### Explicitly not done

- No statutory research (CPA, IT Act, EPA, etc.)  
- No Phase 3 case-law digests  
- No litigation documents  
- No auto-start of Phase 3  

---

## [0.2.2] — 2026-07-30

### Added — Repository Quality Gates

- **`docs/DEFINITION_OF_DONE.md`** — repository-wide Definition of Done (authoritative phase-completion gate)  
- **Definition of Done** section on every `tasks/phase-00.md` … `phase-10.md`  
- **`QUALITY_GATES_REPORT.md`** — summary of this governance change  

### Changed

- `PROJECT_SPECIFICATION.md` — Quality Gates / phase completion policy (DoD)  
- `RESEARCH_GUIDELINES.md` — references DoD; no duplicated quality lists  
- `CONTRIBUTING.md` — PRs must satisfy applicable DoD before merge when phase-scoped  
- `MASTER_PROMPT.md` — mandatory end-of-run **DEFINITION OF DONE** section; stop; no auto-advance  
- `VALIDATION.md` — distinguishes document validation vs phase Definition of Done  

### Not changed

- No Phase 2 research  
- No PIL drafting  
- No repository structure redesign beyond governance docs  

---

## [0.2.1] — 2026-07-30

### Changed — Architecture cleanup (pre–Phase 2)

- Fixed `README.md` navigation and repository tree (removed duplicate `consumer-law/`; START_HERE first)  
- Added `docs/START_HERE.md` (5-minute onboarding)  
- Declared `VALIDATION.md` as **single source of truth** for validation  
- Declared `CITATION_POLICY.md` as **single source of truth** for citations  
- Thinned `RESEARCH_GUIDELINES.md` and `docs/how-to-cite.md` to pointers  
- Updated `docs/README.md` to current Phase 1 + cleanup state  
- Reduced active agent model to **seven core agents** in `AGENTS.md` (skill packs retained under `prompts/agents/`)  
- Replaced monolithic task list with `TASKS.md` dashboard + `tasks/phase-00.md` … `phase-10.md`  
- Minimal script consistency: `list_open_tasks.py` reads phase files; `check_structure.py` requires `tasks/` + START_HERE  
- Aligned `MASTER_PROMPT.md`, `CONTRIBUTING.md`, `REPOSITORY_STRUCTURE.md` with cleanup  
- Added `ARCHITECTURE_CLEANUP_REPORT.md`  

### Not changed

- No substantive legal research  
- Templates content not rewritten  
- `PROJECT_SPECIFICATION.md` philosophy unchanged  
- Phase 2 not started  

---

## [0.2.0] — 2026-07-30

### Added — Phase 1 Research Framework

- Research domain indexes (`research/README.md` + each domain `README.md`, including `research/forum/`)  
- Evidence and litigation folder READMEs (litigation hard-gated)  
- Templates under `templates/` (constitution, statute, judgment, OEM, cyber, environment, comparative, economics, technical, consumer-law, forum, RTI, validation, evidence schemas, synthetic style sample)  
- Validation assets: `citation-schema.json`, source tiers, research/litigation gate checklists, banned patterns  
- Scripts: `check_structure.py`, `list_open_tasks.py`, `new_research_note.py`, `scripts/README.md`  
- `requirements.txt`, `.env.example`  
- Docs: repository tour, how-to-cite, phase-gates, logging, glossary scaffold, examples  
- Agent prompt stubs under `prompts/agents/`  
- `automation/README.md`  
- CI workflow runs real structure check  
- Governance companions: `CITATION_POLICY.md`, `LEGAL_STRATEGY.md` (forum **OPEN**), `REPOSITORY_STRUCTURE.md`, `RESEARCH_GUIDELINES.md`  
- `MASTER_PROMPT.md` upgraded to supervised orchestration contract for Phase 2+  

### Changed

- `ROADMAP.md` — Phase 0 complete; Phase 1 exit criteria marked complete  
- `TASKS.md` — Phase 0 operator items + Phase 1 tasks T031–T085 checked  
- `README.md` — progress badges and Phase 1 status (no substantive research claimed)  
- `LEGAL_STRATEGY.md` — forum section neutralised (no HC/SC default)  

### Explicitly not added

- Substantive legal research memos  
- Judgment digests  
- PIL / affidavit drafts  

---

## [0.1.0] — 2026-07-30

### Added

- Repository foundation (Phase 0)  
- Root governance documents:
  - `README.md`
  - `LICENSE` (MIT + content notice)
  - `PROJECT_SPECIFICATION.md`
  - `ROADMAP.md` (Phases 0–10)
  - `TASKS.md` (300+ granular tasks)
  - `AGENTS.md` (multi-agent architecture)
  - `VALIDATION.md` (anti-hallucination constitution)
  - `MASTER_PROMPT.md` (placeholder only; inactive)
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `.gitignore`
- Directory tree for `docs/`, `research/*`, `evidence/*`, `litigation/*`, `templates/`, `prompts/`, `automation/`, `validation/`, `scripts/`, `output/`, `logs/`, `.github/`  
- `.gitkeep` placeholders for empty directories  
- `.github` issue/PR template stubs  

### Explicitly not added

- Legal research content  
- Judgment digests  
- PIL drafts  
- Executable Master Prompt  

---

## Version legend

| Version | Meaning |
|---------|---------|
| 0.x | Pre-research-release foundation and infrastructure |
| 1.0.0 | First public research corpus meeting validation gates |
| 1.x | Litigation drafts / automation enhancements |
