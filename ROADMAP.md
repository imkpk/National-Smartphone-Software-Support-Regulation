# Roadmap

**Project:** National-Smartphone-Software-Support-Regulation  
**Horizon:** Phase 0 → Phase 10  
**Principle:** No litigation drafting before research validation gates pass.

---

## Phase 0 — Repository Foundation

**Objective:** Create the institutional skeleton of the project.

**Includes**

- Root governance documents  
- Full directory tree  
- Multi-agent architecture definition  
- Task inventory (300+)  
- Validation constitution  
- Contribution and conduct policies  

**Excludes**

- Legal research  
- Judgment digests  
- PIL drafting  

**Exit criteria**

- [x] All Phase 0 files present  
- [x] Empty research/evidence/litigation trees with `.gitkeep`  
- [x] `git init` + initial commit  
- [x] Remote GitHub repository created and linked  

**Status:** Complete

---

## Phase 1 — Research Infrastructure

**Objective:** Make research repeatable and machine-checkable.

**Workstreams**

1. Templates for statute notes, judgment briefs, OEM captures, policy memos  
2. YAML/JSON schemas for citations and sources  
3. Folder README indexes under each `research/*` domain  
4. Validation checklists and script stubs  
5. Logging conventions under `logs/`  
6. Issue templates and PR template in `.github/`  
7. Master orchestration prompt ready for supervised Phase 2+ runs  
8. Supporting governance: citation policy, legal strategy (forum open), research guidelines  

**Exit criteria**

- [x] Templates usable without tribal knowledge  
- [x] `scripts/check_structure.py` (or equivalent) passes  
- [x] Contribution path documented with examples  
- [x] Domain indexes under `research/*`  
- [x] Validation gate checklists present  
- [x] Agent prompt stubs under `prompts/agents/`  

**Depends on:** Phase 0  
**Status:** Complete (framework only — no substantive legal research)  

---

## Phase 2 — Constitutional & Statutory Map (India)

**Objective:** Authoritative map of binding Indian law potentially engaged by software support regulation.

**Domains**

- Constitution (Arts. relevant to equality, speech, life/privacy, environment, writs, DPSPs/duties)  
- Consumer Protection Act framework  
- IT Act / CERT-In related instruments  
- Environment (Protection) Act & E-Waste Rules  
- BIS Act / standards pathway  
- Legal Metrology  
- Other discovered central instruments  

**Exit criteria**

- Each provision has section-level notes + official source  
- Coverage matrix published in `research/`  
- Open questions list for legislative gaps  

**Depends on:** Phase 1  
**Rule:** No analysis without citation  

---

## Phase 3 — Judgments Corpus

**Objective:** Curated, verified case law relevant to PIL maintainability, Art. 21 expansions, environment principles, consumer welfare, digital rights, administrative law.

**Workstreams**

- Supreme Court core set  
- High Court persuasive set  
- Doctrine index (precaution, polluter pays, locus, mandamus, privacy, etc.)  
- Pin-cite verification protocol  

**Exit criteria**

- Every case entry has official citation  
- Ratio vs application clearly separated  
- `UNVERIFIED` items quarantined  

**Depends on:** Phase 2 (parallelisation allowed with caution)  

---

## Phase 4 — Government Policy & Institutions

**Objective:** Map executive instruments and institutional mandates.

**Coverage**

- Digital India / DPI context  
- National cybersecurity policy instruments  
- MeitY, DoT, Consumer Affairs, MoEFCC, CPCB, BIS, CERT-In roles  
- Electronics manufacturing / PLI interfaces  
- Grievance and RTI pathways  

**Exit criteria**

- Institutional RACI-style matrix  
- Policy inventory with official links  
- Documented gaps (absence of software support mandate recorded as finding, not assumption)  

**Depends on:** Phase 1  

---

## Phase 5 — Manufacturers & Technical Baseline

**Objective:** Evidence-grade OEM policy dossier + technical lifecycle literacy.

**Workstreams**

