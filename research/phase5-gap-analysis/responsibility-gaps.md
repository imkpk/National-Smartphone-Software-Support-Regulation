---
title: "Responsibility Gaps — Phase 5 WS5"
domain: "phase5-gap-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS5"
---

# Responsibility Gaps — Phase 5 WS5

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

WS2 update responsibility / Google vs OEM notes; WS3 firmware responsibility matrix; WS4 consolidated responsibility matrix.

## 2. Responsibility map (what is described)

| Responsibility | Documented actor(s) in WS1–WS4 |
|----------------|--------------------------------|
| Publish ASB platform fixes | Google/AOSP |
| Publish SoC fixes | SoC vendors (public depth varies) |
| Maintain ACK/GKI | Google kernel; vendor modules from SoC/OEM |
| Build & ship full device OTA | Device OEM (primary shipper) |
| Mainline packages (GMS path) | Google packages; OEM eligibility |
| Product multi-year support statement | Device OEM (primary public face); Pixel as Google OEM |
| CDD/CTS execution | OEM executes; Google defines/tests |
| End-user install | End user |

## 3. Gaps [ANALYSIS]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| R-G1 | **No single actor** publicly owns an industry-wide multi-year floor for all devices | WS1–WS4 negative findings |
| R-G2 | **Duration commitments** sit mainly with OEM product policy, while **fix content** originates from platform/kernel/SoC — split is clear; joint public calendar is not | WS4 responsibility / security flow |
| R-G3 | Carrier OTA gating (where used) is noted as possible intermediate — not systematically mapped per India carrier in Phase 5 | WS2/WS4 responsibility matrix (limited) |
| R-G4 | Partner-only BSP responsibility details not fully public | WS3 |
| R-G5 | “Who ensures device remains secure after OEM EOL?” — **not established as a single rule** in WS1–WS4 | WS4 security-update-flow residual OPEN |

## 4. Explicit non-claims

This note does **not** assign legal liability or regulatory duty. It records **roles as described in repository technical and product-policy evidence**.


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

