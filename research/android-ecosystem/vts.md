---
title: "Vendor Test Suite (VTS)"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Vendor Test Suite (VTS)

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

The Android Vendor Test Suite (VTS) provides extensive testing of kernel and HAL layers. Like CTS, it uses Trade Federation on a host machine and executes tests on devices/emulators. Test types include GTest HAL tests, Linux kernel tests (kselftest, LTP), some JUnit host tests, and limited Python tests.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | VTS and infrastructure | https://source.android.com/docs/core/tests/vts | 2026-07-31 |
| 2 | Architecture overview (Android-compatible path mentions VTS) | https://source.android.com/docs/core/architecture | 2026-07-31 |
| 3 | HAL overview | https://source.android.com/docs/core/architecture/hal | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Focus | Kernel and HAL validation for vendor implementations |
| Android-compatible devices | Architecture docs: CDD + VSR + VTS/CTS among requirements path |
| Character | Vendor-side test suite — supports Treble/GKI-era interfaces |

## 4. Negative findings / gaps [FACT]

VTS does not define consumer software-support duration.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Exact current VSR document URL pin residual if separate from CDD.

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