- Google, Samsung, Apple, Nothing, Motorola, OnePlus, Xiaomi, POCO, realme, vivo, Oppo, Honor, Sony, Nokia/HMD, ASUS, others as needed  
- OS vs security update distinction  
- Capture date protocol  
- Technical note: Android/iOS update pipelines (descriptive, not reverse engineering)  

**Exit criteria**

- Comparison tables in `evidence/tables/`  
- Per-OEM folders with sources  
- Uncertainty log for SKU-level variance  

**Depends on:** Phase 1  

---

## Phase 6 — Cybersecurity, Environment, Economics

**Objective:** Multidisciplinary evidence packs.

**Workstreams**

- CVE / patch lifecycle / unsupported device risk pathways  
- Global and Indian e-waste data (primary preferred)  
- Consumer loss / replacement / externalities models (labelled estimates)  
- Consumer-law economic interface  

**Exit criteria**

- Three research packs with source lists  
- No unsourced statistics in `VERIFIED` sections  

**Depends on:** Phase 1; benefits from Phase 4–5  

---

## Phase 7 — Comparative International Law

**Objective:** Persuasive comparative materials.

**Coverage**

- European Union Ecodesign / energy labelling for smartphones  
- France repairability / durability indexes  
- UK, US, Japan, South Korea, Australia, Singapore, Germany, others as relevant  
- Right-to-repair landscape mapped to software support  

**Exit criteria**

- Jurisdiction comparison matrix  
- Clear label: **not binding on India**  
- Primary instrument citations  

**Depends on:** Phase 1  

---

## Phase 8 — Evidence Pack & Annexure Factory

**Objective:** Court-annexure-ready artefacts.

**Workstreams**

- Timelines, charts, tables  
- Annexure index templates  
- Evidence chain-of-custody notes  
- Export scripts to DOCX/PDF  

**Exit criteria**

- `evidence/` populated with versioned artefacts  
- Mapping from research claims → annexure IDs  

**Depends on:** Phases 2–7  

---

## Phase 9 — Litigation Drafting

**Objective:** Produce PIL package drafts under dual control of Drafting Agent + Citation Validation Agent.

**Artefacts**

- Synopsis  
- List of dates  
- Writ petition structure  
- Affidavit  
- Prayers (interim/final)  
- Annexure plan  

**Exit criteria**

- All VALIDATION.md litigation gates green  
- Banner removed only after human counsel certification  
- Research Director + QA sign-off  

**Depends on:** Phase 8  
**Hard gate:** No Phase 9 start without PM written approval in CHANGELOG or issue  

---

## Phase 10 — Validation, Automation & Public Hardening

**Objective:** Productionise the repository for continuous quality and public use.

**Workstreams**

- CI structure checks  
- Citation lint (heuristic)  
- MASTER_PROMPT operationalisation  
- Release tagging (v1.0 research corpus)  
- Security review of scripts  
- Community onboarding docs  

**Exit criteria**

- Tagged release  
- Green CI on `main`  
- Public contribution surge plan  

**Depends on:** Phase 9 optional for research-only v1.0; full litigation v1.1 may follow  

---

## Cross-Cutting Workstreams (All Phases)

| Stream | Owner (see AGENTS.md) |
|--------|------------------------|
| Citation integrity | Citation Validation Agent |
| Task hygiene | Project Manager |
| Architecture | Chief Architect |
| Git hygiene | Git Manager |
| Quality gates | Quality Assurance Agent |

---

## Milestone Summary

| Milestone | Target artefact | Phase |
|-----------|-----------------|-------|
| M0 | Foundation docs live | 0 |
| M1 | Templates + validators stub | 1 |
| M2 | India law map v0.9 | 2–4 |
| M3 | Evidence tables v1 | 5–8 |
| M4 | Comparative matrix v1 | 7 |
| M5 | PIL draft v0.1 | 9 |
| M6 | Public research release v1.0 | 10 |

---

## Deliberate Non-Commitments

This roadmap does **not** commit to:

- Filing dates in any court  
- Specific regulatory outcomes (e.g., “India will adopt 5-year OS rule”)  
- Funding or institutional partnerships  

---

*Update this file when phases complete or scope changes. Sync TASKS.md accordingly.*
