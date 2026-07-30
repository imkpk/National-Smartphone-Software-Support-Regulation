# Architecture Review

**Repository:** [National-Smartphone-Software-Support-Regulation](https://github.com/imkpk/National-Smartphone-Software-Support-Regulation)  
**Review type:** Engineering architecture audit (Staff / Principal / Docs / OSS maintainer lens)  
**Review date:** 2026-07-30  
**Reviewed state:** Phase 0 foundation + Phase 1 research framework on `main` (post-merge PR #1)  
**Scope:** Structure, documentation, templates, validation, agents, tasks, automation, navigation, scalability  
**Out of scope:** Legal research quality, substantive correctness of Indian law, PIL drafting  

**Method:** Full tree inventory (~129 files, ~89 Markdown), review of root governance docs, `templates/`, `validation/`, `scripts/`, `AGENTS.md`, `TASKS.md`, `README.md` tree, CI workflow, and empty-folder policy.

---

## Executive Summary

This repository is a **strong early-stage knowledge-system scaffold** for a high-integrity legal research project. Phase 0–1 correctly prioritised **documentation-first**, **phase gates**, **anti-hallucination rules**, and **domain separation** (`research/` vs `evidence/` vs `litigation/`). That is the right architectural bet for long-term credibility.

It is **not yet optimised for contributor scale**. The main risks are not empty folders (acceptable pre-content) but:

1. **Root documentation overload** and **duplicate policy surfaces** (citation / validation / guidelines / master prompt).  
2. **Agent sprawl** (18+ roles) that is conceptual, not operational.  
3. **Monolithic `TASKS.md`** that will not survive hundreds of contributors or 10k files.  
4. **Navigation debt**: no single “start here” path; outdated `docs/README.md`; a **broken tree snippet in `README.md`** (duplicate `consumer-law/`).  
5. **Automation theatre risk**: `automation/` is empty; validation is largely manual; structure check is good but thin.

**Verdict:** Approve for continued development **with a focused architecture hardening sprint** before Phase 2 content floods the tree. Do **not** expand agents or root docs further until consolidation lands.

**Overall score: 7.1 / 10** (see scorecard).

---

## Strengths

| Area | Observation |
|------|-------------|
| **Separation of concerns** | Clear split: `research/` (knowledge), `evidence/` (artefacts), `litigation/` (gated court work), `validation/` (quality), `scripts/` (tooling). |
| **Phase discipline** | Roadmap 0–10, hard gate on litigation, forum left open — correct product sequencing. |
| **Integrity culture** | `VALIDATION.md` + claim labels (FACT/LAW/ANALYSIS/NORM/OPEN) + source tiers T0–T4 is production-grade for LLM-assisted legal work. |
| **Templates** | Domain templates with YAML front matter enable consistent future content; synthetic sample shows format without fake law. |
| **OSS hygiene** | LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG, issue/PR templates, CI structure check, `.gitignore` for secrets/output. |
| **Domain model** | Research domains map cleanly to problem space (constitution → statutes → judgments → policy → OEM → cyber/env/econ → international → forum). |
| **Operable stubs** | `check_structure.py`, `new_research_note.py`, `list_open_tasks.py` are small, readable, stdlib-first (KISS). |
| **Explicit non-goals** | Phase 1 changelog and litigation README reduce accidental scope creep. |

---

## Weaknesses

### 1. Repository structure

| Issue | Detail |
|-------|--------|
| **Root document pile-up** | ~12 top-level Markdown governance files. Contributors face decision paralysis: README vs SPEC vs ROADMAP vs RESEARCH_GUIDELINES vs CITATION_POLICY vs VALIDATION vs MASTER_PROMPT vs LEGAL_STRATEGY vs REPOSITORY_STRUCTURE. |
| **Duplicate structure sources of truth** | Tree described in `README.md`, `REPOSITORY_STRUCTURE.md`, `PROJECT_SPECIFICATION.md`, and `check_structure.py` lists — drift already visible. |
| **README tree bug** | Structure block lists `consumer-law/` twice and mangled nesting under `forum/` (maintenance defect). |
| **Empty leaf dirs** | `evidence/*`, `litigation/*`, `output/` only `.gitkeep` — fine for Phase 1; will look “dead” without READMEs already present at parent (parent READMEs help). |
| **Orphan one-shot script** | `scripts/_phase1_bootstrap.py` is a large generator (~670 lines) used once; confuses “runtime tooling” vs “historical bootstrap.” |
| **Missing OSS meta** | No `CODEOWNERS`, `SECURITY.md`, `SUPPORT.md`, or docs landing “Start here.” |
| **`logs/` policy tension** | `.gitignore` ignores `logs/**` but progress logs are committed — policy unclear for 500 contributors. |

### 2. Documentation

| Issue | Detail |
|-------|--------|
| **Duplication** | Citation rules appear in README, VALIDATION, CITATION_POLICY, RESEARCH_GUIDELINES, docs/how-to-cite. |
| **Stale docs** | `docs/README.md` still says “Phase 0 foundation only” and lists Phase 1 docs as “planned” though they exist. |
| **Inconsistent depth** | Root docs are long and formal; domain READMEs are thin clones of each other (good pattern, little differentiation). |
| **Terminology** | “Agent,” “phase,” “gate,” “status tag,” “source tier” are well introduced but not centralized in glossary (glossary is skeleton). |
| **No docs IA** | `docs/repository-tour.md` helps, but is not linked prominently as the 5-minute path from README top. |

### 3. Templates

| Issue | Detail |
|-------|--------|
| **Good baseline** | Front matter fields consistent; domain mapping in `new_research_note.py` aligns. |
| **Thin shared structure** | Many templates repeat the same section skeleton with small label changes — DRY opportunity via one base template + domain extras. |
| **Metadata gaps** | No required `sources: []` in front matter; schema allows it but templates don’t enforce. No `reviewers` / `depends_on` fields for scale. |
| **Status vocabulary dualism** | Front matter `status` and inline claim labels both use similar words (SECONDARY appears in both systems) — mild cognitive load. |
| **Litigation templates present early** | Assertion map template is fine as scaffolding; risk of premature use without stronger lint/CI block on `litigation/**` writes. |

### 4. Validation

| Issue | Detail |
|-------|--------|
| **Strong constitution** | Cardinal rules R1–R10 are clear and right for this domain. |
| **Enforceability gap** | Almost entirely human process; only structure CI exists. At 100 PRs/week, manual VALIDATION.md will not hold. |
| **Overlap** | VALIDATION.md vs CITATION_POLICY.md vs validation/* checklists partially restate each other. |
| **Missing practical rules** | No file-size limits, binary annexure policy, filename convention enforcement, max quote length, or “how to mark negative findings” in CI. |
| **Severity model** | Defined but not wired to labels/CODEOWNERS/required checks. |

### 5. Agents

| Issue | Detail |
|-------|--------|
| **Too many agents for current stage** | 18 specified + optional roles + forum prompt stub ≈ 19 prompts. Realistic runtime for a small team is 4–6 roles. |
| **Overlaps** | Statute ↔ Consumer-law; Cybersecurity ↔ Technical; Environment ↔ Economics (externalities); Citation Validation ↔ QA; Chief Architect ↔ Git Manager (structure); PM ↔ Research Director (prioritisation). |
| **Orchestration realism** | MASTER_PROMPT assumes multi-agent dispatch; no runner, no queue, no idempotent task state store. Risk of “paper architecture.” |
| **Forum agent** | Prompt stub exists; not first-class in AGENTS core list — inconsistent. |
| **Do not add more agents** | Confirmed: no new agents needed. Merge/collapse is the correct direction. |

### 6. Tasks

| Issue | Detail |
|-------|--------|
| **Volume without graph** | 300+ tasks in one Markdown file (~430 lines). No dependency edges (`blocked_by`, `unlocks`). |
| **Historical noise** | Phase 0 checked tasks remain forever as changelog-by-checkbox; hard to scan “what next.” |
| **Some future leakage** | Cross-cutting “weekly hygiene,” “webinar,” “celebrate” items dilute engineering backlog. |
| **OEM expansion** | Per-brand × multi-task explosion is correct for research but will dominate the file. |
| **Impossible / vague** | “Protect main branch” marked done without repo settings proof; operator tasks mixed with content tasks. |
| **No machine format** | Markdown checkboxes do not scale to 500 contributors (use issues/projects or YAML task packs per phase). |

### 7. Automation

| Issue | Detail |
|-------|--------|
| **Good** | Minimal CI structure check; stdlib scripts; issue templates. |
| **Thin** | No markdown lint, link check, front-matter validation against `citation-schema.json`, no path guards on `litigation/`. |
| **Empty `automation/`** | README only — either implement or demote until Phase 10. |
| **Bootstrap script risk** | Re-running `_phase1_bootstrap.py` could overwrite domain READMEs if reused carelessly (overwrite policy not documented). |

### 8. Navigation (5-minute test)

**Can a new contributor understand the repo in five minutes?** **Partially — borderline fail.**

| Minute | Likely experience |
|--------|-------------------|
| 0–1 | README vision is clear; badges help. |
| 1–3 | Confronted with many root docs; unsure which is binding. |
| 3–5 | May find CONTRIBUTING + VALIDATION, but tree bug and duplicate policies waste time. |
| 5+ | Still unclear “first concrete file to create for Phase 2.” |

Missing: **one** `docs/START_HERE.md` (or README section) with ordered reading list of **3–5 files max**, then “create note via script.”

---

## Risks

| ID | Risk | Impact | Likelihood | Notes |
|----|------|--------|------------|-------|
| R1 | Policy doc drift (README ≠ VALIDATION ≠ CITATION_POLICY) | High | High | Already starting |
| R2 | TASKS.md merge conflicts at scale | High | High | Single file bottleneck |
| R3 | Agent/prompt sprawl unused → false confidence | Medium | High | Paper architecture |
| R4 | Premature litigation folder population | Critical (project integrity) | Medium | Gate is social, not technical |
| R5 | Manual validation fails under PR load | Critical | Medium–High when content starts | |
| R6 | Empty automation/ confuses contributors | Low | Medium | |
| R7 | Bootstrap script accidental rerun | Medium | Low | |
| R8 | Root governance bloat deters OSS contributors | Medium | Medium | |
| R9 | 10k-file growth without naming/sharding conventions | High | Medium (if research succeeds) | |

---

## Recommendations

### P0 — Do soon (before heavy Phase 2 content)

1. **Fix `README.md` structure tree** (duplicate `consumer-law/`, nesting).  
2. **Add `docs/START_HERE.md`** with a 5-minute path: README → VALIDATION → RESEARCH_GUIDELINES → templates/README → first `new_research_note.py` command. Link it from README top.  
3. **Declare single sources of truth:**  
   - Integrity rules → `VALIDATION.md` only  
   - Citation field formats → `CITATION_POLICY.md` (or merge into VALIDATION §)  
   - Structure → `check_structure.py` + `REPOSITORY_STRUCTURE.md` (README embeds by link, not full tree copy)  
4. **Update stale `docs/README.md`** to Phase 1 complete.  
5. **Clarify `logs/` policy** (tracked phase notes vs gitignored run noise).  

### P1 — Architecture hardening (1–2 sprints)

6. **Collapse agent model for execution** (docs may keep expanded matrix as optional):  
   - **Core runtime roles (recommended 6):** Orchestrator/PM, Research (domain-parameterised), Citation Validation, Evidence, Drafting (Phase 9+), Git/Release.  
   - Keep domain specialisation as **skill packs / templates**, not separate permanent agents.  
7. **Split `TASKS.md`** into `tasks/phase-02.md` … or GitHub Issues + milestone labels; keep root TASKS as index only.  
8. **CI upgrades:** validate front matter JSON schema on `research/**/*.md`; fail PR if files added under `litigation/**` without `PHASE9_APPROVED` flag/label; markdown link check.  
9. **Retire or quarantine** `scripts/_phase1_bootstrap.py` → `scripts/archive/` with README “do not run.”  
10. **Add `CODEOWNERS`** for `validation/`, `litigation/`, `scripts/`.  

### P2 — Scale readiness

11. **Naming conventions doc:** `research/<domain>/<slug>.md`, evidence IDs, max path depth.  
12. **Shard large domains** early (`research/judgments/supreme-court/`, `high-courts/<state>/`) before file count explodes.  
13. **ADR folder** `docs/adr/` for structural decisions (task system, agent collapse, forum workflow).  
14. **Projects/board** for contributor work; stop using checkbox MD as sole tracker.  
15. **SECURITY.md** for reporting malicious PRs / secret leaks (even for docs-heavy repos).  

### Explicit non-recommendations

- **Do not add more agents.**  
- **Do not add more root policy Markdown** until consolidation.  
- **Do not build a complex orchestrator** until Phase 2–3 produce real content and validation pain is measured.  
- **Do not delete empty research/evidence dirs yet** — they encode the domain model; keep parent READMEs.

---

## Priority Matrix

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| **P0** | Fix README tree bug | XS | High (trust) |
| **P0** | START_HERE + reading order | S | High (DX) |
| **P0** | Single source of truth for validation/citation | M | High |
| **P0** | Refresh docs/README staleness | XS | Medium |
| **P1** | Collapse agents to core runtime set | M | High |
| **P1** | Split TASKS by phase / Issues | M | High |
| **P1** | CI: schema + litigation path guard | M | High |
| **P1** | Archive bootstrap script | XS | Medium |
| **P1** | CODEOWNERS | S | Medium |
| **P2** | ADR process | S | Medium |
| **P2** | Domain sharding conventions | S | High at scale |
| **P2** | SECURITY.md | XS | Medium |
| **P2** | Implement or empty-state `automation/` | S | Low–Medium |

---

## Technical Debt

| Debt | Type | Paydown |
|------|------|---------|
| Multi-doc policy duplication | Docs | Merge/thin satellite docs |
| Monolithic TASKS.md | Process | Phase files or Issues |
| Agent catalog vs reality | Architecture | Collapse runtime roles |
| Manual-only validation | Quality | Schema CI + PR templates enforced |
| README structure drift | Docs | Generate tree or link-only |
| `_phase1_bootstrap.py` in active scripts | Tooling | Archive |
| Empty automation/ | Structure | Defer or implement minimal Makefile |
| Status tag dual systems | Taxonomy | One glossary section |
| logs/ gitignore vs tracked logs | Policy | Document exception list |
| No CODEOWNERS | OSS | Add |

---

## Files to Improve

| File | Why |
|------|-----|
| `README.md` | Broken structure tree; too much duplicated policy; needs START_HERE link |
| `docs/README.md` | Stale Phase 0 language |
| `TASKS.md` | Scale bottleneck; needs index + split |
| `AGENTS.md` | Too many first-class agents; mark expanded list as optional matrix |
| `MASTER_PROMPT.md` | Align with reduced runtime agent set |
| `VALIDATION.md` / `CITATION_POLICY.md` | Cross-link as SoT; remove duplicated prose |
| `RESEARCH_GUIDELINES.md` | Keep short; point to VALIDATION |
| `REPOSITORY_STRUCTURE.md` | Either generate from script or become the only full tree |
| `scripts/check_structure.py` | Extend for naming rules / litigation guard later |
| `automation/README.md` | Set expectations: “empty until Phase 10” |
| Domain `research/*/README.md` | Add “first tasks” pointers from TASKS when Phase 2 starts |
| `.gitignore` | Document intentional tracked files under `logs/` |

---

## Files to Merge

| Merge candidate | Into | Rationale |
|-----------------|------|-----------|
| `CITATION_POLICY.md` | `VALIDATION.md` (section) **or** keep thin and delete overlap from README | One integrity handbook |
| `RESEARCH_GUIDELINES.md` | Short pointer file → VALIDATION + templates | Avoid third copy of rules |
| `REPOSITORY_STRUCTURE.md` | README appendix **or** generate from `check_structure.py` | One structure SoT |
| `docs/how-to-cite.md` | CITATION_POLICY / VALIDATION | Already a thin mirror |
| Optional agent roles § | Fold into “domain skill packs” appendix | Reduce agent count |
| Supreme Court + High Court agents (runtime) | Single **Case Law** agent with court parameter | Overlap |
| Cybersecurity + Technical (runtime) | Single **Technical Risk** agent with mode flag | Overlap |
| Chief Architect + Git Manager (small teams) | **Platform** maintainer role | Overlap at low headcount |

---

## Files to Remove (or quarantine)

| Path | Action | Why |
|------|--------|-----|
| `scripts/_phase1_bootstrap.py` | Move to `scripts/archive/` or delete after export | One-shot generator; hazard if re-run |
| Redundant `.gitkeep` where README exists | Optional cleanup | Domain dirs with README don’t need `.gitkeep` |
| Duplicate root policy paragraphs | Edit, not delete files wholesale | Prefer merge over delete of governance |

**Do not remove:** empty `evidence/*` or `litigation/*` placeholders yet; they encode product architecture.

---

## Files to Split

| Path | Split into | Why |
|------|------------|-----|
| `TASKS.md` | `tasks/README.md` + `tasks/phase-0.md` … `phase-10.md` or GitHub milestones | Merge conflict & readability |
| `AGENTS.md` | `AGENTS.md` (runtime core) + `docs/agents-full-matrix.md` (optional expanded) | Onboarding vs reference |
| Future `research/judgments/` | `supreme-court/`, `high-courts/<court>/` | Scale |
| Future OEM research | `research/manufacturers/<brand>/` | Scale |
| `CHANGELOG.md` (later) | Keep single until long; then yearly files | Standard |

---

## Future Improvements

1. **Generated docs:** structure tree and task counts generated in CI to prevent drift.  
2. **Pre-commit hooks:** markdownlint, secret scan, front-matter check.  
3. **PR size budgets** for research dumps.  
4. **Content packages:** versioned research releases (`research-v0.3`) separate from framework tags.  
5. **Contributor ladder:** triage → research note → citation validation → maintainers.  
6. **Metrics dashboard:** open tasks by phase, VERIFIED vs PROVISIONAL counts (scriptable).  
7. **Internationalisation** of plain-language docs later — keep English legal core stable.  
8. **Annexure binary store policy** (Git LFS vs release assets) before PDFs accumulate.

---

## Architecture Principles Assessment

| Principle | Assessment | Score |
|-----------|------------|-------|
| **Separation of Concerns** | Strong domain/evidence/litigation split | Good |
| **Single Responsibility** | Weakened by multi-purpose root docs and multi-hat agents | Mixed |
| **DRY** | Policy and templates repeat | Weak |
| **KISS** | Scripts are simple; agent/task systems are not | Mixed |
| **YAGNI** | 18 agents + empty automation is mild YAGNI violation | Weak–Mixed |
| **Documentation First** | Excellent for Phase 0–1 | Strong |
| **Open Source Best Practices** | Solid base; missing CODEOWNERS/SECURITY/start path | Good |

---

## Scalability (10k files / 500 contributors / 100 PRs)

| Concern | Works today? | At target scale? |
|---------|--------------|------------------|
| Domain folders | Yes | Yes, if sharded |
| Monolithic TASKS.md | Barely | **No** |
| Manual validation | Yes | **No** |
| 18 concurrent “agents” | N/A (paper) | **No** without real orchestration and owners |
| Root policy docs | Painful | **No** without START_HERE + SoT |
| Structure CI only | Yes | Insufficient |
| Evidence/litigation split | Yes | Yes |
| GitHub PR workflow | Yes | Needs CODEOWNERS + required checks |

**Conclusion:** Domain layout **can** scale; **process artefacts** (tasks, agents, manual validation, root docs) **will not** without the P0–P1 recommendations.

---

## Repository Score

| Category | Score (/10) | Rationale |
|----------|-------------|-----------|
| **Documentation** | **7.5** | Ambitious and mostly clear; duplication + staleness + root overload |
| **Architecture** | **7.5** | Excellent separation of research/evidence/litigation; agent/task layers overbuilt |
| **Maintainability** | **6.5** | Templates/scripts help; multi-SoT docs and TASKS monolith hurt |
| **Scalability** | **6.0** | Folder model OK; process model not ready for 500 contributors |
| **Developer Experience** | **6.5** | Scripts + CONTRIBUTING good; 5-minute path incomplete; README tree bug |
| **Automation** | **5.5** | Structure CI + 3 scripts solid; automation/ empty; no content validation CI |
| **Navigation** | **6.0** | Tour exists but not front-and-center; too many entry docs |
| **Validation** | **8.0** | Best-in-class rules for this domain; enforceability still mostly human |
| **Overall** | **7.1** | Weighted judgment: strong integrity foundation, needs consolidation before content scale |

---

## Scorecard Narrative

- **Highest:** Validation culture and phase-gated litigation posture.  
- **Lowest:** Automation depth and navigation simplicity.  
- **Strategic message:** This is a **documentation-first legal research platform** with better integrity rules than most OSS repos of its age. The next architecture win is **subtraction and enforcement**, not more frameworks.

---

## Review Closure

| Item | Status |
|------|--------|
| Legal research performed | **No** |
| PIL documents created | **No** |
| Repository rewritten | **No** |
| Only review artefact | **`ARCHITECTURE_REVIEW.md`** (this file) |

**Recommended next engineering action (not executed here):** P0 doc fixes (README tree, START_HERE, SoT), then Phase 2 content under the existing folder model.

---

*End of Architecture Review — 2026-07-30*
