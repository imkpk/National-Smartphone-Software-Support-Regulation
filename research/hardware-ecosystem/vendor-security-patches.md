---
title: "Vendor / SoC Security Patches"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Vendor / SoC Security Patches

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

Official Android Security Bulletin documentation states fixes come from AOSP, upstream Linux kernel, and SOC manufacturers; SoC fixes are available directly from manufacturers. Chipset vendors such as Qualcomm publish their own security bulletins for OEM customers. Device manufacturers must still integrate and ship patches.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | ASB sources | https://source.android.com/docs/security/bulletin/asb-overview | 2026-07-31 |
| 2 | Qualcomm security bulletins | https://docs.qualcomm.com/product/publicresources/securitybulletin | 2026-07-31 |
| 3 | Samsung Mobile Security | https://security.samsungmobile.com/securityUpdate.smsb | 2026-07-31 |
| 4 | OTA updates | https://source.android.com/docs/core/ota | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Three-source model | Platform (AOSP) · Kernel (upstream/LTS/ACK) · SoC vendor |
| OEM duty | Integrate all applicable sources into device builds and ship OTA |
| Publication ≠ ship | Bulletin existence does not equal universal device deployment |
| Character | Descriptive patch supply chain |

## 4. Negative findings / gaps [FACT]

No official global SLA binds all SoC vendors to identical multi-year public patch calendars for every SKU.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Latency statistics bulletin→India retail device residual empirical.

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
