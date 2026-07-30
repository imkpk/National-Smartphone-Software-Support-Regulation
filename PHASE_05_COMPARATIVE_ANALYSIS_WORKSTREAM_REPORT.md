# Phase 5 Workstream 4 Report — Comparative Analysis

**Date:** 2026-07-31  
**Base main:** `aaa36ab` (Phase 5 WS3 merged, v0.6.3)  
**Phase 5 status:** In progress (WS4 when this merges)  
**Version:** **0.6.4**

---

## 1. Objectives

Synthesize **existing** Phase 5 WS1–WS3 evidence into descriptive comparisons of manufacturer product policies, Android platform responsibilities, and hardware/chipset roles in software and security updates.

**Rules:** **No new research.** No rankings, compliance scoring, legislation or regulation recommendations, or legal conclusions stated as law.

## 2. Inputs (repository only)

| WS | Domain | Path | Version when completed |
|----|--------|------|------------------------|
| 1 | Manufacturers | `research/manufacturers/` | 0.6.1 (PR #26) |
| 2 | Android ecosystem | `research/android-ecosystem/` | 0.6.2 (PR #27) |
| 3 | Hardware & chipset | `research/hardware-ecosystem/` | 0.6.3 (PR #28) |

## 3. Outputs

### 3.1 Analysis notes (`research/comparative-analysis/`)

| Note | File |
|------|------|
| Comparison overview | `comparison-overview.md` |
| Manufacturer vs Google roles | `manufacturer-vs-google.md` |
| Android vs chipset | `android-vs-chipset.md` |
| Software update flow | `software-update-flow.md` |
| Security update flow | `security-update-flow.md` |
| Lifecycle comparison | `lifecycle-comparison.md` |
| Consolidated responsibility matrix (narrative) | `responsibility-matrix.md` |
| Negative finding (cross-layer) | `negative-finding-comparative-no-single-unified-support-floor.md` |
| Domain index | `README.md` |

### 3.2 Matrices

| Matrix | File |
|--------|------|
| Manufacturer comparison | `COMPARATIVE_MANUFACTURER_MATRIX.md` |
| Android responsibility | `COMPARATIVE_ANDROID_RESPONSIBILITY_MATRIX.md` |
| Chipset responsibility | `COMPARATIVE_CHIPSET_RESPONSIBILITY_MATRIX.md` |
| Software update flow | `COMPARATIVE_SOFTWARE_UPDATE_FLOW_MATRIX.md` |
| Security update | `COMPARATIVE_SECURITY_UPDATE_MATRIX.md` |
| OS update | `COMPARATIVE_OS_UPDATE_MATRIX.md` |
| Platform dependency | `COMPARATIVE_PLATFORM_DEPENDENCY_MATRIX.md` |
| Lifecycle comparison | `COMPARATIVE_LIFECYCLE_MATRIX.md` |
| Evidence cross-reference | `COMPARATIVE_EVIDENCE_CROSS_REFERENCE_MATRIX.md` |
| Terminology | `COMPARATIVE_TERMINOLOGY_MATRIX.md` |
| Coverage | `COMPARATIVE_COVERAGE_MATRIX.md` |

### 3.3 Reports

| Report | File |
|--------|------|
| Source | `COMPARATIVE_SOURCE_REPORT.md` |
| Citation | `COMPARATIVE_CITATION_REPORT.md` |
| Validation | `COMPARATIVE_VALIDATION_REPORT.md` |
| Consistency | `COMPARATIVE_CONSISTENCY_REPORT.md` |
| Cross-reference | `COMPARATIVE_CROSS_REFERENCE_REPORT.md` |
| Gate++ | `orchestration/PHASE_05_WS4_GATE_REPORT.md` |

## 4. Key synthesis findings

| Finding | Basis |
|---------|--------|
| **Capability ≠ commitment** | WS2/WS3 architecture describes *how* updates are enabled; WS1 product policies state *how long* OEMs publicly promise support (where published) |
| **Publication ≠ device receipt** | WS2 ASB and WS3 SoC fixes may be published without every device receiving them |
| **Multi-path updates, partial modular coverage** | WS2 Mainline / Play System Updates; WS2/WS3 GKI/KMI — partial surfaces only |
| **Heterogeneous public documentation** | WS1 OEM residual OPEN; WS3 SoC public matrices uneven |
| **Google dual role** | Platform steward (WS2/WS3) and Pixel OEM (WS1); product multi-year windows remain private policies, not Indian law |
| **No single unified multi-year floor across layers** | All three workstream negative findings + comparative negative finding |

## 5. Negative finding (this workstream)

Repository evidence from WS1–WS3, read together, does **not** establish:

1. One industry-wide multi-year OS/security floor for all manufacturers  
2. One platform-doc multi-year device floor in AOSP/Google documentation  
3. One public multi-year chipset/firmware consumer floor for all SoCs  
4. One single clock that equates product support years, ASB cadence, and ACK/GKI EOL  

**What is present:** partial OEM multi-year statements; ACK/GKI branch EOL tables; modular update paths.

## 6. Validation / Gate++

| Check | Result |
|-------|--------|
| No new research | **PASS** |
| Traceability to WS1–WS3 | **PASS** |
| Repository Relevance on notes/matrices/reports | **PASS** |
| No rankings / recommendations / legal conclusions as law | **PASS** |
| Documentation + indexes update | **PASS** (this PR) |
| Gate++ | **PASS** — `orchestration/PHASE_05_WS4_GATE_REPORT.md` |

## 7. Explicitly not done

- New external research or unofficial sources  
- Manufacturer rankings or compliance evaluations  
- Legislation / regulation recommendations or policy advocacy  
- Predictions of future OEM behaviour  
- Phase 5 **not** complete  
- **WS5 not started**  

## 8. Next

Further Phase 5 work only after this PR is reviewed, approved, merged into `main`, and further work is authorised. **Do not auto-start Workstream 5.**

---

*Phase 5 Workstream 4 — Comparative Analysis — v0.6.4*
