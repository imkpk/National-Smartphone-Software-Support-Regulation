---
title: "Comparison Overview — Phase 5 WS1–WS3"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Comparison Overview — Phase 5 WS1–WS3

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


## 1. Three evidence layers compared

| Layer | Workstream | What was documented | What was *not* documented as law |
|-------|------------|---------------------|----------------------------------|
| **Product policies** | WS1 | OEM published OS/security support statements | Industry-wide multi-year legal floor |
| **Platform architecture** | WS2 | AOSP update paths, Mainline, ASB, CDD/CTS, Treble/GKI, responsibilities | Universal multi-year device floor in platform docs |
| **Hardware/firmware** | WS3 | LTS→ACK→GKI, SoC roles, firmware/TEE/boot chain | Universal multi-year chipset/firmware consumer floor |

## 2. Cross-layer descriptive synthesis

1. **Capability vs commitment:** WS2/WS3 describe *how* updates can be produced and delivered; WS1 describes *what* OEMs *publicly promise* for product lines. These are different evidence classes.
2. **Publication ≠ delivery:** WS2 (ASB) and WS3 (SoC fixes) show fixes may be published without every device receiving them; WS1 shows shipping/support duration is product-policy driven.
3. **Partial modular paths:** Mainline / Play System Updates (WS2) and GKI/KMI (WS2/WS3) reduce some update friction but do not replace full OEM OTA for vendor/firmware surfaces.
4. **Heterogeneity:** WS1 manufacturer matrices are uneven; WS3 chipset public matrices are uneven; together they show **no single public multi-year floor** across brands or SoCs.
5. **Google dual role:** As platform steward (WS2/WS3) and as Pixel OEM (WS1), Google publishes clearer product multi-year windows for Pixel than many third-party OEMs — still a private product policy, not Indian law.

## 3. Evidence map (traceability)

| Comparison question | Primary evidence |
|---------------------|------------------|
| Who publishes multi-year product support? | WS1 manufacturer notes + lifecycle matrix |
| Who publishes platform security fixes? | WS2 security bulletins + update responsibility matrix |
| Who supplies kernel/firmware pieces? | WS3 firmware responsibility + kernel lifecycle matrices |
| What delivery channels exist? | WS2 OTA / Mainline / Play system updates; WS3 vendor_boot / GKI |
| What is missing industry-wide? | All three negative findings |

## 4. Scope of this workstream

WS1–WS3 repository evidence only. No rankings, no compliance scoring, no policy proposals.


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
