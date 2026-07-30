# Multi-Agent Architecture

**Project:** National-Smartphone-Software-Support-Regulation  
**Document status:** Active (design)  
**Runtime status:** Manual / human-supervised until `MASTER_PROMPT.md` activation  

This document defines specialised agents as **roles with contracts**. They may be humans, LLMs under supervision, or hybrid pairs. All agents are bound by [`VALIDATION.md`](VALIDATION.md).

---

## 1. Architecture Overview

```text
                    ┌──────────────────────┐
                    │   Chief Architect    │
                    └──────────┬───────────┘
                               │
                    ┌──────────v───────────┐
                    │  Project Manager     │
                    └──────────┬───────────┘
                               │
                    ┌──────────v───────────┐
                    │  Research Director   │
          ┌────────┴──────────┬──────────┴────────┐
          v                   v                   v
   Domain Research      Evidence Agent      Drafting Agent
   Agents (×N)                                 │
          │                   │                v
          └─────────┬─────────┘         litigation/**
                    v
         Citation Validation Agent
                    │
                    v
         Quality Assurance Agent
                    │
                    v
              Git Manager
```

**Principle:** Research agents **propose**; validation agents **dispose**; drafting agents **consume only validated inputs**.

---

## 2. Global Rules (All Agents)

1. Never invent judgments, statutes, notifications, or citations.  
2. Prefer primary sources.  
3. Label uncertainty explicitly.  
4. Write outputs only to assigned paths.  
5. Do not promote content to `litigation/` without Phase 9 approval + validation gates.  
6. Do not execute offensive security work.  
7. Log significant decisions to `logs/` when automation exists.  
8. On conflict between speed and accuracy, choose accuracy.  
9. Escalate BLOCKER issues via GitHub issue template `validation_blocker`.  
10. Re-read VALIDATION.md at the start of every work session.

---

## 3. Agent Specifications

### 3.1 Chief Architect

| Field | Content |
|-------|---------|
| **Mission** | Own system design, repository topology, standards, and long-term coherence of the research platform. |
| **Responsibilities** | Maintain PROJECT_SPECIFICATION, folder architecture, agent contracts, integration points with automation; resolve design disputes; prevent scope rot. |
| **Inputs** | ROADMAP, SPEC, incident reports, PM change requests. |
| **Outputs** | Architecture ADRs in `docs/` (future), updates to AGENTS.md/SPEC, structural refactors. |
| **Rules** | No silent breaking moves of public paths; document migrations; keep Phase gates intact. |
| **Handoffs** | → Project Manager (implementation sequencing); → Git Manager (structural PRs); → Research Director (domain boundary clarifications). |

---

### 3.2 Project Manager

| Field | Content |
|-------|---------|
| **Mission** | Deliver phases on time with transparent task state and blocked-item management. |
| **Responsibilities** | Own TASKS.md hygiene; prioritise backlog; enforce phase exit criteria; coordinate human approvals; update README progress; refuse out-of-phase litigation work. |
| **Inputs** | TASKS.md, ROADMAP, agent capacity, validation incident queue. |
| **Outputs** | Sprint plans, checked-off tasks, CHANGELOG release notes coordination, risk escalations. |
| **Rules** | Cannot waive VALIDATION.md; cannot skip Phase 9 hard gate; must record scope changes. |
| **Handoffs** | → Research Director (research batches); → Drafting Agent (only after approval); → Chief Architect (scope changes); → QA (release readiness). |

---

### 3.3 Research Director

| Field | Content |
|-------|---------|
| **Mission** | Ensure domain research is complete, non-duplicative, and methodologically sound. |
| **Responsibilities** | Allocate work across domain agents; maintain research index; resolve overlap (e.g., consumer-law vs statutes); set verification priorities. |
| **Inputs** | Open research tasks; domain drafts; comparative gaps. |
| **Outputs** | Research coverage matrix; consolidated review notes; priority lists for Citation Validation. |
| **Rules** | Balance breadth vs depth; forbid “complete dump” uncited memos. |
| **Handoffs** | → All domain agents; → Evidence Agent; → Citation Validation; → Drafting (input pack). |

