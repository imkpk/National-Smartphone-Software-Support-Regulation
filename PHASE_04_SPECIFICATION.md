# Phase 4 Specification — Government Policy & Institutions

**Phase:** 4  
**Status:** **Complete** (v0.6.0)  
**OS:** Bound by [`REPOSITORY_OS.md`](REPOSITORY_OS.md)  
**Version note:** Phase 4 closed at **0.6.0**; research workstreams shipped under `0.5.x`  

---

## 1. Objectives

Map **government policy, institutions, standards/guidance, consultations, and programmes** relevant to smartphone software support, security updates, device longevity, consumer protection, digital safety, e-waste, and cyber security — **official evidence only**.

Descriptive research. **No advocacy. No litigation. No legislative drafting.**

---

## 2. Prerequisites (Dependency Engine)

| Prerequisite | Required state |
|--------------|----------------|
| Phase 3 | Complete on main |
| REPOSITORY_OS | Active (v1.0+) |
| Latest main | Clean sync before each workstream |
| Prior Phase 4 WS | Previous WS merged before next starts |

---

## 3. Workstream sequence (do not reorder)

| WS | Name | Output path | Status (maintain via orchestration) |
|----|------|-------------|-------------------------------------|
| 1 | Government Policies | `research/policy/` | **Complete** (PR #17) |
| 2 | Government Institutions | `research/institutions/` | **Complete** (PR #18) |
| 3 | Standards & Technical Guidance | `research/standards/` | **Complete** (PR #20) |
| 4 | Public Consultations | `research/consultations/` | **Complete** (PR #21) |
| 5 | Government Programmes | `research/programs/` | **Complete** (PR #22) |
| 6 | Gap Analysis | `research/phase4-gap-analysis/` | **Complete** (PR #23) |
| 7 | Phase 4 Audit | `PHASE_4_AUDIT.md` + related | **Complete** (PR #24) |
| 8 | Formal Completion | `PHASE_04_COMPLETION_REPORT.md` + close package | **Complete** (PR #25) |

---

## 4. Workstream definitions

### WS1 — Government Policies

National digital, electronics, telecom, cyber, repair/longevity policy framing.  
**Done when:** policy notes + POLICY_* reports + negative finding (if applicable) + workstream report.

### WS2 — Government Institutions

Mandates, responsibilities, RACI-style analytical matrix, TRAI/RBI-NPCI relevance.  
Cross-link Phase 3 regulators — do not rewrite.  
**Done when:** institution notes + INSTITUTION_* reports + negative finding + workstream report + RACI.

### WS3 — Standards & Technical Guidance

BIS, CERT-In guidance, security baselines, repairability/software maintenance standards **if official**.  
**Done when:** standards notes + STANDARD_* (or equivalent) reports + negative finding + workstream report.  
**Must include Repository Relevance on every new note.**

### WS4 — Public Consultations

Official consultation/discussion/draft papers only.  
**Done when:** consultation notes + reports + negative finding if none found + workstream report.

### WS5 — Government Programmes

Digital India depth, electronics schemes, circular economy / e-waste programmes, consumer awareness — official only. Avoid pure duplicate of WS1 framing notes; deepen programme artefacts.  
**Done when:** programme notes + reports + workstream report.

### WS6 — Gap Analysis

Synthesize WS1–WS5 only. **No recommendations.**  
**Done when:** gap docs + matrices + validation + workstream report.

### WS7 — Audit

Verify WS1–WS6 + docs consistency.  
**Outputs:** `PHASE_4_AUDIT.md`, audit summary/checklist as needed.

### WS8 — Completion

Only if audit PASS or PASS WITH MINOR ISSUES.  
**Outputs:** `PHASE_04_COMPLETION_REPORT.md`, release notes, final validation; version bump; mark Phase 4 complete.  
**Do not begin Phase 5.**

---

## 5. Expected outputs (every research workstream WS1–WS6)

- Domain folder + notes  
- Coverage matrix  
- Source report  
- Citation report  
- Validation report  
- Negative finding (if applicable)  
- Workstream report (`PHASE_04_*_WORKSTREAM_REPORT.md`)  
- Documentation updates (README, CHANGELOG, TASKS, phase-04)  
- Orchestration state/gate notes  

---

## 6. Exclusions (entire phase)

- Manufacturer OEM policy catalogue (Phase 5)  
- Economics deep pack  
- Litigation drafting  
- Comparative expansion beyond existing Phase 3 international notes (unless official Indian consultation cites foreign law — then cite carefully as secondary)  
- Architecture/governance changes outside REPOSITORY_OS maintenance  
- Multiple workstreams per PR  

---

## 7. Completion criteria

Phase 4 is complete only when:

1. WS1–WS6 complete and merged  
2. Audit PASS or PASS WITH MINOR ISSUES  
3. Completion package generated  
4. TASKS / README / CHANGELOG mark Phase 4 Complete  
5. Version updated  
6. Human approval after each merge observed  

---

## 8. Relationship to Phase 3

Phase 3 closed at **v0.5.0**. Phase 4 does not reopen judgments/statutes research except cross-reference.

---

*Phase 4 specification — keep OS rules in REPOSITORY_OS.md*
