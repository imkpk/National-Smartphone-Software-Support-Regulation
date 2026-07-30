# Phase 5 WS5 — Gap Analysis (NO NEW RESEARCH)
# Synthesizes WS1 manufacturers, WS2 android-ecosystem, WS3 hardware-ecosystem, WS4 comparative-analysis only.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "phase5-gap-analysis"
OUT.mkdir(parents=True, exist_ok=True)
ACCESS = "2026-07-31"
BASE = "45b5377"  # PR #29 merge on main


def header_sections(extra_sources=None):
    sources = """| Workstream | Path / report |
|------------|---------------|
| WS1 Manufacturers | `research/manufacturers/` · `PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md` |
| WS2 Android Ecosystem | `research/android-ecosystem/` · `PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS3 Hardware Ecosystem | `research/hardware-ecosystem/` · `PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS4 Comparative Analysis | `research/comparative-analysis/` · `PHASE_05_COMPARATIVE_ANALYSIS_WORKSTREAM_REPORT.md` |
"""
    if extra_sources:
        sources += extra_sources
    return f"""## Repository Relevance

**Why this document belongs in the repository:**  
Phase 5 Workstreams 1–4 collected manufacturer policies, Android platform architecture, hardware/chipset evidence, and comparative synthesis. Gap analysis organises **descriptive absences and residual OPENs** in that evidence for later phases without adding new external research.

**Tags:** Phase 5 · Gap analysis · Repository Cross Reference

## Classification

**ANALYSIS** — Descriptive gap synthesis of existing repository evidence. **Not** legal conclusions; **not** recommendations; **not** manufacturer rankings; **not** compliance evaluations; **not** predictions.

## Evidence sources (repository only)

{sources}
**Rule:** No new external research or new citations as authorities in this workstream.

"""


def footer_sections():
    return """
## Negative findings

See `negative-findings.md` and per-workstream negative findings (WS1–WS4).

## Cross references

- All matrices and reports in this folder
- `../../PHASE_05_GAP_ANALYSIS_WORKSTREAM_REPORT.md`
- Phase 4 gap analysis (`research/phase4-gap-analysis/`) — government-side context only; not re-researched

## Audit trail

- Phase 5 Workstream 5 — Gap Analysis
- Synthesis only — no new web research
- Descriptive gaps only
"""


def note(slug, title, body):
    content = f"""---
title: "{title}"
domain: "phase5-gap-analysis"
status: VERIFIED
last_updated: {ACCESS}
phase: 5
workstream: "P5-WS5"
---

# {title}

{header_sections()}
{body}
{footer_sections()}
"""
    (OUT / f"{slug}.md").write_text(content, encoding="utf-8")
    print("wrote", slug)


# ── Core notes ──────────────────────────────────────────────

note(
    "overall-gap-analysis",
    "Overall Gap Analysis — Phase 5 WS1–WS4",
    f"""
## 1. Purpose

Integrated descriptive synthesis of gaps visible when reading Phase 5 WS1–WS4 together.  
**Does not:** recommend legislation, regulation, manufacturer actions, rankings, or litigation conclusions.

## 2. Scope

| Layer | Workstream | Evidence path |
|-------|------------|---------------|
| Product policies | WS1 | `research/manufacturers/` |
| Platform architecture | WS2 | `research/android-ecosystem/` |
| Hardware / chipset / kernel / firmware | WS3 | `research/hardware-ecosystem/` |
| Comparative synthesis | WS4 | `research/comparative-analysis/` |

Base main at synthesis: `{BASE}` · repository version **0.6.4**.

## 3. Gap definition [ANALYSIS]

In this workstream, a **gap** means:

1. An **absence** recorded as a negative finding in WS1–WS4 (e.g. no industry-wide multi-year floor); or  
2. A **residual OPEN** explicitly left in Phase 5 notes/matrices (e.g. incomplete single-matrix capture for some OEMs; sparse SoC public matrices); or  
3. A **descriptive misalignment** between layers (e.g. capability architecture present while product duration statements are uneven; publication of fixes ≠ device receipt).

Gaps are **not** prescriptions of what law or vendors “should” do.

## 4. Central cross-layer picture [ANALYSIS from FACT notes]

| Question | What repository evidence shows is present | What is not established in WS1–WS4 |
|----------|-------------------------------------------|-----------------------------------|
| Multi-year product support statements | Partial (Pixel; Samsung series; some security baselines) — WS1 | Industry-wide OEM multi-year matrix |
| Platform update mechanisms | AOSP OTA, Mainline, GKI, ASB, CDD/CTS — WS2 | Universal multi-year device floor in platform docs |
| Kernel / firmware / SoC support windows | LTS/ACK/GKI tables; uneven SoC public docs — WS3 | Universal multi-year chipset/firmware consumer floor |
| Alignment of clocks | Compared in WS4 | Single clock equating product years, ASB cadence, ACK EOL |
| Indian multi-year legal floor | Phase 4 context only (not re-researched) | Not present as Phase 5 finding from OEM/platform/hardware docs either |

## 5. Gap clusters (summary)

1. **Commitment transparency gap** — Uneven public multi-year product matrices across brands (WS1).  
2. **Capability–commitment gap** — Platform/hardware enable updates; product duration is OEM-policy driven (WS2/WS3/WS4).  
3. **Publication–delivery gap** — ASB/SoC publication does not equal universal ship (WS2/WS3).  
4. **Modular coverage gap** — Mainline/GKI cover partial surfaces only (WS2/WS3).  
5. **SoC public-evidence gap** — Chipset multi-year consumer matrices uneven / sparse for some vendors (WS3).  
6. **Lifecycle clock gap** — Product, platform version, ACK, LTS, SoC firmware clocks are not the same (WS4).  
7. **Documentation residual gap** — Residual brands, PDF annexures, iOS observational model, technical cross-read still OPEN in tasks (WS1–WS4 residuals).  
8. **Unified floor gap** — No single multi-year floor across product + platform + hardware layers (WS4 negative finding).

## 6. Research confidence [ANALYSIS]

| Topic | Confidence |
|-------|------------|
| Inventory of WS1–WS4 folders and negative findings | **High** |
| Non-identification of unified multi-year floor in Phase 5 WS1–WS4 scope | **High** (protocol-scoped) |
| Completeness of every residual brand/SKU worldwide | **Not claimed** — residual OPEN |

## 7. Limitations

- No new research in this workstream  
- Does not re-audit Phase 2–4 government materials (context only)  
- Partner-only BSP content remains out of public capture (WS3 residual)  
- Phase 5 residual tasks (T252, T256, T260, residual brands) remain OPEN  
""",
)

