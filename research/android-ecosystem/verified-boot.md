---
title: "Android Verified Boot"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Android Verified Boot

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

Verified Boot ensures executed code comes from a trusted source (usually device OEMs) via a chain of trust from hardware root of trust through bootloader to verified partitions (boot, system, vendor, etc.). Android 8+ includes Android Verified Boot (AVB) working with Treble, standardizing footers and rollback protection features.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Verified Boot overview | https://source.android.com/docs/security/features/verifiedboot | 2026-07-31 |
| 2 | Use Verified Boot | https://source.android.com/docs/security/features/verifiedboot/verified-boot | 2026-07-31 |
| 3 | AVB | https://source.android.com/docs/security/features/verifiedboot/avb | 2026-07-31 |
| 4 | dm-verity | https://source.android.com/docs/security/features/verifiedboot/dm-verity | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Chain of trust | Hardware root → bootloader → partitions |
| Enforcement history | Android 7.0 strict enforcement; earlier versions warned |
| dm-verity | Hash-tree verification for large partitions |
| AVB | Reference implementation with Treble; standardized footers; rollback features |
| Character | Device integrity architecture |

## 4. Negative findings / gaps [FACT]

Verified Boot protects integrity of software that is present; it does not define how long updates will be offered.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. OEM lock state / unlock policy variance residual.

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
