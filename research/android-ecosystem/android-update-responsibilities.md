---
title: "Android Update Responsibilities (descriptive map)"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Android Update Responsibilities (descriptive map)

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

Official documentation distributes technical responsibilities across Google/AOSP (platform code, bulletins, Mainline modules, GKI/ACK), SoC vendors (chipset fixes), and OEMs (device builds, OTAs, vendor partitions, product support policies). This note maps those roles descriptively without assigning legal liability.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Architecture overview | https://source.android.com/docs/core/architecture | 2026-07-31 |
| 2 | Security bulletins — fix sources | https://source.android.com/docs/security/bulletin/asb-overview | 2026-07-31 |
| 3 | Mainline | https://source.android.com/docs/core/architecture/modular-system | 2026-07-31 |
| 4 | GKI | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | 2026-07-31 |
| 5 | OTA | https://source.android.com/docs/core/ota | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Google / AOSP | Publish platform source, CDD/CTS, security bulletins, Mainline modules, GKI/ACK maintenance |
| SoC vendors | Provide chipset/kernel/firmware fixes referenced in bulletins |
| OEMs | Integrate fixes, build device images, operate OTA pipelines, set product support lifetimes (WS1) |
| Carriers (where applicable) | May control OTA approval/distribution in some markets (implementation/business practice) |
| Users | Install offered updates; app updates via Play |
| Character | Descriptive responsibility map from platform docs — not legal allocation under Indian law |

## 4. Negative findings / gaps [FACT]

Platform docs describe technical roles; they do not create Indian statutory duties for multi-year support.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Contractual GMS terms between Google and OEMs remain largely non-public.

## 7. Research confidence

**High** — based on official source.android.com / developer.android.com / android.com materials accessed 2026-07-31.

## 8. Cross references

- `research/manufacturers/` (OEM lifecycle policies — Phase 5 WS1)
- `research/phase4-gap-analysis/` (government-side gaps)
- Other notes in `research/android-ecosystem/`
- `../../PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md`

## Audit trail

- Phase 5 Workstream 2 — Android Ecosystem
- Official Google / AOSP documentation only
- Descriptive only — no recommendations or legal interpretation
