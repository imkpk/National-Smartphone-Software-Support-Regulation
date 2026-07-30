# Project Specification

**Project name:** National-Smartphone-Software-Support-Regulation  
**Document type:** Foundational product & research specification  
**Phase:** 0 — Foundation  
**Version:** 0.1.0  
**Status:** Active  

---

## 1. Vision

Create the definitive open-source knowledge system on **smartphone software support regulation in India**, engineered to the documentation, validation, and operational standards of a Fortune 500 software organisation, and suitable as the factual and legal backbone for public-interest advocacy and litigation preparation.

## 2. Mission

1. Aggregate **verified** law, policy, and evidence.  
2. Separate **facts**, **legal propositions**, and **normative analysis**.  
3. Enable multi-agent and human collaboration under strict anti-hallucination rules.  
4. Deliver reproducible research artefacts and, only in later phases, court-oriented drafts.  
5. Remain transparent, citable, and forkable.

## 3. Goals

| Goal | Description | Success metric |
|------|-------------|----------------|
| G1 | Completeness of Indian legal map | Checklist coverage ≥ 95% of TASKS Phase 2–4 items |
| G2 | Citation integrity | 0 fabricated citations in `main` |
| G3 | Manufacturer evidence | All major OEMs documented with dated captures |
| G4 | Comparative law pack | EU + ≥ 8 jurisdictions tabulated |
| G5 | Litigation readiness | Validated PIL package passes VALIDATION.md gates |
| G6 | Automation | Structure + citation checks runnable via `scripts/` |
| G7 | Public usability | Clear README, docs, and contribution path |

## 4. Scope

**In scope**

- Indian constitutional provisions relevant to digital end-points, equality, privacy, environment, consumer welfare, and writ jurisdiction.  
- Central statutes, rules, notifications, and policies touching consumer protection, IT/cybersecurity, environment/e-waste, standards (BIS), metrology, electronics manufacturing, and Digital India.  
- Supreme Court and High Court jurisprudence on related doctrines (not a general case law dump).  
- Comparative international product longevity / software support / right-to-repair regimes.  
- OEM software support policies and technical lifecycle concepts.  
- Cybersecurity (patch lifecycle, CVE exposure pathways), e-waste, and economic externalities research.  
- Templates, validation schemas, automation, and eventual litigation drafts.  
- Evidence artefacts: tables, timelines, charts, annexure indexes.

**Geographic focus:** India (primary); international (comparative).  
**Device focus:** Smartphones (tablets secondary if material).  
**Software focus:** OS upgrades and security updates; related firmware where material.

## 5. Non-Scope

Explicitly **out of scope** (unless later approved by Project Manager change control):

- Providing personalised legal advice to individuals.  
- Hacking, exploit development, or offensive security tooling.  
- Reverse engineering proprietary OS binaries for distribution.  
- Defamation or unsubstantiated fraud allegations against named companies.  
- Drafting of private commercial contracts for OEMs.  
- Political campaigning materials unrelated to the research question.  
- **Phase 0:** any legal research, judgment digests, or PIL drafting (deferred by design).  
- Claiming judicial outcomes or “binding international law on India” without analysis of dualist incorporation.

## 6. Deliverables

| ID | Deliverable | Location | Phase |
|----|-------------|----------|-------|
| D0 | Repository foundation | Root docs + tree | 0 |
| D1 | Research templates & schemas | `templates/`, `validation/` | 1 |
| D2 | Constitutional & statutory memos | `research/` | 2 |
| D3 | Judgments corpus | `research/judgments/` | 3 |
| D4 | Government policy map | `research/government/` | 4 |
| D5 | OEM policy dossier | `research/manufacturers/` | 5 |
| D6 | Cyber / environment / economics packs | `research/*` | 6 |
| D7 | Comparative law dossier | `research/international/` | 7 |
| D8 | Evidence annexure factory | `evidence/` | 8 |
| D9 | Litigation package drafts | `litigation/` | 9 |
| D10 | Automation + public release hardening | `scripts/`, `.github/` | 10 |

## 7. Repository Standards

1. **English (Indian legal English)** for formal documents; plain English summaries allowed in `docs/`.  
2. **UTF-8** encoding; LF preferred in git attributes where possible.  
3. **Markdown** as default authoring format; exports to DOCX/PDF via scripts in later phases.  
4. **Semantic folder placement** — do not dump research at repo root.  
5. **`.gitkeep`** in empty directories until real content exists.  
6. **No secrets** in git (API keys, personal phone numbers of parties, sealed documents).  
7. **CHANGELOG.md** updated on every meaningful release.  
8. **Branching (recommended):** `main` (protected quality), `research/*`, `litigation/*`, `automation/*`.

## 8. Research Standards

