---
title: "MediaTek — public documentation orientation"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — MediaTek — public documentation orientation

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

MediaTek is a major smartphone SoC vendor supplying platforms widely used in India-volume devices. Android platform architecture treats SoC vendors as providers of chipset/kernel/firmware fixes referenced in security bulletins. Public MediaTek developer documentation depth for multi-year Android security support matrices is limited compared with AOSP kernel docs; detailed BSP materials are typically partner-gated.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | ASB — SOC manufacturer fixes (generic role) | https://source.android.com/docs/security/bulletin/asb-overview | 2026-07-31 |
| 2 | GKI / vendor modules | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | 2026-07-31 |
| 3 | HAL overview (vendor implementation) | https://source.android.com/docs/core/architecture/hal | 2026-07-31 |
| 4 | AOSP architecture | https://source.android.com/docs/core/architecture | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Architectural role | SoC vendor: BSP, vendor modules, firmware, HAL implementations |
| Update path | Fixes → OEM integration → device OTA |
| Public matrix | Dedicated public multi-year MediaTek Android support matrix not captured in this pass |
| Character | SoC vendor in Android hardware stack |

## 4. Negative findings / gaps [FACT]

Official publicly crawlable multi-year MediaTek security-update duration tables for mobile platforms were **not identified** in this workstream; residual OPEN for partner portal materials.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. MediaTek official public security bulletin index URL if published.
2. India Helio/Dimensity platform support windows.

## 7. Research confidence

**Moderate — architecture clear; vendor public lifecycle docs sparse** — based on official materials accessed 2026-07-31.

## 8. Cross references

- `research/android-ecosystem/` (platform update architecture — Phase 5 WS2)
- `research/manufacturers/` (OEM product policies — Phase 5 WS1)
- Other notes in `research/hardware-ecosystem/`
- `../../PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md`

## Audit trail

- Phase 5 Workstream 3 — Hardware & Chipset Ecosystem
- Official documentation only
- Descriptive only — no recommendations or legal interpretation