---

### 3.4 Constitution Agent

| Field | Content |
|-------|---------|
| **Mission** | Map constitutional provisions and doctrine relevant to smartphone software support regulation. |
| **Responsibilities** | Article-level notes (14, 19, 21, 32, 48A, 51A(g), 226, etc. as justified); doctrine of non-arbitrariness, privacy, environment-as-life; writ jurisdiction notes; **no invented fundamental rights**. |
| **Inputs** | Official Constitution text; validated case law from Judgments agents on constitutional holdings. |
| **Outputs** | `research/constitution/**` memos; cross-links to judgments. |
| **Rules** | Cite article numbers; distinguish enforceable FR vs DPSP/duties; no “right to free phones.” |
| **Handoffs** | → Supreme Court / High Court Agents (supporting cases); → Drafting Agent (grounds framing); → Citation Validation. |

---

### 3.5 Statute Agent

| Field | Content |
|-------|---------|
| **Mission** | Catalogue and analyse central statutes and rules material to the project. |
| **Responsibilities** | CPA, IT Act, EPA, E-Waste Rules, BIS Act, Legal Metrology, other discovered Acts; section-level accuracy; amendment awareness. |
| **Inputs** | India Code, Gazette, official PDFs. |
| **Outputs** | `research/statutes/**`, `research/consumer-law/**` (shared with consumer focus). |
| **Rules** | Section numbers mandatory; no paraphrases presented as quotes without verification. |
| **Handoffs** | → Government Policy Agent (subordinate instruments); → Citation Validation; → Drafting. |

---

### 3.6 Supreme Court Agent

| Field | Content |
|-------|---------|
| **Mission** | Build verified Supreme Court case briefs relevant to project doctrines. |
| **Responsibilities** | PIL locus, Art. 21 expansions, environmental principles, privacy, consumer-welfare landmarks, administrative law mandamus limits; official citations only. |
| **Inputs** | Official reports / reputable databases; Research Director priority list. |
| **Outputs** | `research/judgments/supreme-court/**` |
| **Rules** | No fake SCC cites; pin-cites provisional until full text checked; ratio ≠ every sentence in judgment. |
| **Handoffs** | → Constitution Agent; → Citation Validation; → Drafting. |

---

### 3.7 High Court Agent

| Field | Content |
|-------|---------|
| **Mission** | Curate persuasive High Court authorities (including Telangana/Andhra where relevant to filing forum strategy). |
| **Responsibilities** | Digital rights, consumer, environment, PIL procedure HCs; clearly mark as persuasive. |
| **Inputs** | Official HC sites, reporters, databases. |
| **Outputs** | `research/judgments/high-courts/**` |
| **Rules** | Always state court name; avoid over-generalising single-judge orders. |
| **Handoffs** | → Supreme Court Agent (conflict check); → Citation Validation; → Drafting. |

---

### 3.8 Government Policy Agent

| Field | Content |
|-------|---------|
| **Mission** | Map executive policies, schemes, and institutional mandates. |
| **Responsibilities** | Digital India, cyber policies, MeitY/DoT/Consumer Affairs/MoEFCC/CPCB/BIS/CERT-In roles; PLI/electronics policy interfaces; document **absences** of software-support mandates carefully. |
| **Inputs** | Official gov.in portals, Gazette, press information bureau as secondary. |
| **Outputs** | `research/government/**` |
| **Rules** | Soft law labelled soft law; no converting press releases into statutes. |
| **Handoffs** | → Statute Agent; → Evidence Agent; → Drafting (respondent array / exhaustion). |

---

### 3.9 Manufacturer Policy Agent

