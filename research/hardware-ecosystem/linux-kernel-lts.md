---
title: "Linux Kernel Long-Term Support (LTS)"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Research Note — Linux Kernel Long-Term Support (LTS)

## Repository Relevance

**Why this topic belongs in the repository:**  
Chipset, kernel, firmware, and boot-chain architecture determine **what can be updated** and **who must supply patches** for Android devices. This is foundational technical evidence for software-support longevity research in India — **not** Indian law and **not** OEM multi-year product promises (see Phase 5 WS1).

**Tags:** Hardware ecosystem · Kernel · Firmware · Chipset · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official technical documentation (AOSP, kernel.org, vendor security/docs where public). Descriptive only. **Not** legal conclusions; **not** recommendations; **not** vendor rankings.

## 1. Topic summary [FACT]

Upstream Linux Longterm (LTS) kernels are maintained for multi-year periods with important bugfixes backported. kernel.org publishes active longterm versions, maintainers, release dates, and projected EOL. Android Common Kernels are downstream of these LTS kernels.

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
| 1 | kernel.org — Active kernel releases / Longterm | https://www.kernel.org/releases.html | 2026-07-31 |
| 2 | kernel.org releases category | https://www.kernel.org/category/releases.html | 2026-07-31 |
| 3 | AOSP Kernel overview (LTS → ACK) | https://source.android.com/docs/core/architecture/kernel | 2026-07-31 |
| 4 | AOSP — Long Term Stable Kernels | https://source.android.com/docs/core/architecture/kernel/releases | 2026-07-31 |

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
| Categories | Prepatch/RC · Mainline · Stable · Longterm |
| Cadence | Mainline ~every 9–10 weeks; stable updates as-needed (~weekly) |
| Longterm purpose | Backport important bugfixes for older trees |
| Example LTS set (kernel.org table) | e.g. 6.18, 6.12, 6.6, 6.1, 5.15, 5.10 with projected EOL dates |
| EOL note | Projected EOL not fixed in stone; may extend with industry support |
| Android link | Each Android Common Kernel is based on an upstream LTS |
| Character | Upstream kernel maintenance model — not OEM product support years |

## 4. Negative findings / gaps [FACT]

kernel.org LTS lifetimes describe **kernel tree** maintenance, not commercial smartphone multi-year OS commitments. Distribution kernels may differ and are unsupported by kernel.org maintainers.

## 5. Limitations

- Public chipset documentation depth varies widely; partner BSP details are often non-public.
- Platform architecture docs do not guarantee device-level support duration.
- Not Indian law.

## 6. Open questions [OPEN]

1. Exact mapping of every India-volume device kernel to a specific LTS branch requires per-device capture.

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