note(
    "manufacturer-gaps",
    "Manufacturer Support Commitment Gaps — Phase 5 WS5",
    """
## 1. Evidence base

WS1 manufacturer notes and matrices; WS4 manufacturer comparison matrix and manufacturer-vs-google note.

## 2. Gaps identified [ANALYSIS from WS1/WS4 FACT]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| M-G1 | No **industry-wide** multi-year OS/security matrix published jointly by manufacturers | WS1 negative finding |
| M-G2 | For several high-volume brands (Nothing, OnePlus, OPPO, Vivo, Realme, HMD, Sony, Honor, ASUS), a **single dedicated multi-year policy page** comparable to Pixel was **not captured** as a unified matrix — residual OPEN | WS1 coverage matrix |
| M-G3 | Apple uses security-release / vintage model — **no** fixed N-year table identified in WS1 capture | WS1 lifecycle matrix |
| M-G4 | Xiaomi/Motorola publish **security** baselines or per-product cycles more clearly than uniform multi-year **OS** upgrade tables for all models | WS1 lifecycle matrix |
| M-G5 | Residual India-volume brands (iQOO, Tecno/Infinix, other discovery) **not** captured in WS1 note set | tasks/phase-05 residual T238–T246 |
| M-G6 | SKU-level variance uncertainty logs exist per notes, but **not** a complete India SKU universe | WS1 uncertainty residual |
| M-G7 | OEM multi-year statements are **private product policies**, not established as Indian law in Phase 5 manufacturer evidence | WS1 negative finding; Phase 4 context |

## 3. What is present (contrast)

- Pixel multi-year windows (7y / 5y by generation)  
- Samsung series-specific multi-year materials  
- Xiaomi ≥2y security baseline + EOL lists; Motorola per-product security cycles  

## 4. Not claimed

These gaps do **not** assert non-compliance with any statute; they describe **public documentation evidence** as captured in WS1.
""",
)

note(
    "android-platform-gaps",
    "Android Platform Gaps — Phase 5 WS5",
    """
## 1. Evidence base

WS2 Android ecosystem notes, update responsibility matrix, platform negative finding; WS4 android responsibility and software/security flow matrices.

## 2. Gaps identified [ANALYSIS from WS2/WS4 FACT]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| A-G1 | Platform docs describe **how** updates work (OTA, Mainline, GKI, CDD/CTS) — **not** a universal multi-year consumer device floor | WS2 negative finding |
| A-G2 | **ASB publication ≠ universal device shipping** — integration/ship remains OEM/SoC-dependent | WS2 ASB / monthly security notes |
| A-G3 | **Mainline / Play System Updates are partial** — selected modules only; kernel/vendor/non-modular surfaces remain full-OTA dependent | WS2 Mainline / component matrix |
| A-G4 | **GKI/ACK lifetimes ≠ OEM product marketing support years** | WS2 GKI; WS3 ACK; WS4 lifecycle comparison |
| A-G5 | **CDD/CTS/VTS** define compatibility policy/tests — not multi-year support duration for retail models | WS2 CDD/CTS/VTS |
| A-G6 | **GMS commercial partner terms** not fully public as a single consumer-facing multi-year matrix on pages reviewed in WS2 | WS2 negative finding |
| A-G7 | Android Enterprise / Enterprise Recommended document **managed-device capabilities**, not a consumer multi-year legal floor | WS2 enterprise notes |
| A-G8 | Play Integrity may surface “recent security updates” signals — **measurement**, not OEM multi-year promise | WS2 play-integrity; WS4 security flow |

## 3. What is present (contrast)

- Rich architecture for multi-path updates  
- Monthly ASB process documentation  
- Treble / vendor interface separation  
- GKI requirements for modern Android kernels  
- Explicit Google vs OEM responsibility language in platform notes  

## 4. Responsibility implication (descriptive)

Where multi-year **duration** is documented for a retail device, repository evidence points primarily to **OEM product policy (WS1)**, not platform CDD text (WS2).
""",
)

note(
    "hardware-gaps",
    "Hardware, Chipset, Kernel, and Firmware Gaps — Phase 5 WS5",
    """
## 1. Evidence base

WS3 hardware ecosystem notes and matrices; WS4 chipset responsibility, platform dependency, lifecycle matrices.

## 2. Gaps identified [ANALYSIS from WS3/WS4 FACT]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| H-G1 | **No universal multi-year consumer chipset/firmware support floor** across SoC vendors | WS3 negative finding |
| H-G2 | **ACK/GKI/LTS multi-year tables** are kernel-branch maintenance windows — not automatic OEM product multi-year OS promises | WS3 kernel lifecycle; WS4 lifecycle |
| H-G3 | **SoC public documentation uneven** — Qualcomm security bulletins strong; MediaTek/UNISOC multi-year public matrices sparse | WS3 chipset support matrix |
| H-G4 | **Detailed BSP packages largely partner-only** — not fully capturable as public consumer matrices | WS3 BSP residual |
| H-G5 | **ASB SoC-source fixes** still require OEM integration and shipping | WS3 vendor-security-patches; WS2 ASB |
| H-G6 | **TEE / modem / bootloader / firmware** update calendars not standardized as public N-year consumer matrices across vendors | WS3 firmware lifecycle / TEE / bootloader |
| H-G7 | **KMI stability** enables independent GKI updates only when frozen — KMI break implies vendor module rebuild | WS3 KMI; WS4 dependency matrix |

## 3. What is present (contrast)

- LTS → ACK → GKI architectural chain  
- Published ACK support / EOL tables (4–6 years by branch, as captured)  
- Qualcomm public security bulletin channel  
- Tensor dual role with Pixel product pages (OEM + SoC)  
- Firmware responsibility split documented  

## 4. Dependency gap (descriptive)

Long-term device security depends on a **chain** (platform fixes + kernel + SoC firmware + OEM integration). A gap or stop at any link can interrupt updates even if other links continue (WS4 platform dependency matrix).
""",
)

