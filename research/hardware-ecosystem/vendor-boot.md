---
title: "Vendor Boot Partition"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Vendor Boot Partition

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

Android 11 introduced vendor_boot to enable GKI: vendor-specific boot info is factored out of the boot partition. vendor_boot holds vendor ramdisk, DTB, and (v4) multiple ramdisk fragments including DLKM modules. Bootloader must load both boot and vendor_boot. Partition is A/B with virtual A/B and protected by Android Verified Boot.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Vendor boot partitions | https://source.android.com/docs/core/architecture/bootloader/partitions/vendor-boot-partitions | 2026-07-31 |
| 2 | Boot image header | https://source.android.com/docs/core/architecture/bootloader/boot-image-header | 2026-07-31 |
| 3 | Kernel module support | https://source.android.com/docs/core/architecture/kernel/kernel-module-support | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Why | Enable arbitrary device boot with GKI by separating vendor bits from generic boot |
| Contents | Header, vendor ramdisk(s), DTB; v4 adds ramdisk table and bootconfig |
| DLKM | Dynamic loadable kernel modules can live in vendor ramdisk fragments |
| Bootloader duty | Access both boot and vendor_boot; concatenate ramdisks correctly |
| Integrity | Protected by Verified Boot; A/B with virtual A/B |
| Character | Boot-chain packaging for GKI era |

## 4. Negative findings / gaps [FACT]

vendor_boot structure enables modular updates but does not define multi-year support duration.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Device-specific ramdisk fragment policies residual.

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
