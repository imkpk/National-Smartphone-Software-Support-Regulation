# Changelog

All notable changes to this project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).  
Versioning aims to follow [Semantic Versioning](https://semver.org/) for releases after `0.1.0`.

---

## [Unreleased]

### Planned

- Phase 2 constitutional and statutory research memos (substantive)  
- Forum analysis memo population (still open; no pre-judgment)  

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
