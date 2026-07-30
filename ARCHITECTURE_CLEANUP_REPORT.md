# Architecture Cleanup Report

**Repository:** National-Smartphone-Software-Support-Regulation  
**Date:** 2026-07-30  
**Basis:** Approved items from [`ARCHITECTURE_REVIEW.md`](ARCHITECTURE_REVIEW.md)  
**Result:** Cleanup complete. **Phase 2 not started.** No legal research or PIL content added.

---

## 1. Executive summary

Implemented the seven approved architecture cleanup items: README navigation/tree fix, `docs/START_HERE.md`, validation and citation single sources of truth, refreshed docs index, seven-core-agent model, and split task system (`TASKS.md` dashboard + `tasks/phase-00`…`10`).  

`CHANGELOG.md` records **[0.2.1]**. Structure check: **PASS**. Open tasks remain **303** (Phase 2+); done **85** (Phases 0–1).

---

## 2. Change-by-change summary

### 2.1 Fix README navigation and repository tree

| Action | Detail |
|--------|--------|
| **Fixed** | Duplicate `consumer-law/` and broken nesting under `forum/` removed |
| **Added** | Top “Start here” table with ordered links |
| **Simplified** | Citation/methodology sections now point to SoT docs instead of full rule copies |
| **Updated** | Structure summary; full tree deferred to `REPOSITORY_STRUCTURE.md` |
| **File** | `README.md` |

### 2.2 Add `docs/START_HERE.md`

| Action | Detail |
|--------|--------|
| **Created** | 5-minute path: five required reads + first tooling commands + do-not list |
| **Linked from** | `README.md`, `docs/README.md`, `CONTRIBUTING.md`, `MASTER_PROMPT.md` startup |
| **File** | `docs/START_HERE.md` |

### 2.3 `VALIDATION.md` as single source of truth (validation)

| Action | Detail |
|--------|--------|
| **Header** | Explicit SoT authority for gates, claim classes, tiers, status tags, anti-hallucination |
| **Cross-link** | Citation *formats* → `CITATION_POLICY.md` |
| **Checklists** | `validation/` remains operational implementation, must not contradict SoT |
| **Downstream** | README, RESEARCH_GUIDELINES, CONTRIBUTING point to VALIDATION for integrity |
| **File** | `VALIDATION.md` (banner + judgment field pointer) |

### 2.4 `CITATION_POLICY.md` as single source of truth (citations)

| Action | Detail |
|--------|--------|
| **Header** | Explicit SoT for bibliographic elements |
| **Deduped** | Claim-label definitions deferred to VALIDATION §3 (no second definition) |
| **Pointer** | `docs/how-to-cite.md` reduced to link-only |
| **File** | `CITATION_POLICY.md` |

### 2.5 Update `docs/README.md`

| Action | Detail |
|--------|--------|
| **Status** | Phase 1 complete; cleanup applied; research not started; forum open |
| **Index** | Lists START_HERE and current docs |
| **SoT table** | Root authorities clearly labelled |
| **File** | `docs/README.md` |

### 2.6 Reduce active agents to approximately seven

| Core runtime agent | Replaces / absorbs |
|--------------------|--------------------|
| 1. Project Manager | PM + light orchestration |
| 2. Research Agent (domain=) | Constitution, Statute, SC, HC, Government, OEM, Cyber, Env, Econ, Technical, Consumer-law, Forum as **skill packs** |
| 3. Citation Validation Agent | Unchanged role |
| 4. Evidence Agent | Unchanged role |
| 5. Drafting Agent | Unchanged; Phase 9+ only |
| 6. Quality Assurance Agent | Unchanged role |
| 7. Git / Release Agent | Git Manager + light platform/structure (ex–Chief Architect overlap) |

| Action | Detail |
|--------|--------|
| **Rewrote** | `AGENTS.md` around seven cores + extensibility via skill packs |
| **Preserved** | Existing `prompts/agents/*.md` files as skill packs (not deleted) |
| **Aligned** | `MASTER_PROMPT.md` dispatch examples to Research Agent + skill pack |
| **Did not** | Add new agents |

