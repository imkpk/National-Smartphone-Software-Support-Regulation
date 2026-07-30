---
title: "Board Support Package (BSP) / Vendor software stack"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Board Support Package (BSP) / Vendor software stack

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

In Android architecture, device-specific hardware support is implemented via vendor partition components: HALs, vendor kernel modules, firmware blobs, and board configuration. Official AOSP docs describe HAL services that must implement required interfaces for a target release on the vendor partition. Pre-GKI, SoC/OEM device-specific kernel changes lived in-tree; GKI moves SoC/board support to loadable vendor modules.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | HAL overview | https://source.android.com/docs/core/architecture/hal | 2026-07-31 |
| 2 | Architecture overview | https://source.android.com/docs/core/architecture | 2026-07-31 |
| 3 | GKI — vendor modules | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | 2026-07-31 |
| 4 | Compatibility matrices (VINTF) | https://source.android.com/docs/core/architecture/vintf/comp-matrices | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| HAL role | Standard interface for hardware vendors without modifying higher layers |
| Vendor partition duty | Implement required HALs per compatibility matrix |
| GKI-era BSP kernel side | SoC/board support as loadable vendor modules, not GKI core |
| Update implication | BSP/vendor stack updates typically ship via OEM OTA / vendor images |
| Character | Technical vendor software bundle concept — detailed SoC BSP kits often partner-only |

## 4. Negative findings / gaps [FACT]

Complete commercial BSP packages (Qualcomm/MediaTek/etc. partner portals) are largely non-public; this note describes AOSP-visible architecture only.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Public BSP release notes per SoC generation residual OPEN.

## 7. Research confidence

**High for AOSP architecture; Moderate for vendor-specific BSP contents** — based on official materials accessed 2026-07-31.

## 8. Cross references

- `research/android-ecosystem/` (platform update architecture — Phase 5 WS2)
- `research/manufacturers/` (OEM product policies — Phase 5 WS1)
- Other notes in `research/hardware-ecosystem/`
- `../../PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md`

## Audit trail

- Phase 5 Workstream 3 — Hardware & Chipset Ecosystem
- Official documentation only
- Descriptive only — no recommendations or legal interpretation
