---
title: "Security Update Flow — Comparative Synthesis"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Security Update Flow — Comparative Synthesis

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


## 1. Three-source model (WS2 ASB + WS3)

| Source | Who produces | How devices get it |
|--------|--------------|--------------------|
| Android platform fixes | Google/AOSP (ASB) | OEM merges & ships OTA (some Mainline modules via Play system updates) |
| Upstream Linux kernel fixes | kernel.org LTS → ACK/GKI | OEM ships kernel package / GKI image |
| SoC manufacturer fixes | Qualcomm et al. (public depth varies) | OEM integrates BSP/firmware & ships |

## 2. Security patch level

- WS2: devices report security patch levels corresponding to incorporated bulletin content when OEMs ship builds.  
- Play Integrity may surface “recent security updates” signals on some Android versions (WS2 play-integrity) — **measurement**, not OEM multi-year promise.

## 3. Comparison with product support (WS1)

| Concept | Evidence | Meaning |
|---------|----------|---------|
| Monthly ASB cadence | WS2 | Publication rhythm for fixes |
| Security support years | WS1 (where stated) | How long OEM says it will ship security updates for a product |
| ACK/GKI branch EOL | WS3 | When common kernel branch loses Google support |
| Device still “secure” after EOL | Not established as single rule in WS1–WS3 | Residual OPEN / empirical |

## 4. Synthesis

Security **content** flows from platform/kernel/SoC; security **duration for a retail model** is stated (when at all) in OEM policies (WS1). Common-kernel EOL (WS3) is a related but distinct technical window.

## Evidence pins

- WS2: `android-security-bulletins.md`, `security-patch-levels.md`, `monthly-security-updates.md`  
- WS3: `vendor-security-patches.md`, `android-common-kernel.md`, `KERNEL_LIFECYCLE_MATRIX.md`  
- WS1: coverage + lifecycle matrices


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
