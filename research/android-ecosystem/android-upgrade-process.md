---
title: "Android Upgrade / OTA Process"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Android Upgrade / OTA Process

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

Android devices can receive OTA updates to the system, read-only system apps, and time zone rules. Official OTA docs describe Virtual A/B (seamless) updates (Android 11+), legacy A/B, and deprecation of non-A/B as of Android 15. OTAs do not update user-installed Play apps (those update via Play).

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | OTA updates | https://source.android.com/docs/core/ota | 2026-07-31 |
| 2 | Virtual A/B seamless updates | https://source.android.com/docs/core/ota/virtual_ab | 2026-07-31 |
| 3 | A/B system updates | https://source.android.com/docs/core/ota/ab | 2026-07-31 |
| 4 | Time zone rules updates | https://source.android.com/docs/core/permissions/timezone-rules | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Package scope | OS, system partition apps, time zone rules — not user Play apps |
| Virtual A/B | Two logical slots; compressed snapshots for large dynamic partitions |
| Non-A/B | Deprecated as of Android 15 |
| TZ updates | From Android 8.1, TZ rules can update without full system image |
| Character | Technical update delivery architecture for implementers |

## 4. Negative findings / gaps [FACT]

OTA mechanisms enable updates; they do not specify minimum years of support for commercial devices.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Carrier vs OEM OTA channel differences in India — residual.

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