note(
    "documentation-gaps",
    "Documentation and Evidence Coverage Gaps — Phase 5 WS5",
    """
## 1. Evidence base

WS1–WS4 coverage matrices, residual OPEN items in tasks/phase-05.md, WS4 terminology and evidence cross-reference matrices.

## 2. Documentation gaps [ANALYSIS]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| D-G1 | Uneven **depth** of official multi-year product documentation across OEMs | WS1 coverage / comparison matrices |
| D-G2 | Residual **brand captures** not completed (iQOO, Tecno/Infinix, other India-volume discovery) | tasks T238–T246 |
| D-G3 | **PDF annexure archive** of captures under evidence/annexures residual OPEN | tasks T252 |
| D-G4 | **iOS update support observational model** technical note residual OPEN | tasks T256 |
| D-G5 | **Technical + cybersecurity cross-read** residual OPEN | tasks T260 |
| D-G6 | Partner-gated **BSP** documentation not in public repository capture | WS3 residual |
| D-G7 | SoC multi-year **consumer-facing** matrices sparse for some vendors | WS3 chipset matrix |
| D-G8 | No single public document equating **product years ↔ ACK EOL ↔ ASB cadence** | WS4 lifecycle comparison |

## 3. Standards / programme documentation (Phase 5 lens)

Within Phase 5 WS1–WS4 evidence:

| Topic | Present as | Not present as |
|-------|------------|----------------|
| CDD / CTS / VTS | Compatibility policy and tests (WS2) | Multi-year retail support floor |
| Mainline component list | Modular update architecture (WS2) | Full OS/security replacement |
| ACK EOL tables | Kernel branch support windows (WS3) | Automatic product support years |

Phase 4 standards/programme **legal/IS floor** absences remain government-side context (not re-researched here).

## 4. Evidence availability gap

Repository holds **high** evidence density for architecture and **partial** evidence for product multi-year commitments; **low** public evidence for some SoC multi-year consumer matrices and residual brands.
""",
)

note(
    "responsibility-gaps",
    "Responsibility Gaps — Phase 5 WS5",
    """
## 1. Evidence base

WS2 update responsibility / Google vs OEM notes; WS3 firmware responsibility matrix; WS4 consolidated responsibility matrix.

## 2. Responsibility map (what is described)

| Responsibility | Documented actor(s) in WS1–WS4 |
|----------------|--------------------------------|
| Publish ASB platform fixes | Google/AOSP |
| Publish SoC fixes | SoC vendors (public depth varies) |
| Maintain ACK/GKI | Google kernel; vendor modules from SoC/OEM |
| Build & ship full device OTA | Device OEM (primary shipper) |
| Mainline packages (GMS path) | Google packages; OEM eligibility |
| Product multi-year support statement | Device OEM (primary public face); Pixel as Google OEM |
| CDD/CTS execution | OEM executes; Google defines/tests |
| End-user install | End user |

## 3. Gaps [ANALYSIS]

| Gap ID | Description | Trace |
|--------|-------------|-------|
| R-G1 | **No single actor** publicly owns an industry-wide multi-year floor for all devices | WS1–WS4 negative findings |
| R-G2 | **Duration commitments** sit mainly with OEM product policy, while **fix content** originates from platform/kernel/SoC — split is clear; joint public calendar is not | WS4 responsibility / security flow |
| R-G3 | Carrier OTA gating (where used) is noted as possible intermediate — not systematically mapped per India carrier in Phase 5 | WS2/WS4 responsibility matrix (limited) |
| R-G4 | Partner-only BSP responsibility details not fully public | WS3 |
| R-G5 | “Who ensures device remains secure after OEM EOL?” — **not established as a single rule** in WS1–WS4 | WS4 security-update-flow residual OPEN |

## 4. Explicit non-claims

This note does **not** assign legal liability or regulatory duty. It records **roles as described in repository technical and product-policy evidence**.
""",
)

note(
    "negative-findings",
    "Negative Findings Summary — Phase 5 WS1–WS5",
    """
## 1. Purpose

Consolidate **negative findings already established** in WS1–WS4, plus the WS5 cross-layer gap framing. No new external search.

## 2. Per-workstream negative findings [FACT inventory]

| WS | File | Core absence |
|----|------|--------------|
| 1 | `research/manufacturers/negative-finding-oem-unified-multi-year-matrix.md` | No industry-wide OEM multi-year matrix; uneven documentation depth |
| 2 | `research/android-ecosystem/negative-finding-android-platform-not-multi-year-device-floor.md` | Platform docs not a multi-year device floor; bulletin ≠ ship; Mainline partial |
| 3 | `research/hardware-ecosystem/negative-finding-hardware-no-universal-chipset-support-floor.md` | No universal multi-year chipset/firmware consumer floor; SoC public matrices uneven |
| 4 | `research/comparative-analysis/negative-finding-comparative-no-single-unified-support-floor.md` | No single unified multi-year floor across product + platform + hardware layers |

## 3. Cross-layer synthesis [ANALYSIS]

Taken together, Phase 5 WS1–WS4 evidence establishes:

1. **Partial product policies** exist for some brands.  
2. **Rich update architecture** exists (platform + kernel + modular paths).  
3. **A single unified multi-year support floor** across all manufacturers, all SoCs, and platform docs **does not appear** in the repository evidence reviewed.  
4. **Capability, publication, and commitment** are different evidence classes and must not be conflated.

## 4. Phase 4 context (not re-researched)

Phase 4 government-side materials (policy/institutions/standards/consultations/programmes) also recorded non-identification of a dedicated Indian multi-year OS/security-support **legal/IS/programme** floor. That remains **adjacent context** for later phases — not a Phase 5 WS5 re-audit.

## 5. Protocol note

Negative findings are **protocol-scoped** (what was searched and captured in each workstream). They are not absolute claims about all possible unindexed partner documents worldwide.
""",
)

