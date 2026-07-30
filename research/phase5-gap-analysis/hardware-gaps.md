---
title: "Hardware, Chipset, Kernel, and Firmware Gaps — Phase 5 WS5"
domain: "phase5-gap-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS5"
---

# Hardware, Chipset, Kernel, and Firmware Gaps — Phase 5 WS5

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

WS3 hardware ecosystem notes and matrices; WS4 chipset responsibility, platform dependency, lifecycle matrices.

## 2. Gaps identified [ANALYSIS from WS3/WS4 FACT]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| H-G1 | **No universal multi-year consumer chipset/firmware support floor** across SoC vendors | WS3 negative finding |
| H-G2 | **ACK/GKI/LTS multi-year tables** are kernel-branch maintenance windows — not automatic OEM product multi-year OS promises | WS3 kernel lifecycle; WS4 lifecycle |
| H-G3 | **SoC public documentation uneven** — Qualcomm security bulletins strong; MediaTek/UNISOC multi-year public matrices sparse | WS3 chipset support matrix |
| H-G4 | **Detailed BSP packages largely partner-only** — not fully capturable as public consumer matrices | WS3 BSP residual |
| H-G5 | **ASB SoC-source fixes** still require OEM integration and shipping | WS3 vendor-security-patches; WS2 ASB |
| H-G6 | **TEE / modem / bootloader / firmware** update calendars not standardized as public N-year consumer matrices across vendors | WS3 firmware lifecycle / TEE / bootloader |
| H-G7 | **KMI stability** enables independent GKI updates only when frozen — KMI break implies vendor module rebuild | WS3 KMI; WS4 dependency matrix |

## 3. What is present (contrast)

- LTS → ACK → GKI architectural chain  
- Published ACK support / EOL tables (4–6 years by branch, as captured)  
- Qualcomm public security bulletin channel  
- Tensor dual role with Pixel product pages (OEM + SoC)  
- Firmware responsibility split documented  

## 4. Dependency gap (descriptive)

Long-term device security depends on a **chain** (platform fixes + kernel + SoC firmware + OEM integration). A gap or stop at any link can interrupt updates even if other links continue (WS4 platform dependency matrix).


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