### 2.7 Replace monolithic `TASKS.md`

| Action | Detail |
|--------|--------|
| **Dashboard** | New `TASKS.md` with phase status table and counts |
| **Created** | `tasks/README.md` |
| **Created** | `tasks/phase-00.md` … `tasks/phase-10.md` (content migrated from former monolith) |
| **Counts** | 85 done / 303 open / 388 total (unchanged inventory) |
| **phase-10** | Includes former “Cross-Cutting” and “Meta” sections |
| **Scripts (minimal)** | `list_open_tasks.py` reads `tasks/phase-*.md`; `check_structure.py` requires `tasks/` + phase files + START_HERE |

---

## 3. Other consistency updates (supporting only)

| File | Change |
|------|--------|
| `RESEARCH_GUIDELINES.md` | Workflow-only; SoT table; no duplicated rules |
| `docs/how-to-cite.md` | Pointer only |
| `docs/repository-tour.md` | START_HERE + split tasks |
| `CONTRIBUTING.md` | START_HERE + SoT + tasks path |
| `REPOSITORY_STRUCTURE.md` | Reflects `tasks/`, SoT files, cleanup artefacts |
| `MASTER_PROMPT.md` | Seven agents; phase task paths |
| `CHANGELOG.md` | **[0.2.1]** entry |

---

## 4. Explicitly not done (per instructions)

- No legal research memos  
- No PIL / affidavit / synopsis drafting  
- No Phase 2 task execution  
- No rewrite of research templates bodies  
- No automation framework rewrite  
- `PROJECT_SPECIFICATION.md` left unchanged  
- Philosophy unchanged (integrity-first, forum open, phase gates)  

---

## 5. Verification

| Check | Result |
|-------|--------|
| `python scripts/check_structure.py` | **PASS** |
| `python scripts/list_open_tasks.py` | **open: 303, done: 85**; first open = Phase 2 T086 |
| Substantive `research/*` content | Still indexes/READMEs only |
| Forum pre-judgment | None |

---

## 6. Files touched (inventory)

### Created
- `docs/START_HERE.md`
- `tasks/README.md`
- `tasks/phase-00.md` … `tasks/phase-10.md` (11 files)
- `ARCHITECTURE_CLEANUP_REPORT.md` (this file)

### Substantively updated
- `README.md`
- `TASKS.md` (now dashboard)
- `AGENTS.md`
- `VALIDATION.md`
- `CITATION_POLICY.md`
- `RESEARCH_GUIDELINES.md`
- `docs/README.md`
- `docs/how-to-cite.md`
- `docs/repository-tour.md`
- `CONTRIBUTING.md`
- `REPOSITORY_STRUCTURE.md`
- `MASTER_PROMPT.md`
- `CHANGELOG.md`
- `scripts/list_open_tasks.py` (minimal, required)
- `scripts/check_structure.py` (minimal, required)

### Unchanged (examples)
- `PROJECT_SPECIFICATION.md`
- `templates/*` bodies
- `validation/*` checklist bodies (still valid implementations)
- `prompts/agents/*` skill pack files (retained)
- `ROADMAP.md` (phase definitions; status still accurate)
- `LICENSE`, `CODE_OF_CONDUCT.md`

---

## 7. Residual risks / follow-ups (not in this cleanup)

| Item | Note |
|------|------|
| Prompt stub names still use old agent titles | Intentional skill packs; optional later rename |
| Dashboard counts are static | Recompute when phases complete |
| `scripts/_phase1_bootstrap.py` still present | Review recommended archive later (not in approved list) |
| CODEOWNERS / SECURITY.md | Not in approved cleanup set |

---

## 8. Stop condition

Architecture cleanup **complete**.  

**Do not begin Phase 2** until explicitly authorised.

---

*End of Architecture Cleanup Report*