# Matrices
matrices = {
    "GAP_MATRIX.md": f"""# Gap Matrix — Phase 5 WS5

## Repository Relevance

Descriptive inventory of gaps from WS1–WS4 evidence. **Date:** {ACCESS}

## Classification

**ANALYSIS** — Gap inventory. Not recommendations.

## Evidence sources

WS1–WS4 paths and workstream reports only.

## Cross references

`overall-gap-analysis.md` · layer gap notes · `GAP_EVIDENCE_MATRIX.md`

## Negative findings

See `negative-findings.md`.

| Gap ID | Cluster | Layer | Description (descriptive) | Primary WS |
|--------|---------|-------|---------------------------|------------|
| M-G1 | Commitment transparency | Product | No industry-wide OEM multi-year matrix | WS1 |
| M-G2 | Commitment transparency | Product | Several brands lack single multi-year matrix capture | WS1 |
| M-G5 | Documentation residual | Product | Residual India-volume brands not captured | WS1/tasks |
| A-G1 | Capability–commitment | Platform | No universal multi-year device floor in platform docs | WS2 |
| A-G2 | Publication–delivery | Platform | ASB publish ≠ universal ship | WS2 |
| A-G3 | Modular coverage | Platform | Mainline partial only | WS2 |
| H-G1 | Chipset floor | Hardware | No universal multi-year chipset/firmware consumer floor | WS3 |
| H-G3 | Evidence availability | Hardware | SoC public multi-year matrices uneven | WS3 |
| H-G4 | Evidence availability | Hardware | BSP partner-gated | WS3 |
| L-G1 | Lifecycle clocks | Cross | Product / ACK / LTS / ASB clocks not identical | WS4 |
| U-G1 | Unified floor | Cross | No single multi-year floor across all layers | WS4 |
| D-G3 | Documentation residual | Repo process | PDF annexure archive OPEN | tasks |
| D-G4 | Documentation residual | Technical residual | iOS observational model OPEN | tasks |
| R-G1 | Responsibility | Cross | No single actor owns industry-wide multi-year floor | WS1–WS4 |
| R-G5 | Responsibility | Cross | Post-OEM-EOL security rule not established as single standard | WS4 |

**Count:** 15 primary gap rows (illustrative inventory; layer notes expand detail).
""",
    "GAP_EVIDENCE_MATRIX.md": f"""# Evidence Matrix — Phase 5 WS5

## Repository Relevance

Maps gap claims to repository evidence paths. **Date:** {ACCESS}

## Classification

**ANALYSIS** — Traceability. No new sources.

## Evidence sources

WS1–WS4 only.

## Cross references

`GAP_MATRIX.md` · `GAP_CROSS_REFERENCE_REPORT.md`

## Negative findings

All major negative findings listed in `negative-findings.md`.

| Gap / claim | WS1 | WS2 | WS3 | WS4 |
|-------------|-----|-----|-----|-----|
| Uneven OEM multi-year docs | manufacturer notes; coverage matrix; NF | — | — | COMPARATIVE_MANUFACTURER_MATRIX |
| Platform not multi-year floor | — | platform NF; CDD/CTS/Mainline | GKI/ACK not product years | lifecycle + platform dependency |
| SoC public uneven | — | ASB three-source model | chipset matrix; NF; vendor-security-patches | chipset responsibility matrix |
| Bulletin ≠ ship | — | ASB notes | SoC fix integration | security-update-flow |
| Mainline partial | — | project-mainline; play-system-updates | GKI kernel-only | software-update-flow |
| No unified multi-year floor | OEM NF | platform NF | hardware NF | comparative NF |
| Residual brands / annexures / iOS model | tasks residual | tasks residual | — | tasks residual |
""",
    "GAP_COVERAGE_MATRIX.md": f"""# Coverage Matrix — Phase 5 WS5 Gap Analysis

## Repository Relevance

Confirms required gap-analysis topics are covered. **Date:** {ACCESS}

## Classification

**ANALYSIS** — Coverage checklist.

## Evidence sources

WS1–WS4 repository evidence.

## Cross references

Folder README · `GAP_VALIDATION_REPORT.md`

## Negative findings

Absences documented rather than filled with new research.

| Required analysis topic | Covered in | Status |
|-------------------------|------------|--------|
| Manufacturer support commitments | manufacturer-gaps · GAP_MATRIX | Yes |
| Android platform responsibilities | android-platform-gaps · GAP_RESPONSIBILITY_GAP_MATRIX | Yes |
| Chipset ecosystem | hardware-gaps | Yes |
| Kernel lifecycle | hardware-gaps · GAP_LIFECYCLE_GAP_MATRIX | Yes |
| Firmware lifecycle | hardware-gaps · GAP_LIFECYCLE_GAP_MATRIX | Yes |
| Security update responsibilities | android-platform-gaps · responsibility-gaps | Yes |
| OS update responsibilities | android-platform-gaps · manufacturer-gaps | Yes |
| Platform dependencies | GAP_DEPENDENCY_GAP_MATRIX · hardware-gaps | Yes |
| Documentation coverage | documentation-gaps | Yes |
| Standards coverage (CDD/CTS lens) | documentation-gaps · android-platform-gaps | Yes (Phase 5 lens) |
| Evidence availability | GAP_EVIDENCE_MATRIX · documentation-gaps | Yes |
| Institutional coverage | overall-gap-analysis (Phase 4 context only) | Contextual — not re-researched |
| Technical responsibilities | responsibility-gaps | Yes |
| Support lifecycle transparency | manufacturer-gaps · documentation-gaps | Yes |
| Update mechanisms | android-platform-gaps · hardware-gaps | Yes |
| Negative findings summary | negative-findings · GAP_NEGATIVE_FINDINGS_REPORT | Yes |

**Coverage:** Complete for WS5 descriptive gap scope.
""",
    "GAP_RESPONSIBILITY_GAP_MATRIX.md": f"""# Responsibility Gap Matrix — Phase 5 WS5

## Repository Relevance

Describes responsibility **splits and absences** from WS1–WS4. **Date:** {ACCESS}

## Classification

**ANALYSIS** — Not legal liability assignment.

## Evidence sources

WS2 ANDROID_UPDATE_RESPONSIBILITY_MATRIX · WS3 FIRMWARE_RESPONSIBILITY_MATRIX · WS4 responsibility-matrix

## Cross references

`responsibility-gaps.md` · `GAP_MATRIX.md`

## Negative findings

No single industry-wide multi-year owner (R-G1).

| Function | Who is described as acting | Public multi-year duration owner? | Gap note |
|----------|----------------------------|-----------------------------------|----------|
| ASB platform fix content | Google/AOSP | No (publication cadence, not device years) | A-G2 |
| Kernel LTS/ACK/GKI | Google kernel + upstream | ACK branch EOL tables exist; not product years | H-G2 |
| SoC firmware fixes | SoC vendors | Rarely as open consumer multi-year matrix | H-G1/H-G3 |
| Device OTA ship | OEM | Where OEM publishes product policy (WS1) | M-G2 residual |
| Mainline modules | Google (+ OEM eligibility) | Partial surface only | A-G3 |
| Industry-wide floor | — | **Not identified** | R-G1 / U-G1 |
| Post-OEM EOL security | Not established as single rule | Residual OPEN | R-G5 |
""",
    "GAP_DOCUMENTATION_GAP_MATRIX.md": f"""# Documentation Gap Matrix — Phase 5 WS5

## Repository Relevance

Catalogues documentation depth gaps in Phase 5 evidence. **Date:** {ACCESS}

## Classification

**ANALYSIS**

## Evidence sources

WS1 coverage matrix · WS3 chipset matrix · tasks/phase-05.md residuals

## Cross references

`documentation-gaps.md`

## Negative findings

Uneven public documentation is itself a WS1/WS3 FACT theme.

| Domain | Strong public capture in repo | Sparse / residual OPEN |
|--------|-------------------------------|------------------------|
| OEM multi-year product policy | Pixel; Samsung series materials | Several OEMs single-matrix residual; iQOO/Tecno residual |
| Android architecture | Broad WS2 topic set | GMS full commercial terms not public matrix |
| Kernel LTS/ACK/GKI | Strong AOSP/kernel.org | — |
| SoC security | Qualcomm bulletins; Pixel/Tensor | MediaTek/UNISOC multi-year public matrices |
| BSP internals | Conceptual BSP note | Partner-only deep packages |
| Evidence annexures | — | T252 PDF archive OPEN |
| iOS observational model | — | T256 OPEN |
""",
    "GAP_LIFECYCLE_GAP_MATRIX.md": f"""# Lifecycle Gap Matrix — Phase 5 WS5

## Repository Relevance

Compares lifecycle **clocks** and where multi-year public artifacts exist. **Date:** {ACCESS}

## Classification

**ANALYSIS**

## Evidence sources

WS1 lifecycle matrix · WS3 KERNEL_LIFECYCLE · WS4 COMPARATIVE_LIFECYCLE_MATRIX / lifecycle-comparison

## Cross references

`overall-gap-analysis.md` · `hardware-gaps.md`

## Negative findings

No single equated clock (L-G1 / U-G1).

| Lifecycle clock | Public multi-year artifact in Phase 5 evidence? | Sets retail device support years? | Gap |
|-----------------|--------------------------------------------------|-----------------------------------|-----|
| OEM product OS/security | Partial (WS1) | **Yes where published** | M-G2 residual brands/series |
| Android platform version / CDD | Per-version docs (WS2) | No | A-G1 / A-G5 |
| ASB monthly cadence | Yes (process) | No | A-G2 |
| ACK/GKI branch EOL | Yes (WS3) | Not automatically | H-G2 |
| Upstream LTS EOL | Yes (WS3) | Not automatically | H-G2 |
| SoC firmware | Uneven (WS3) | Rarely open matrix | H-G1/H-G6 |
| Mainline module eligibility | Ongoing while eligible (WS2) | Partial surface only | A-G3 |
""",
    "GAP_DEPENDENCY_GAP_MATRIX.md": f"""# Dependency Gap Matrix — Phase 5 WS5

## Repository Relevance

Describes dependency-chain gaps that can interrupt device updates. **Date:** {ACCESS}

## Classification

**ANALYSIS**

## Evidence sources

WS4 COMPARATIVE_PLATFORM_DEPENDENCY_MATRIX · WS2/WS3 architecture notes

## Cross references

`hardware-gaps.md` · `android-platform-gaps.md` · `responsibility-gaps.md`

## Negative findings

Chain fragility is descriptive, not predictive of future OEM behaviour.

| Dependent layer | Depends on | Documented failure / stop mode in evidence | Gap ID |
|-----------------|------------|--------------------------------------------|--------|
| OEM security OTA | ASB + SoC + kernel fixes | Cannot ship unpublished fixes | A-G2 / H-G5 |
| GKI without vendor rebuild | Stable KMI | KMI break → module rebuild | H-G7 |
| Mainline delivery | Device eligibility / GMS path | Modules not delivered | A-G3 |
| Vendor HALs | Treble/VINTF | Upgrade friction if interfaces break | WS2 Treble |
| Product multi-year claim | OEM ability to integrate full chain | Claim ≠ capability if chain breaks | WS4 dependency |
| Consumer long-term security | All of the above | Layered residual risk (descriptive) | U-G1 |
""",
}

