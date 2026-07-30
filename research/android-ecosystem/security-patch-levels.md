---
title: "Security Patch Levels"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Security Patch Levels

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

Android Security Bulletins associate published fixes with security patch level dates (commonly YYYY-MM-01 and YYYY-MM-05 style strings). Devices report a security patch level reflecting the set of fixes incorporated when the OEM builds and ships an update.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Android Security Bulletins (patch levels in tables) | https://source.android.com/docs/security/bulletin/asb-overview | 2026-07-31 |
| 2 | Bulletins monthly index | https://source.android.com/docs/security/bulletin | 2026-07-31 |
| 3 | Play Integrity — strong integrity / recent security updates (Android 13+) | https://developer.android.com/google/play/integrity/overview | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Identifier | Date-based security patch level string associated with bulletin contents |
| Device display | Consumer devices expose patch level in system settings (implementation via platform) |
| Integrity signal | Play Integrity optional MEETS_STRONG_INTEGRITY (Android 13+) relates to recent security updates among other signals |
| Character | Technical versioning of security fix bundles — not multi-year legal support floor |

## 4. Negative findings / gaps [FACT]

A high security patch level on a device indicates incorporated bulletin content for that build; it does not alone prove ongoing multi-year commitment.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Exact mapping rules OEM uses when shipping partial vendor vs platform components.

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