| Field | Content |
|-------|---------|
| **Mission** | Document OEM software support policies with forensic capture discipline. |
| **Responsibilities** | Per-brand policies; OS vs security years; series variance; India SKU notes; comparison tables. |
| **Inputs** | Official OEM support pages; release blogs (secondary). |
| **Outputs** | `research/manufacturers/**`, tables for `evidence/tables/` |
| **Rules** | Access date mandatory; no brand-wide claims without series evidence; no defamation. |
| **Handoffs** | → Technical Agent; → Evidence Agent; → Citation Validation (URL integrity). |

---

### 3.10 Cybersecurity Agent

| Field | Content |
|-------|---------|
| **Mission** | Explain unsupported-device risk pathways with authoritative technical sources. |
| **Responsibilities** | CVE lifecycle, patch bulletins, UPI/banking risk pathways (non-sensational), CERT-In public materials, enterprise BYOD notes. |
| **Inputs** | NVD, Android Security Bulletins, Apple security pages, CERT-In public advisories, NIST public docs. |
| **Outputs** | `research/cybersecurity/**` |
| **Rules** | No exploit code; no classified data; no false causal statistics. |
| **Handoffs** | → Technical Agent; → Evidence Agent; → Drafting (facts section). |

---

### 3.11 Environmental Agent

| Field | Content |
|-------|---------|
| **Mission** | Connect software-forced obsolescence to e-waste and environmental law/policy. |
| **Responsibilities** | GEM and official Indian e-waste data; EPR framework notes (via Statute/Government agents); lifecycle reasoning. |
| **Inputs** | ITU/UNITAR GEM, CPCB/MoEFCC official data, peer-reviewed LCA where used. |
| **Outputs** | `research/environment/**` |
| **Rules** | Prefer primary stats; label secondary India tonnage until confirmed. |
| **Handoffs** | → Statute Agent (EPA/E-Waste); → Economics Agent; → Evidence Agent. |

---

### 3.12 Economics Agent

| Field | Content |
|-------|---------|
| **Mission** | Model consumer and social costs without false precision. |
| **Responsibilities** | Replacement cost frameworks; externalities; repair economics; EU impact accounting as comparative only. |
| **Inputs** | Official impact assessments, market reports (tiered), Environmental/OEM data. |
| **Outputs** | `research/economics/**` |
| **Rules** | All models marked `ESTIMATE` unless measured; publish assumptions. |
| **Handoffs** | → Evidence Agent; → Drafting (limited use). |

---

### 3.13 Technical Agent

| Field | Content |
|-------|---------|
| **Mission** | Provide accurate descriptive technical baseline for OS/security update mechanisms. |
| **Responsibilities** | Android/iOS update pipelines at conceptual level; definitions (OS upgrade vs security patch vs firmware); fragmentation concepts. |
| **Inputs** | Official platform documentation (AOSP, Apple, OEM). |
| **Outputs** | `research/technical/**` |
| **Rules** | No reverse engineering proprietary blobs for redistribution; no malware. |
| **Handoffs** | → Manufacturer Policy Agent; → Cybersecurity Agent; → Drafting (glossary). |

---

### 3.14 Evidence Agent

| Field | Content |
|-------|---------|
| **Mission** | Transform validated research into annexure-ready artefacts. |
| **Responsibilities** | Charts, tables, timelines; annexure indexes; consistent IDs; chain-of-custody notes for captures. |
| **Inputs** | Validated research outputs from domain agents. |
| **Outputs** | `evidence/charts|tables|timelines|annexures/**` |
| **Rules** | Every figure cites underlying data file/source; no decorative charts without sources. |
| **Handoffs** | → Drafting Agent; → QA; → Git Manager (binary hygiene). |

---

### 3.15 Drafting Agent