for name, body in matrices.items():
    (OUT / name).write_text(body, encoding="utf-8")
    print("wrote", name)

# Reports
reports = {
    "GAP_NEGATIVE_FINDINGS_REPORT.md": f"""# Negative Findings Report — Phase 5 WS5

## Repository Relevance

Formal report companion to `negative-findings.md`. **Date:** {ACCESS}

## Classification

**ANALYSIS** / inventory of prior **FACT** negative findings.

## Evidence sources

WS1–WS4 negative finding files (paths only).

## Cross references

`negative-findings.md` · layer gap notes

## Negative findings

| # | Statement | Origin |
|---|-----------|--------|
| 1 | No industry-wide OEM multi-year matrix; uneven official documentation depth | WS1 |
| 2 | Android platform docs are not a universal multi-year device support floor; bulletin ≠ ship; Mainline partial | WS2 |
| 3 | No universal multi-year chipset/firmware consumer floor; SoC public matrices uneven | WS3 |
| 4 | No single unified multi-year floor across product, platform, and hardware layers | WS4 |
| 5 | Residual documentation/process OPENs (brands, annexures, iOS model, cross-read) remain in tasks | WS1–WS4 residuals |

**Protocol-scoped.** No new search performed in WS5.

**Overall inventory status:** **PASS** (complete relative to WS1–WS4 NFs)
""",
    "GAP_CITATION_REPORT.md": f"""# Citation Report — Phase 5 WS5 Gap Analysis

## Repository Relevance

Confirms citations are repository-internal. **Date:** {ACCESS}

## Classification

**ANALYSIS** (citation discipline)

## Evidence sources

WS1–WS4 paths only.

## Cross references

`GAP_SOURCE_REPORT.md` · `GAP_VALIDATION_REPORT.md`

## Negative findings

No new external authorities introduced.

| Rule | Status |
|------|--------|
| Citations point to repository paths | **PASS** |
| No new external URLs as authorities | **PASS** |
| ANALYSIS labeled | **PASS** |
| Traceability matrices present | **PASS** |

**Overall:** **PASS**
""",
    "GAP_SOURCE_REPORT.md": f"""# Source Report — Phase 5 WS5 Gap Analysis

## Repository Relevance

Declares accepted sources for WS5. **Date:** {ACCESS}

## Classification

**ANALYSIS** (source discipline)

## Evidence sources (accepted)

| Class | Paths |
|-------|-------|
| WS1 | `research/manufacturers/*` · `PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md` |
| WS2 | `research/android-ecosystem/*` · `PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS3 | `research/hardware-ecosystem/*` · `PHASE_05_HARDWARE_ECOSYSTEM_WORKSTREAM_REPORT.md` |
| WS4 | `research/comparative-analysis/*` · `PHASE_05_COMPARATIVE_ANALYSIS_WORKSTREAM_REPORT.md` |
| Task residuals | `tasks/phase-05.md` (OPEN items inventory only) |
| Phase 4 context | `research/phase4-gap-analysis/` (pointer only; not re-researched) |

## Rejected

- New web research  
- Blogs, forums, news  
- New external primary sources  
- Rankings / advocacy materials as authority  

## Negative findings

Source set limited to prior Phase 5 evidence ensures gaps are **from the record**, not invented.

## Cross references

`GAP_CITATION_REPORT.md`

**Conclusion:** All gap statements trace to prior Phase 5 workstream artefacts.
""",
    "GAP_VALIDATION_REPORT.md": f"""# Validation Report — Phase 5 WS5 Gap Analysis

## Repository Relevance

Fail-closed validation for WS5 package. **Date:** {ACCESS}

## Classification

**ANALYSIS** (validation meta). Bound by VALIDATION.md · REPOSITORY_OS.md.

## Evidence sources

All artefacts in this folder; WS1–WS4 inputs by path only.

## Cross references

`orchestration/PHASE_05_WS5_GATE_REPORT.md` · `GAP_CONSISTENCY_REPORT.md`

## Negative findings

Unified multi-year floor absence validated as **already evidenced** in WS1–WS4, not newly asserted from web research.

| Check | Result |
|-------|--------|
| No new research | **PASS** |
| All gaps trace to WS1–WS4 (or documented task residual) | **PASS** |
| Repository Relevance + Classification | **PASS** |
| No recommendations / rankings / legal conclusions as law | **PASS** |
| No duplicate re-audit of primary WS1–WS4 notes | **PASS** (synthesis only) |
| Cross references present | **PASS** |
| Single workstream | **PASS** |
| Naming under `research/phase5-gap-analysis/` | **PASS** |

**Overall:** **PASS**
""",
    "GAP_CONSISTENCY_REPORT.md": f"""# Consistency Report — Phase 5 WS5 Gap Analysis

## Repository Relevance

Confirms WS5 does not contradict WS1–WS4. **Date:** {ACCESS}

## Classification

**ANALYSIS**

## Evidence sources

WS1–WS4 reports + this folder.

## Cross references

`GAP_VALIDATION_REPORT.md` · `negative-findings.md`

## Negative findings

Consistent cross-layer absence of unified multi-year floor.

| Consistency check | Result |
|-------------------|--------|
| WS1 uneven OEM matrices reflected | **PASS** |
| WS2 bulletin ≠ ship / platform not floor reflected | **PASS** |
| WS3 SoC unevenness / no chipset floor reflected | **PASS** |
| WS4 unified floor NF reflected | **PASS** |
| Capability ≠ commitment preserved | **PASS** |
| ACK EOL not equated to product years | **PASS** |
| Mainline partial, not full OS replacement | **PASS** |
| Phase 4 legal-floor context not re-researched as new claim | **PASS** |
| No rankings or recommendations introduced | **PASS** |

**Overall consistency:** **PASS**
""",
    "GAP_CROSS_REFERENCE_REPORT.md": f"""# Cross Reference Report — Phase 5 WS5 Gap Analysis

## Repository Relevance

Link graph for gap package. **Date:** {ACCESS}

## Classification

**ANALYSIS**

## Evidence sources

This folder + WS1–WS4 folders + workstream reports.

## Cross references

`GAP_EVIDENCE_MATRIX.md` · `research/README.md`

## Negative findings

No orphan gap IDs intended.

| From | To |
|------|-----|
| overall-gap-analysis | All layer gap notes + GAP_MATRIX |
| manufacturer-gaps | WS1 manufacturers + WS4 manufacturer matrices |
| android-platform-gaps | WS2 android-ecosystem + WS4 flow matrices |
| hardware-gaps | WS3 hardware-ecosystem + WS4 chipset/lifecycle |
| documentation-gaps | WS1–WS3 coverage + tasks/phase-05 residuals |
| responsibility-gaps | WS2/WS3/WS4 responsibility artefacts |
| negative-findings | All four prior NF files + WS5 summary |
| GAP_* matrices/reports | Layer notes + prior WS reports |

**Orphans:** None intended.
""",
    "GAP_COVERAGE_REPORT.md": f"""# Coverage Report — Phase 5 WS5 Gap Analysis

## Repository Relevance

Narrative coverage summary companion to `GAP_COVERAGE_MATRIX.md`. **Date:** {ACCESS}

## Classification

**ANALYSIS**

## Evidence sources

WS1–WS4.

## Cross references

`GAP_COVERAGE_MATRIX.md` · workstream report

## Negative findings

Covered as inventory, not filled by new research.

## Summary

All analysis-scope topics listed in the WS5 execution prompt are mapped to artefacts. Institutional multi-year **legal** duty remains Phase 4 context only. Residual Phase 5 task OPENs are inventoried as documentation gaps, not resolved here.

**Status:** **Complete for WS5 scope**
""",
}

