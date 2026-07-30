---
title: "Kernel Module Interface (KMI)"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Kernel Module Interface (KMI)

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

KMI is the stable interface between the GKI kernel and vendor modules, consisting of symbol lists of functions and global data required by vendor modules. KMI is identified by Android platform release + kernel version (e.g. android14-6.1). ACK KMI branches pass through development, stabilization, and frozen phases. KMI generation changes require vendor module rebuild.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Kernel overview — KMI definition | https://source.android.com/docs/core/architecture/kernel | 2026-07-31 |
| 2 | Android common kernels — ACK KMI lifecycle | https://source.android.com/docs/core/architecture/kernel/android-common | 2026-07-31 |
| 3 | GKI project | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Purpose | Allow vendor modules and GKI kernel to update independently when KMI stable |
| Naming | ANDROID_RELEASE-KERNEL_VERSION (e.g. android15-6.6) |
| Lifecycle | Dev → stabilization (KMI tracking) → frozen (no KMI breaks except serious security) |
| Generation | KMI generation in uname; change breaks prior vendor modules until rebuilt |
| Cross-GKI | KMI compatibility not maintained across different GKI kernels |
| Character | ABI stability contract for kernel modules |

## 4. Negative findings / gaps [FACT]

Stable KMI does not eliminate need for vendor module security patches or firmware updates.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Partner symbol-list processes are largely internal to GKI partnerships.

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
