---
title: "Android Platform Gaps — Phase 5 WS5"
domain: "phase5-gap-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS5"
---

# Android Platform Gaps — Phase 5 WS5

## Repository Relevance

**Why this document belongs in the repository:**  
Phase 5 Workstreams 1–4 collected manufacturer policies, Android platform architecture, hardware/chipset evidence, and comparative synthesis. Gap analysis organises **descriptive absences and residual OPENs** in that evidence for later phases without adding new external research.

**Tags:** Phase 5 · Gap analysis · Repository Cross Reference

## Classification

**ANALYSIS** — Descriptive gap synthesis of existing repository evidence. **Not** legal conclusions; **not** recommendations; **not** manufacturer rankings; **not** compliance evaluations; **not** predictions.

## Evidence sources (repository only)

| Workstream | Path / report |
|------------|---------------|
| WS1 Manufacturers | `research/manufacturers/` · `PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md` |
| WS2 Android Ecosystem | `research/android-ecosystem/` · `PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS3 Hardware Ecosystem | `research/hardware-ecosystem/` · `PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS4 Comparative Analysis | `research/comparative-analysis/` · `PHASE_05_COMPARATIVE_ANALYSIS_WORKSTREAM_REPORT.md` |

**Rule:** No new external research or new citations as authorities in this workstream.



## 1. Evidence base

WS2 Android ecosystem notes, update responsibility matrix, platform negative finding; WS4 android responsibility and software/security flow matrices.

## 2. Gaps identified [ANALYSIS from WS2/WS4 FACT]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| A-G1 | Platform docs describe **how** updates work (OTA, Mainline, GKI, CDD/CTS) — **not** a universal multi-year consumer device floor | WS2 negative finding |
| A-G2 | **ASB publication ≠ universal device shipping** — integration/ship remains OEM/SoC-dependent | WS2 ASB / monthly security notes |
| A-G3 | **Mainline / Play System Updates are partial** — selected modules only; kernel/vendor/non-modular surfaces remain full-OTA dependent | WS2 Mainline / component matrix |
| A-G4 | **GKI/ACK lifetimes ≠ OEM product marketing support years** | WS2 GKI; WS3 ACK; WS4 lifecycle comparison |
| A-G5 | **CDD/CTS/VTS** define compatibility policy/tests — not multi-year support duration for retail models | WS2 CDD/CTS/VTS |
| A-G6 | **GMS commercial partner terms** not fully public as a single consumer-facing multi-year matrix on pages reviewed in WS2 | WS2 negative finding |
| A-G7 | Android Enterprise / Enterprise Recommended document **managed-device capabilities**, not a consumer multi-year legal floor | WS2 enterprise notes |
| A-G8 | Play Integrity may surface “recent security updates” signals — **measurement**, not OEM multi-year promise | WS2 play-integrity; WS4 security flow |

## 3. What is present (contrast)

- Rich architecture for multi-path updates  
- Monthly ASB process documentation  
- Treble / vendor interface separation  
- GKI requirements for modern Android kernels  
- Explicit Google vs OEM responsibility language in platform notes  

## 4. Responsibility implication (descriptive)

Where multi-year **duration** is documented for a retail device, repository evidence points primarily to **OEM product policy (WS1)**, not platform CDD text (WS2).


## Negative findings

See `negative-findings.md` and per-workstream negative findings (WS1–WS4).

## Cross references

- All matrices and reports in this folder
- `../../PHASE_05_GAP_ANALYSIS_WORKSTREAM_REPORT.md`
- Phase 4 gap analysis (`research/phase4-gap-analysis/`) — government-side context only; not re-researched

## Audit trail

- Phase 5 Workstream 5 — Gap Analysis
- Synthesis only — no new web research
- Descriptive gaps only

