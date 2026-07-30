---
title: "Generic Kernel Image (GKI)"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Research Note — Generic Kernel Image (GKI)

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

The GKI project addresses kernel fragmentation by unifying the core kernel and moving SoC/board support into loadable vendor modules with a stable Kernel Module Interface (KMI). Beginning Android 12, devices shipping with kernel 5.10+ must ship with the GKI kernel. GKI kernels are built from Android Common Kernel (ACK) sources.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | Generic Kernel Image (GKI) project | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | 2026-07-31 |
| 2 | Android common kernels (ACK) | https://source.android.com/docs/core/architecture/kernel/android-common | 2026-07-31 |
| 3 | Kernel architecture overview | https://source.android.com/docs/core/architecture/kernel | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Problem addressed | Pre-GKI custom kernels with large out-of-tree code hindered security backport and LTS merges |
| Design | Single GKI binary per architecture/LTS + vendor modules; stable KMI |
| Requirement | Android 12+ devices with kernel 5.10+ ship GKI |
| Goals | Partners deliver kernel security fixes without full vendor rebuild; reduce major kernel uprev cost |
| ACK support lifetimes | Official ACK table lists multi-year EOL dates per branch (e.g. 4–6 year support lifetimes depending on branch) |
| Character | Kernel architecture & common-kernel support windows — distinct from OEM product support marketing |

## 4. Negative findings / gaps [FACT]

GKI/ACK support lifetimes describe common kernel branch maintenance by Google/community processes — they are not automatic consumer device OS-upgrade promises for every OEM SKU.

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Which India-volume models actually ship pure GKI vs exceptions — device capture residual.

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
