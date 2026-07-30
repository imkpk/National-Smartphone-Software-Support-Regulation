---
title: "Gap analysis — Regulatory authorities layer"
domain: "gap-analysis"
status: VERIFIED
last_updated: 2026-07-30
phase: 3
workstream: "GAP-6"
---

# Gap Analysis — Regulatory Authorities Layer

## 1. Scope

Synthesise `research/regulators/` (MeitY, DoT, CERT-In, CCPA, BIS, CPCB). No new regulator research.

## 2. Repository evidence reviewed

| Artefact | Role |
|----------|------|
| `meity.md`, `dot.md`, `cert-in.md`, `ccpa.md`, `bis.md`, `cpcb.md` | Authority notes |
| `REGULATOR_COVERAGE_MATRIX.md` | Mandate matrix |
| `negative-finding-regulatory-software-support-duty.md` | Negative finding |
| Source / citation / validation reports | Quality trail |

## 3. Findings [FACT / ANALYSIS]

### Coverage [FACT]

Six priority authorities documented with mandate, publications orientation, relevance, limitations, and official sources.

### What the repository establishes [FACT]

From regulator coverage matrix and negative finding:

| Authority | Binding multi-year OS/security-year mandate found? | Primary interface (repository) |
|-----------|----------------------------------------------------|--------------------------------|
| MeitY | **No** | IT/electronics policy; Digital India; standards interface |
| DoT | **No** | Telecom policy; device-as-terminal |
| CERT-In | **No** | Cyber incident response; patching culture |
| CCPA | **No** | UTP / misleading ads / class protection |
| BIS | **No** | Indian Standards + QCO pathway |
| CPCB | **No** | E-waste EPR / end-of-life |

**Requirements identified** (real regimes): cyber incident directions, consumer market conduct, standards/QCO pathways, e-waste EPR, telecom policy — **not** multi-year OS floors (`negative-finding-regulatory-software-support-duty.md`).

## 4. Negative findings [FACT]

| Question | Repository answer |
|----------|-------------------|
| Official multi-year smartphone OS/security-support duty from the six authorities | **Not identified** |
| Exhaustive historical Gazette of every niche notification | Residual OPEN (TEC/NCCS, unpublished drafts) |

## 5. Limitations

- Public portal review ≠ full Gazette history.  
- CERT-In Directions full PDF paragraph pins flagged SECONDARY until annexed.  
- meity.md/dot.md were empty post-PR #10; restored PR #11 — content now present.  
- Guidelines ≠ statute (especially CCPA).  

## 6. Research confidence

**High** for non-identification on public official materials reviewed for the six authorities.  
**Moderate** for residual niche notifications / RTI file notings.  
**High** for institutional interface mapping (which body owns which pathway).

## 7. Open questions [OPEN]

1. RTI to MeitY/BIS/DoT on software-support standards file notings.  
2. TEC/NCCS equipment standards deeper pass.  
3. Any CCPA order/guideline mentioning software-update duration.  
4. BIS draft IS search residual.