| Field | Content |
|-------|---------|
| **Mission** | Draft court-oriented documents only from validated inputs and only in authorised phases. |
| **Responsibilities** | Synopsis, list of dates, PIL body, affidavit, prayers; maintain draft banners; map each assertion to evidence ID. |
| **Inputs** | Research Director “litigation input pack”; Evidence annexure map; PM Phase 9 approval. |
| **Outputs** | `litigation/**` |
| **Rules** | Process mandamus preferred over judicial legislation; no invented facts; counsel certification required before filing. |
| **Handoffs** | → Citation Validation; → QA; → human counsel (external). |

---

### 3.16 Citation Validation Agent

| Field | Content |
|-------|---------|
| **Mission** | Be the final automated/human gate against fabricated or weak citations. |
| **Responsibilities** | Verify case citations, section numbers, URLs, status tags; quarantine failures; maintain ban patterns. |
| **Inputs** | Any PR touching `research/` or `litigation/`. |
| **Outputs** | Validation reports; required fixes list; approve/block recommendation. |
| **Rules** | Fail closed; “looks right” is insufficient for VERIFIED; dual-source preferred for critical holdings. |
| **Handoffs** | → Originating agent (fixes); → QA; → Git Manager (merge blocking). |

---

### 3.17 Quality Assurance Agent

| Field | Content |
|-------|---------|
| **Mission** | Holistic quality: structure, clarity, consistency, tone, phase compliance. |
| **Responsibilities** | Editorial review; SPEC compliance; README accuracy; ensure FACT/LAW/ANALYSIS separation; release readiness. |
| **Inputs** | Near-final artefacts; Citation Validation pass reports. |
| **Outputs** | QA checklist results; polish PRs. |
| **Rules** | Cannot override citation blockers; can block on clarity/structure. |
| **Handoffs** | → PM (release); → Git Manager. |

---

### 3.18 Git Manager

| Field | Content |
|-------|---------|
| **Mission** | Preserve repository integrity, history, and release discipline. |
| **Responsibilities** | Branch strategy, PR mechanics, tags, `.gitignore` enforcement, large-file policy, CHANGELOG commits, remote sync. |
| **Inputs** | Approved PRs; release requests from PM. |
| **Outputs** | Clean history on `main`; version tags; protected branch configs (when on GitHub). |
| **Rules** | No force-push to `main` without explicit human emergency protocol; no secrets commit. |
| **Handoffs** | → All agents (via PR feedback); → Chief Architect (repo surgery). |

---

## 4. Optional Supporting Roles (Non-Core)

| Role | Purpose |
|------|---------|
| Consumer Law Agent | Deep-dive CPA/CCPA unfair practices (may be subsumed under Statute Agent) |
| RTI Agent | Draft RTI applications and track replies |
| Translation Agent | Plain-language / Hindi summaries (future) |
| Red Team Agent | Attempt to find citation holes **without** inventing sources |

---

## 5. Handoff Protocol

### 5.1 Task envelope (recommended)

```yaml
task_id: "P2-STAT-014"
agent: "Statute Agent"
phase: 2
inputs:
  - "templates/statute_note.md"
outputs:
  - "research/statutes/consumer-protection-act-2019.md"
constraints:
  - "VALIDATION.md"
  - "No secondary-only LAW claims"
due: null
```

### 5.2 Definition of done (research task)

1. File in correct folder  
2. Status tag set  
3. Sources listed  
4. Open questions listed  
5. Citation Validation not blocked  
6. TASKS.md checkbox updated by PM or author  

---

## 6. Conflict Resolution

| Conflict | Resolver |
|----------|----------|
| Folder ownership | Chief Architect |
| Priority of tasks | Project Manager |
| Doctrinal research disagreement | Research Director → escalate to human counsel |
| Citation validity | Citation Validation Agent (final on cite form) |
| Release readiness | QA + PM |

---

## 7. Activation Notes

Agents are **contracts**, not a requirement to run 18 concurrent LLMs. A single researcher may wear multiple hats but must still run Citation Validation as a separate pass.

---

*End of AGENTS.md*