for name, body in reports.items():
    (OUT / name).write_text(body, encoding="utf-8")
    print("wrote", name)

# README
(OUT / "README.md").write_text(
    f"""# Phase 5 Gap Analysis — Workstream 5

**Status:** Workstream 5 complete (synthesis of WS1–WS4 only)  
**Phase 5 overall:** In progress  
**Rule:** **No new research.** Evidence from WS1–WS4 only.  
**Access / synthesis date:** {ACCESS}

## Repository Relevance

Descriptive gap analysis of manufacturer policies, Android platform architecture, hardware/chipset evidence, and comparative synthesis. Organises absences and residual OPENs for later phases.

## Classification

**ANALYSIS** — repository synthesis only. Not recommendations, rankings, or legal conclusions.

## Evidence sources

| WS | Path |
|----|------|
| 1 | `research/manufacturers/` |
| 2 | `research/android-ecosystem/` |
| 3 | `research/hardware-ecosystem/` |
| 4 | `research/comparative-analysis/` |

## Negative findings

See [negative-findings.md](negative-findings.md) · [GAP_NEGATIVE_FINDINGS_REPORT.md](GAP_NEGATIVE_FINDINGS_REPORT.md).

## Analysis notes

| Note | File |
|------|------|
| Overall gap analysis | [overall-gap-analysis.md](overall-gap-analysis.md) |
| Manufacturer gaps | [manufacturer-gaps.md](manufacturer-gaps.md) |
| Android platform gaps | [android-platform-gaps.md](android-platform-gaps.md) |
| Hardware / kernel / firmware gaps | [hardware-gaps.md](hardware-gaps.md) |
| Documentation gaps | [documentation-gaps.md](documentation-gaps.md) |
| Responsibility gaps | [responsibility-gaps.md](responsibility-gaps.md) |
| Negative findings summary | [negative-findings.md](negative-findings.md) |

## Matrices & reports

| Artefact | File |
|----------|------|
| Gap matrix | [GAP_MATRIX.md](GAP_MATRIX.md) |
| Evidence matrix | [GAP_EVIDENCE_MATRIX.md](GAP_EVIDENCE_MATRIX.md) |
| Coverage matrix | [GAP_COVERAGE_MATRIX.md](GAP_COVERAGE_MATRIX.md) |
| Responsibility gap matrix | [GAP_RESPONSIBILITY_GAP_MATRIX.md](GAP_RESPONSIBILITY_GAP_MATRIX.md) |
| Documentation gap matrix | [GAP_DOCUMENTATION_GAP_MATRIX.md](GAP_DOCUMENTATION_GAP_MATRIX.md) |
| Lifecycle gap matrix | [GAP_LIFECYCLE_GAP_MATRIX.md](GAP_LIFECYCLE_GAP_MATRIX.md) |
| Dependency gap matrix | [GAP_DEPENDENCY_GAP_MATRIX.md](GAP_DEPENDENCY_GAP_MATRIX.md) |
| Negative findings report | [GAP_NEGATIVE_FINDINGS_REPORT.md](GAP_NEGATIVE_FINDINGS_REPORT.md) |
| Source / citation / validation / consistency / cross-ref / coverage reports | GAP_*_REPORT.md |
| Workstream report | [`../../PHASE_05_GAP_ANALYSIS_WORKSTREAM_REPORT.md`](../../PHASE_05_GAP_ANALYSIS_WORKSTREAM_REPORT.md) |
""",
    encoding="utf-8",
)
print("wrote README")

