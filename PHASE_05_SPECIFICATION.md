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
| 5 | Gap Analysis | `research/phase5-gap-analysis/` | **This workstream** (v0.6.5) |
| 6+ | Further Phase 5 (as later specified) | TBD | Not started |

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

## 8. WS5 scope

**Descriptive gap analysis only** based on WS1–WS4 repository evidence. **No new research.**

Identify descriptive gaps concerning: manufacturer support commitments; Android platform, chipset, kernel, firmware, security, and OS update responsibilities; platform dependencies; documentation / standards / evidence availability; technical responsibilities; support lifecycle transparency; update mechanisms.

### Expected WS5 outputs

- `research/phase5-gap-analysis/` notes and matrices  
- Coverage / citation / validation / consistency / cross-reference / negative-findings reports  
- `PHASE_05_GAP_ANALYSIS_WORKSTREAM_REPORT.md`  
- Documentation updates  

### WS5 exclusions

- Additional web research or new evidence captures  
- New external citations as authorities  
- Rankings, compliance evaluation, legislation/regulation recommendations  
- Re-writing WS1–WS4 primary notes  
- Multiple workstreams per PR  
- Auto-start of WS6  

---

## 9. Exclusions (phase-wide)

- New Indian government research (Phase 4 closed)  
- Litigation / policy advocacy  
- Multiple workstreams per PR  
- Auto-start of the next workstream after merge  

---

## 10. Completion of Phase 5

Phase 5 completes only after all planned Phase 5 workstreams + audit + close (later). **WS1–WS5 alone do not close Phase 5.**

---

*Phase 5 specification — updated WS5*
