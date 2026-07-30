---
title: "Lifecycle Comparison — Product, Platform, Kernel, Firmware"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Lifecycle Comparison — Product, Platform, Kernel, Firmware

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


## 1. Lifecycle types compared

| Lifecycle type | Whose clock? | Public multi-year tables in repo? | Workstream |
|----------------|--------------|-----------------------------------|------------|
| **Product OS/security support** | Device OEM | Yes for some brands; uneven | WS1 |
| **Android platform release** | Google AOSP | Versioned CDD/CTS; not consumer N-year floor | WS2 |
| **ACK / GKI kernel branch** | Google kernel team | Yes — EOL years in AOSP ACK table | WS3 |
| **Upstream LTS** | kernel.org | Yes — projected EOL | WS3 |
| **SoC firmware** | SoC + OEM | Uneven public depth | WS3 |
| **Mainline module currency** | Google Play / partner | Ongoing modular updates while eligible | WS2 |

## 2. Descriptive alignment (not identity)

These clocks are **not the same**:
- A device can remain in an OEM multi-year window (WS1) while running a kernel branch approaching ACK EOL (WS3) — relationship is product-specific (residual OPEN per SKU).  
- ASB continues monthly (WS2) independently of any single OEM’s end-of-support date (WS1).  
- Apple’s model (WS1) uses security-release/vintage documentation rather than Pixel-style single N-year table.

## 3. Negative synthesis

Across all three workstreams, repository evidence does **not** establish:
1. One industry-wide multi-year OS floor for all manufacturers  
2. One platform-doc multi-year device floor  
3. One public multi-year chipset/firmware floor for all SoCs  

## Evidence pins

- WS1 lifecycle + negative finding  
- WS2 platform negative finding  
- WS3 hardware negative finding + kernel lifecycle matrix


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
