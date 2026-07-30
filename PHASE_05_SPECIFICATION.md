# Phase 5 Specification — Manufacturers & Technical Baseline

**Phase:** 5  
**Status:** In progress  
**OS:** Bound by [`REPOSITORY_OS.md`](REPOSITORY_OS.md)  
**Version note:** Phase 5 research under `0.6.x`  

---

## 1. Objectives

Document **published manufacturer software/security update lifecycle commitments** and related **technical baseline** evidence (Android platform ecosystem, etc.) for smartphones relevant to the India research repository.

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
| 2 | Android Ecosystem | `research/android-ecosystem/` | **This workstream** (v0.6.2) |
| 3+ | Further technical baseline (as later specified) | TBD | Not started |

---

## 4. WS1 scope (complete)

Official manufacturer documentation for listed OEMs (Google · Samsung · Apple · Nothing · Motorola · OnePlus · Xiaomi · OPPO · Vivo · Realme · HMD/Nokia · Sony · Honor · ASUS · Lenovo).

---

## 5. WS2 scope

Official **Google / AOSP** Android documentation only:

- AOSP architecture  
- Android Enterprise / Enterprise Recommended  
- Project Mainline · Play System Updates  
- Security Bulletins · monthly cadence · security patch levels  
- CDD · CTS · VTS · GMS  
- Treble · GKI · vendor interface  
- OTA / upgrade process · release cycle · update distribution  
- Update responsibilities · Google vs OEM roles  
- Verified Boot · rollback protection · Play Integrity  

Exclude blogs, forums, news, Wikipedia, community docs as sole authority.

---

## 6. Expected WS2 outputs

- `research/android-ecosystem/` notes  
- Coverage / architecture / responsibility / component matrices  
- Source / citation / validation / cross-reference reports  
- Negative findings  
- `PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md`  
- Documentation updates  

---

## 7. Exclusions

- New Indian government research (Phase 4 closed)  
- Re-writing OEM notes (WS1 closed)  
- Litigation / recommendations  
- Multiple workstreams per PR  
- Auto-start of WS3  

---

## 8. Completion of Phase 5

Phase 5 completes only after all planned Phase 5 workstreams + audit + close (later). **WS1 + WS2 alone do not close Phase 5.**

---

*Phase 5 specification — updated WS2*
