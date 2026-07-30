---
title: "Manufacturer Product Policies vs Google Platform Role"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Manufacturer Product Policies vs Google Platform Role

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


## 1. Distinction of roles (from WS1 + WS2)

| Role | Evidence | Character |
|------|----------|-----------|
| Google as **platform steward** | WS2 AOSP, ASB, Mainline, GKI/ACK, CDD/CTS | Publishes code, bulletins, modular updates, compatibility program |
| Google as **Pixel OEM** | WS1 google-pixel.md | Publishes multi-year Pixel OS/security windows (e.g. 7y / 5y by generation) |
| Third-party **device OEMs** | WS1 other manufacturer notes | Publish product support policies of varying clarity |
| **SoC vendors** | WS3 | Supply chipset/firmware fixes; public multi-year consumer matrices uneven |

## 2. Descriptive comparison (not ranking)

| Dimension | Platform docs (WS2/WS3) | Pixel product policy (WS1) | Typical third-party OEM (WS1) |
|-----------|-------------------------|---------------------------|------------------------------|
| Multi-year OS table | Not as industry floor | Captured for listed generations | Strong for some (e.g. Samsung series); residual OPEN for several brands |
| Security cadence narrative | Monthly ASB process | Within multi-year window | Series/product specific or residual OPEN |
| Mainline/Play system updates | Documented as modular path | Applies where GMS/Mainline present | Device-dependent |
| Legal character | Not Indian law | Private product policy | Private product policy |

## 3. Synthesis statement

WS2/WS3 **enable** updates; WS1 **states product-level duration** where OEMs publish it. Platform documentation does **not** substitute for OEM multi-year product matrices, and OEM matrices do **not** create Indian statutory duties (Phase 4 context).

## Evidence pins

- `research/manufacturers/google-pixel.md`, `samsung-galaxy.md`, coverage/lifecycle matrices  
- `research/android-ecosystem/google-vs-oem-responsibilities.md`, `android-update-responsibilities.md`  
- `research/hardware-ecosystem/tensor.md` (Google as SoC+OEM on Pixel)


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
