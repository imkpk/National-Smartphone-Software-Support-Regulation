# Phase 5 Specification — Manufacturers & Technical Baseline

**Phase:** 5  
**Status:** In progress  
**OS:** Bound by [`REPOSITORY_OS.md`](REPOSITORY_OS.md)  
**Version note:** Phase 5 research under `0.6.x`  

---

## 1. Objectives

Document **published manufacturer software/security update lifecycle commitments** and related **technical baseline** evidence (Android platform ecosystem, hardware/chipset stack, etc.) for smartphones relevant to the India research repository.

**Descriptive only.** No recommendations, legal conclusions, or policy drafting.

---

## 2. Prerequisites

| Prerequisite | Required |
|--------------|----------|
| Phase 4 Complete | Yes (v0.6.0) |
| REPOSITORY_OS | Active |
| Latest main | Clean sync |

---

## 3. Workstream sequence

| WS | Title | Path | Status |
|----|-------|------|--------|
| 1 | Manufacturers & Technical Baseline (OEM policies) | `research/manufacturers/` | **Complete** (v0.6.1, PR #26) |
| 2 | Android Ecosystem | `research/android-ecosystem/` | **Complete** (v0.6.2, PR #27) |
| 3 | Hardware & Chipset Ecosystem | `research/hardware-ecosystem/` | **Complete** (v0.6.3, PR #28) |
| 4 | Comparative Analysis | `research/comparative-analysis/` | **Complete** (v0.6.4, PR #29) |
| 5 | Gap Analysis | `research/phase5-gap-analysis/` | **Complete** (v0.6.5, PR #30) |
| 6 | Repository Audit | `audit/phase5/` | **This workstream** (v0.6.6) |
| 7+ | Further Phase 5 (as later specified) | TBD | Not started |

---

## 4. WS1 scope (complete)

Official manufacturer documentation for listed OEMs.

---

## 5. WS2 scope (complete)

Official Google / AOSP Android platform & update infrastructure documentation.

---

## 6. WS3 scope (complete)

Official documentation covering hardware/chipset stack enabling updates (LTS, ACK, GKI, KMI, BSP, firmware, TEE, SoC vendors).

---

## 7. WS4 scope (complete)

**Descriptive comparison only** of findings from WS1–WS3. **No new research.**

---

## 8. WS5 scope (complete)

**Descriptive gap analysis only** based on WS1–WS4 repository evidence. **No new research.**

---

## 9. WS6 scope

**Repository audit only** of Phase 5 WS1–WS5. **No new research. No new analysis. No rewrite of workstream conclusions.**

Verify completeness, consistency, cross references, documentation quality, evidence traceability, repository health, residual OPEN inventory.

### Expected WS6 outputs

- `audit/phase5/` checklist, summary, health, consistency, cross-ref, citation, version, relevance, knowledge-graph, residual reports  
- `orchestration/PHASE_05_WS6_GATE_REPORT.md`  
- Documentation updates  

### WS6 exclusions

- Web research or new evidence  
- Expanding or rewriting WS1–WS5 research packages  
- Phase 5 completion close  
- Phase 6 start  
- Multiple workstreams per PR  
- Auto-start of WS7  

---

## 10. Exclusions (phase-wide)

- New Indian government research (Phase 4 closed)  
- Litigation / policy advocacy  
- Multiple workstreams per PR  
- Auto-start of the next workstream after merge  

---

## 11. Completion of Phase 5

Phase 5 completes only after all planned Phase 5 workstreams + audit + formal close (later). **WS1–WS6 alone do not close Phase 5** until a dedicated completion workstream is authorised.

---

*Phase 5 specification — updated WS6*
