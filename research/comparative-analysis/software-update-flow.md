---
title: "Software Update Flow — Comparative Synthesis"
domain: "comparative-analysis"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS4"
---

# Software Update Flow — Comparative Synthesis

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


## 1. Multi-path update model (WS2 + WS3 + WS1 delivery)

```
[AOSP / ASB / LTS / SoC fixes]
        │
        ▼
[OEM / partner integration]
        │
        ├── Full system OTA (A/B or Virtual A/B)  ← WS2 OTA docs
        ├── Mainline modules via Play system updates or partner OTA  ← WS2
        ├── GKI boot image (when KMI allows)  ← WS2/WS3
        ├── Vendor image / vendor_boot modules  ← WS3
        ├── Firmware (modem, TEE, bootloader, …)  ← WS3
        └── User apps via Google Play (not OS)  ← WS2
        │
        ▼
[End device]  ← duration of offers governed by OEM product policy (WS1)
```

## 2. Flow vs commitment

| Stage | Documented in | Sets multi-year duration? |
|-------|---------------|---------------------------|
| Fix publication | WS2 ASB, WS3 SoC bulletins | No |
| Integration | Implied OEM duty (WS2/WS3) | No |
| Shipping channels | WS2 OTA/Mainline; WS3 GKI/vendor | No |
| How long offers continue | **WS1 OEM policies** | **Yes (where published)** |

## 3. Mainline / Play System Updates impact (descriptive)

- Cover **selected modular components** only (WS2 project-mainline / component matrix).  
- Do **not** replace kernel/vendor/firmware paths (WS2/WS3).  
- Do **not** create multi-year product floors (WS1 negative finding + WS2 platform negative finding).

## Evidence pins

- WS2: `update-distribution-architecture.md`, `android-upgrade-process.md`, `project-mainline.md`, `play-system-updates.md`  
- WS3: `firmware-lifecycle.md`, `generic-kernel-image.md`, `vendor-boot.md`  
- WS1: manufacturer lifecycle matrix


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
