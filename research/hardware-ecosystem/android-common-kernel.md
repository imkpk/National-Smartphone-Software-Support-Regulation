---
title: "Android Common Kernel (ACK)"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Android Common Kernel (ACK)

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

Android Common Kernels (ACKs) are downstream of kernel.org LTS kernels and include Android-specific patches. Hosted at android.googlesource.com/kernel/common. GKI kernels (5.10+) are ACKs with stable KMI. ACK branches receive regular LTS merges and Android Security Bulletin-relevant kernel fixes. Official tables list multi-year ACK support lifetimes and EOL dates.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Android common kernels | https://source.android.com/docs/core/architecture/kernel/android-common | 2026-07-31 |
| 2 | Kernel overview | https://source.android.com/docs/core/architecture/kernel | 2026-07-31 |
| 3 | kernel/common repository | https://android.googlesource.com/kernel/common/ | 2026-07-31 |
| 4 | Android Security Bulletins | https://source.android.com/docs/security/bulletin/asb-overview | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Source base | Downstream of LTS + Android-interest patches |
| android-mainline | Primary Android feature development branch; new LTS → new ACK branch |
| LTS merges | Regular merges into ACK branches after upstream LTS posts |
| Security | ACK receives LTS + Android-specific bugfixes including ASB-cited kernel patches |
| Support lifetimes | Official table: e.g. 4–6 years depending on branch; EOL dates published; after EOL Google no longer supports; devices on EOLed kernels considered vulnerable per AOSP docs |
| Character | Common kernel maintenance windows — distinct from OEM product marketing |

## 4. Negative findings / gaps [FACT]

ACK EOL means Google/common-kernel support ends; OEM may still ship devices without common-kernel updates. Not a consumer legal multi-year floor.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Partner out-of-tree patches not in ACK remain vendor responsibility.

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
