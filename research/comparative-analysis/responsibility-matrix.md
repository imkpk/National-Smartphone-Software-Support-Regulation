---
title: "Consolidated Responsibility Matrix — Descriptive"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Consolidated Responsibility Matrix — Descriptive

## Repository Relevance

**Why this document belongs in the repository:**  
Phase 5 Workstreams 1–3 collected manufacturer policies, Android platform architecture, and hardware/chipset evidence. Comparative synthesis organises that evidence for later phases without adding new external research.

**Tags:** Comparative analysis · Phase 5 · Repository Cross Reference

## Classification

**ANALYSIS** — Descriptive comparison of existing repository evidence. **Not** legal conclusions; **not** recommendations; **not** manufacturer rankings; **not** compliance evaluations.

## Evidence sources (repository only)

| Workstream | Path / report |
|------------|---------------|
| WS1 Manufacturers | `research/manufacturers/` · `PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md` |
| WS2 Android Ecosystem | `research/android-ecosystem/` · `PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS3 Hardware Ecosystem | `research/hardware-ecosystem/` · `PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md` |

**Rule:** No new external research in this workstream.


## Consolidated map (WS1 + WS2 + WS3)

| Responsibility | Google platform | SoC vendor | Device OEM | Carrier (where used) | End user |
|----------------|-----------------|------------|------------|----------------------|----------|
| Publish ASB / AOSP fixes | ● | chipset fixes ● | integrate/ship ● | may gate OTA | install |
| Maintain ACK/GKI | ● | vendor modules ● | ship device package ● | — | — |
| SoC firmware patches | — | ● | integrate/ship ● | — | — |
| Full system OTA | base code ● | BSP pieces ● | **build & ship ●** | may distribute | install |
| Mainline packages | build/sign (GMS) ● | — | optional partner OTA | — | receive |
| Product multi-year support statement | Pixel as OEM ● | rarely public matrix | **primary ●** | — | purchase choice |
| CDD/CTS/VTS compliance | define/test ● | support ● | execute ● | — | — |
| Verified Boot / TEE | specs / Trusty ● | hardware TEE ● | configure/sign ● | — | — |

**Legend:** ● = role described in repository evidence. Not a legal liability assignment.

## Evidence pins

- WS2 `ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md`  
- WS3 `FIRMWARE_RESPONSIBILITY_MATRIX.md`  
- WS1 manufacturer notes (product support column)


## Negative findings

See `negative-finding-comparative-no-single-unified-support-floor.md` and per-workstream negative findings.

## Cross references

- All matrices in this folder
- `../../PHASE_05_COMPARATIVE_ANALYSIS_WORKSTREAM_REPORT.md`
- Phase 4 gap analysis (government-side legal floor negative finding — context only; not re-researched)

## Audit trail

- Phase 5 Workstream 4 — Comparative Analysis
- Synthesis only — no new web research
- Descriptive only
