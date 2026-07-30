---
title: "Generic Kernel Image (GKI)"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Generic Kernel Image (GKI)

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

The GKI project unifies the core Android kernel and moves SoC/board support into loadable vendor modules. GKI is built from ACK sources; single binary per architecture per LTS; stable KMI allows independent kernel vs module updates. Beginning Android 12, devices shipping kernel 5.10+ must ship GKI. Goals include delivering kernel security fixes without full vendor rebuild.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | GKI project | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | 2026-07-31 |
| 2 | Kernel overview (GKI architecture) | https://source.android.com/docs/core/architecture/kernel | 2026-07-31 |
| 3 | GKI release builds | https://source.android.com/docs/core/architecture/kernel/gki-release-builds | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Problem | Pre-GKI kernels had large out-of-tree customization → fragmentation, costly security backports, hard LTS merges |
| Design | Generic core kernel + vendor modules; no SoC/board code in GKI core |
| Requirement | Android 12+ with kernel ≥5.10 ship GKI |
| Update goal | Partners deliver kernel security/bug fixes without vendor image rebuild when KMI stable |
| Certified boot image | Google-certified GKI boot.img for boot partition |
| Character | Kernel architecture for updatability — not N-year retail support law |

## 4. Negative findings / gaps [FACT]

GKI enables independent core-kernel updates but vendor modules, firmware, and full platform images still require partner/OEM action.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. India SKU exceptions or delayed GKI adoption residual empirical capture.

## 7. Research confidence

**High** — based on official materials accessed 2026-07-31.

## 8. Cross references

- `research/android-ecosystem/` (platform update architecture — Phase 5 WS2)
- `research/manufacturers/` (OEM product policies — Phase 5 WS1)
- Other notes in `research/hardware-ecosystem/`
- `../../PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md`

## Audit trail

- Phase 5 Workstream 3 — Hardware & Chipset Ecosystem
- Official documentation only
- Descriptive only — no recommendations or legal interpretation
