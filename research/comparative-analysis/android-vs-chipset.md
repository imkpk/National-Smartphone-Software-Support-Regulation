---
title: "Android Platform vs Chipset Responsibilities"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Android Platform vs Chipset Responsibilities

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


## 1. Responsibility split (WS2 + WS3)

| Domain | Android platform (Google/AOSP) | Chipset / SoC | Device OEM |
|--------|--------------------------------|---------------|------------|
| Framework / many system components | Primary (AOSP + Mainline where modular) | — | Integrates skin/builds |
| Security bulletin platform fixes | Publishes / merges AOSP | — | Ships OTA |
| Upstream/LTS kernel fixes | Merges into ACK/GKI | May contribute | Ships device kernel package |
| SoC proprietary firmware / modem | — | Develops / bulletins (where public) | Integrates & ships |
| Vendor kernel modules / HALs | Defines interfaces (Treble/HAL/KMI) | Implements for SoC | Integrates on product |
| Product support years | Pixel only as OEM | Rarely as consumer matrix | **Primary public face (WS1)** |

## 2. Architectural enablers (not duration promises)

| Mechanism | Workstream | Effect on updates |
|-----------|------------|-------------------|
| Treble / vendor interface | WS2 | Separates framework from vendor implementation |
| GKI + KMI | WS2/WS3 | Core kernel updatable without full vendor rebuild when KMI stable |
| Mainline / Play system updates | WS2 | Modular components outside full OS image |
| vendor_boot | WS3 | Packages vendor ramdisk/modules separately from GKI boot |
| ASB three-source model | WS2/WS3 | Platform + kernel + SoC fixes must all be integrated |

## 3. Synthesis

Chipset vendors and Google platform provide **inputs** to device security; OEMs remain the typical **integrator and shipper** of full device updates and the typical **publisher** of multi-year product support statements (WS1).

## Evidence pins

- WS2: `ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md`, Mainline, Treble, ASB notes  
- WS3: `FIRMWARE_RESPONSIBILITY_MATRIX.md`, GKI, KMI, SoC notes, vendor-security-patches


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