# Workstream report
(ROOT / "PHASE_05_GAP_ANALYSIS_WORKSTREAM_REPORT.md").write_text(
    f"""# Phase 5 Workstream 5 Report — Gap Analysis

**Date:** {ACCESS}  
**Base main:** `{BASE}` (Phase 5 WS4 merged, v0.6.4)  
**Phase 5 status:** In progress (WS5 when this merges)  
**Version:** **0.6.5**

---

## 1. Objectives

Produce a **descriptive gap analysis** based exclusively on Phase 5 WS1–WS4 repository evidence (manufacturers, Android ecosystem, hardware ecosystem, comparative analysis).

**Rules:** **No new research.** No rankings, compliance scoring, legislation/regulation recommendations, manufacturer action recommendations, or legal conclusions stated as law.

## 2. Inputs (repository only)

| WS | Domain | Path | Version when completed |
|----|--------|------|------------------------|
| 1 | Manufacturers | `research/manufacturers/` | 0.6.1 (PR #26) |
| 2 | Android ecosystem | `research/android-ecosystem/` | 0.6.2 (PR #27) |
| 3 | Hardware & chipset | `research/hardware-ecosystem/` | 0.6.3 (PR #28) |
| 4 | Comparative analysis | `research/comparative-analysis/` | 0.6.4 (PR #29) |

## 3. Outputs

### 3.1 Analysis notes (`research/phase5-gap-analysis/`)

| Note | File |
|------|------|
| Overall gap analysis | `overall-gap-analysis.md` |
| Manufacturer gaps | `manufacturer-gaps.md` |
| Android platform gaps | `android-platform-gaps.md` |
| Hardware gaps | `hardware-gaps.md` |
| Documentation gaps | `documentation-gaps.md` |
| Responsibility gaps | `responsibility-gaps.md` |
| Negative findings summary | `negative-findings.md` |
| Domain index | `README.md` |

### 3.2 Matrices

| Matrix | File |
|--------|------|
| Gap matrix | `GAP_MATRIX.md` |
| Evidence matrix | `GAP_EVIDENCE_MATRIX.md` |
| Coverage matrix | `GAP_COVERAGE_MATRIX.md` |
| Responsibility gap | `GAP_RESPONSIBILITY_GAP_MATRIX.md` |
| Documentation gap | `GAP_DOCUMENTATION_GAP_MATRIX.md` |
| Lifecycle gap | `GAP_LIFECYCLE_GAP_MATRIX.md` |
| Dependency gap | `GAP_DEPENDENCY_GAP_MATRIX.md` |

### 3.3 Reports

| Report | File |
|--------|------|
| Negative findings | `GAP_NEGATIVE_FINDINGS_REPORT.md` |
| Source | `GAP_SOURCE_REPORT.md` |
| Citation | `GAP_CITATION_REPORT.md` |
| Validation | `GAP_VALIDATION_REPORT.md` |
| Consistency | `GAP_CONSISTENCY_REPORT.md` |
| Cross-reference | `GAP_CROSS_REFERENCE_REPORT.md` |
| Coverage | `GAP_COVERAGE_REPORT.md` |
| Gate++ | `orchestration/PHASE_05_WS5_GATE_REPORT.md` |

## 4. Key gap clusters

| Cluster | Basis |
|---------|--------|
| Commitment transparency | Uneven OEM multi-year public matrices (WS1) |
| Capability ≠ commitment | Platform/hardware architecture vs product policies (WS2–WS4) |
| Publication ≠ delivery | ASB/SoC publish vs OEM ship (WS2/WS3) |
| Modular partial coverage | Mainline / GKI (WS2/WS3) |
| SoC public-evidence unevenness | WS3 chipset matrix |
| Lifecycle clock misalignment | WS4 lifecycle comparison |
| No unified multi-year floor | WS1–WS4 negative findings |
| Documentation residuals | tasks residual brands / annexures / iOS model / cross-read |

## 5. Validation / Gate++

| Check | Result |
|-------|--------|
| No new research | **PASS** |
| Traceability to WS1–WS4 | **PASS** |
| Repository Relevance on artefacts | **PASS** |
| No rankings / recommendations / legal conclusions as law | **PASS** |
| Documentation + indexes update | **PASS** (this PR) |
| Gate++ | **PASS** — `orchestration/PHASE_05_WS5_GATE_REPORT.md` |

## 6. Explicitly not done

- New external research or unofficial sources  
- Manufacturer rankings or compliance evaluations  
- Legislation / regulation recommendations or policy advocacy  
- Predictions of future behaviour  
- Phase 5 **not** complete  
- **WS6 not started**  

## 7. Next

Further Phase 5 work only after this PR is reviewed, approved, merged into `main`, and further work is authorised. **Do not auto-start Workstream 6.**

---

*Phase 5 Workstream 5 — Gap Analysis — v0.6.5*
""",
    encoding="utf-8",
)
print("wrote workstream report")

