---
title: "Google vs OEM Responsibilities (updates)"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Google vs OEM Responsibilities (updates)

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

Complementing the update-responsibilities map: Google publishes Android platform security fixes and modular updates; OEMs decide product-line support duration and ship device-specific builds. Pixel devices have Google-published support-duration pages (WS1). Third-party OEMs publish their own policies.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Security bulletins | https://source.android.com/docs/security/bulletin/asb-overview | 2026-07-31 |
| 2 | Mainline | https://source.android.com/docs/core/architecture/modular-system | 2026-07-31 |
| 3 | Pixel software updates (OEM example — Google as OEM) | https://support.google.com/pixelphone/answer/4457705 | 2026-07-31 |
| 4 | Architecture overview | https://source.android.com/docs/core/architecture | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Google as platform steward | AOSP, bulletins, Mainline, GKI/ACK, compatibility program |
| Google as Pixel OEM | Publishes multi-year Pixel update commitments (WS1) |
| Other OEMs | Integrate platform; ship OTAs; publish own lifecycle policies (WS1) |
| Shared security surface | Kernel/vendor/firmware require OEM/SoC action beyond pure framework Mainline modules |
| Character | Descriptive split — not liability conclusions |

## 4. Negative findings / gaps [FACT]

Neither Google platform documentation nor OEM marketing pages constitute Indian legislation mandating multi-year support industry-wide.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Whether any public GMS MoU clauses on security updates exist outside partner portals.

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
