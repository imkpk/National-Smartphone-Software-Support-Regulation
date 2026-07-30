# Phase 5 Specification — Manufacturers & Technical Baseline

**Phase:** 5  
**Status:** In progress  
**OS:** Bound by [`REPOSITORY_OS.md`](REPOSITORY_OS.md)  
**Version note:** Phase 5 research under `0.6.x`  

---

## 1. Objectives

Document **published manufacturer software/security update lifecycle commitments** and related **technical baseline** evidence (Android platform ecosystem, hardware/chipset stack, etc.) for smartphones relevant to the India research repository.

**Descriptive only.** No recommendations, legal conclusions, or policy drafting.

---

## 2. Prerequisites

| Prerequisite | Required |
|--------------|----------|
| Phase 4 Complete | Yes (v0.6.0) |
| REPOSITORY_OS | Active |
| Latest main | Clean sync |

---

## 3. Workstream sequence

| WS | Title | Path | Status |
|----|-------|------|--------|
| 1 | Manufacturers & Technical Baseline (OEM policies) | `research/manufacturers/` | **Complete** (v0.6.1, PR #26) |
| 2 | Android Ecosystem | `research/android-ecosystem/` | **Complete** (v0.6.2, PR #27) |
| 3 | Hardware & Chipset Ecosystem | `research/hardware-ecosystem/` | **This workstream** (v0.6.3) |
| 4+ | Further technical baseline (as later specified) | TBD | Not started |

---

## 4. WS1 scope (complete)

Official manufacturer documentation for listed OEMs.

---

## 5. WS2 scope (complete)

Official Google / AOSP Android platform & update infrastructure documentation.

---

## 6. WS3 scope

Official documentation covering hardware/chipset stack enabling updates:

- Linux Kernel LTS · Android Common Kernel · GKI · KMI  
- Vendor boot · BSP / vendor software · firmware lifecycle  
- Bootloader · Secure Boot · Verified Boot · TEE  
- Qualcomm · MediaTek · Google Tensor · Samsung Exynos · UNISOC  
- Vendor security patches · kernel maintenance  

Exclude blogs, forums, Wikipedia, news, community docs as sole authority.

---

## 7. Expected WS3 outputs

- `research/hardware-ecosystem/` notes  
- Coverage / architecture / chipset / kernel lifecycle / firmware responsibility matrices  
- Source / citation / validation / cross-reference reports  
- Negative findings  
- `PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md`  
- Documentation updates  

---

## 8. Exclusions

- New Indian government research (Phase 4 closed)  
- Re-writing WS1 OEM notes or WS2 Android notes  
- Litigation / recommendations / vendor rankings  
- Multiple workstreams per PR  
- Auto-start of WS4  

---

## 9. Completion of Phase 5

Phase 5 completes only after all planned Phase 5 workstreams + audit + close (later). **WS1–WS3 alone do not close Phase 5.**

---

*Phase 5 specification — updated WS3*