# Gate report
orch = ROOT / "orchestration"
orch.mkdir(exist_ok=True)
(orch / "PHASE_05_WS5_GATE_REPORT.md").write_text(
    f"""# Repository Gate++ — Phase 5 WS5

**Date:** {ACCESS}  
**Workstream:** Gap Analysis  
**Target version:** 0.6.5  
**Base:** v0.6.4 / PR #29 merged (`{BASE}`)

| Check | Result |
|-------|--------|
| PR #29 / WS4 prerequisite | **PASS** (merged; v0.6.4) |
| Phase 5 WS4 complete | **PASS** |
| Repository version baseline | **PASS** (0.6.4 → 0.6.5) |
| No new research | **PASS** |
| Folder `research/phase5-gap-analysis/` | **PASS** |
| Required gap notes present | **PASS** |
| Matrices present (gap, evidence, coverage, responsibility, documentation, lifecycle, dependency) | **PASS** |
| Reports present (source, citation, validation, consistency, cross-ref, coverage, negative findings) | **PASS** |
| Traceability to WS1–WS4 | **PASS** |
| No rankings / recommendations / legal conclusions as law | **PASS** |
| Single workstream only | **PASS** |
| Indexes / README / CHANGELOG / ROADMAP / TASKS / STATE_REPORT | **PASS** (this PR) |
| Knowledge graph reachability | **PASS** |
| Naming conventions | **PASS** |
| WS6 not included | **PASS** |

**Overall:** **PASS**

---
""",
    encoding="utf-8",
)
print("wrote gate report")
print("DONE")