1. Prefer **primary sources**.  
2. Record `source_url`, `accessed_on`, `document_id`, `jurisdiction`.  
3. Use status tags: `VERIFIED` | `SECONDARY` | `UNVERIFIED` | `DISPUTED` | `OUTDATED`.  
4. Never invent case names, citations, section numbers, or notification numbers.  
5. When sources conflict, document both and escalate to Citation Validation Agent.  
6. Separate sections: **Facts**, **Law**, **Analysis**, **Open Questions**, **Sources**.  
7. Pin-cites for judgments only after full-text verification (or mark provisional).

## 9. Coding Standards

1. Scripts: Python 3.11+ preferred; Node allowed for doc tooling.  
2. Type hints / clear CLI `--help` for user-facing scripts.  
3. No network calls that scrape behind logins without documented consent.  
4. Deterministic outputs where possible (fixed sort orders, pinned dates in fixtures).  
5. Tests for parsers and validators live under `scripts/tests/` (Phase 1+).  
6. Fail closed: validators exit non-zero on missing citations in gated paths.

## 10. Documentation Standards

1. Every top-level doc has title, purpose, version/status where relevant.  
2. Cross-link related docs; avoid orphan files.  
3. Keep README progress honest.  
4. User-facing docs in `docs/`; agent instructions in `AGENTS.md` and `prompts/`.  
5. Diagrams optional (Mermaid) for architecture in later phases.

## 11. Quality Standards

| Gate | Rule |
|------|------|
| Q1 | `VALIDATION.md` compliance for any file under `research/` or `litigation/` |
| Q2 | No `TODO cite` left in files marked `status: final` |
| Q3 | Peer or agent review before merge to `main` for legal claims |
| Q4 | Litigation drafts watermarked `DRAFT — NOT FOR FILING` until final checklist |
| Q5 | Automated structure check passes (Phase 1+) |
| Q6 | Phase completion only when [`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md) + phase-specific DoD are satisfied |

## 11A. Quality Gates (Definition of Done)

### Repository-wide Definition of Done

The authoritative phase-completion gate is:

**[`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md)**

It defines mandatory criteria for research completeness, validation, citations, documentation, navigation, task tracking, changelog, cross-references, placeholder removal, review, and completion approval.

**Distinction:**

| Instrument | Answers |
|------------|---------|
| [`VALIDATION.md`](VALIDATION.md) | Is this **document/claim** acceptable? |
| [`CITATION_POLICY.md`](CITATION_POLICY.md) | Is this **citation** well-formed? |
| [`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md) | Is this **phase** finished enough to advance? |

### Phase completion policy

1. Each `tasks/phase-XX.md` file includes a **Definition of Done** section that inherits the repository-wide DoD and adds phase-specific criteria.  
2. A phase is **not** complete merely because files or folders exist.  
3. **No phase may begin** until the previous phase satisfies its Definition of Done (repository-wide + phase-specific), except parallel streams expressly allowed in `ROADMAP.md` after Phase 1 is complete.  
4. Phase 9 additionally requires written Project Manager approval in `CHANGELOG.md` before drafting.  
5. Completing a phase must be recorded (CHANGELOG and/or `logs/`); the next phase must **not** start automatically.  
6. Pull requests that claim phase completion must demonstrate DoD compliance.

## 12. Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Hallucinated citations | Critical | Medium (LLM workflows) | VALIDATION.md; Citation Validation Agent; human spot-check |
| Outdated OEM policies | High | High | Dated captures; re-verification tasks |
| Scope creep into general cyber policy | Medium | Medium | Non-scope list; PM change control |
| Copyright issues with full judgment dumps | Medium | Medium | Cite + link; fair dealing extracts only |
| Litigation drafts treated as advice | High | Medium | Disclaimer; draft banners |
| Empty research dirs forever | Medium | Medium | TASKS.md accountability |
| Dual standards for India vs export SKUs overlooked | Medium | Medium | Manufacturer research protocol |

## 13. Dependencies

- Human legal reviewers (qualified counsel for filing).  
- Access to primary databases (India Code, SCC Online/Manupatra or free official sources, EUR-Lex, OEM sites).  
- Optional: archive.org / permalink tools for web captures.  
- Runtime: Git, Markdown editor, later Python/Node for automation.  
- GitHub (or compatible) for issues, PRs, Actions.

## 14. Future Work

- Full multi-agent runtime (MASTER_PROMPT activation).  
- Citation linter and judgment schema.  
- Public website front-end (optional).  
- Multilingual plain-language summaries (Hindi and others).  
- Integration with RTI tracking.  
- Continuous monitoring of OEM policy changes.

## 15. Change Control

Material changes to Scope, Non-Scope, or Quality Gates require:

1. Issue or proposal in GitHub.  
2. Update to this specification.  
3. CHANGELOG entry.  
4. Project Manager acknowledgment in PR description.

---

*End of Project Specification v0.1.0 — Quality Gates (DoD) added 2026-07-30*
