---
title: "Bootloader & Secure Boot"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Bootloader & Secure Boot

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

The bootloader is the first software stage after hardware ROM; it verifies and loads subsequent images under Verified Boot. Official docs describe bootloader requirements for vendor_boot/GKI (must read both boot and vendor_boot). Secure boot / chain of trust begins at hardware root of trust. Rollback protection records versions to prevent booting older images.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Verified Boot | https://source.android.com/docs/security/features/verifiedboot | 2026-07-31 |
| 2 | Vendor boot — bootloader support | https://source.android.com/docs/core/architecture/bootloader/partitions/vendor-boot-partitions | 2026-07-31 |
| 3 | Boot flow / rollback | https://source.android.com/docs/security/features/verifiedboot/verified-boot | 2026-07-31 |
| 4 | Implement Bootconfig | https://source.android.com/docs/core/architecture/bootloader/implementing-bootconfig | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Role | Verify and load kernel/ramdisk/DTB; enforce AVB |
| GKI impact | Bootloader must support vendor_boot header formats v3/v4 |
| Secure boot | Hardware-backed root of trust anchors chain |
| Character | Critical for trusted update installation |

## 4. Negative findings / gaps [FACT]

Bootloader update availability and unlock policies are OEM/device-specific; not standardized as multi-year public floors in AOSP docs.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Per-OEM bootloader unlock and ARB (anti-rollback) bit practices residual.

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
