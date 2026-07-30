# National Smartphone Software Support Regulation

**Open-source legal research repository on minimum smartphone software support standards in India**

[![Status](https://img.shields.io/badge/status-Phase%201%20Framework%20Complete-blue)]()
[![Research](https://img.shields.io/badge/legal%20research-not%20started-lightgrey)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Validation](https://img.shields.io/badge/validation-VALIDATION.md%20SoT-red)](VALIDATION.md)
[![Forum](https://img.shields.io/badge/forum-open%20(Art.32%20vs%20226)-orange)](research/forum/)

---

## Start here

**New contributors:** read [`docs/START_HERE.md`](docs/START_HERE.md) first (≈ 5 minutes).

| Priority | Document | Role |
|----------|----------|------|
| 1 | [`docs/START_HERE.md`](docs/START_HERE.md) | Onboarding path |
| 2 | [`VALIDATION.md`](VALIDATION.md) | **Single source of truth — validation & integrity gates** |
| 3 | [`CITATION_POLICY.md`](CITATION_POLICY.md) | **Single source of truth — how to cite** |
| 4 | [`TASKS.md`](TASKS.md) | Task dashboard → `tasks/phase-XX.md` |
| 5 | [`ROADMAP.md`](ROADMAP.md) | Phases 0–10 |

---

## Project Vision

To build a comprehensive, rigorously cited, and openly auditable research corpus on the regulation of smartphone **operating system upgrades** and **security updates** in India—bridging constitutional law, consumer protection, cybersecurity, environmental policy, comparative international regulation, and public-interest litigation readiness.

## Mission

1. Collect and organise **primary legal authorities** (Constitution, statutes, rules, judgments, government policies).  
2. Document **manufacturer software support policies** with source URLs and capture dates.  
3. Integrate **cybersecurity, e-waste, economics, and technical** evidence.  
4. Produce **court-ready work product** only after validation gates pass.  
5. Enforce zero tolerance for **fabricated citations and legal hallucinations**.

## Problem Statement

India is among the world’s largest smartphone markets. Smartphones are essential end-points for UPI, banking, Aadhaar-linked services, DigiLocker, healthcare, education, employment, and digital identity.

Despite this dependence, many devices—especially high-volume budget and mid-range models—historically receive limited OS and security support relative to hardware life. That creates cybersecurity exposure, consumer information asymmetry, premature electronic waste, and regulatory asymmetry relative to jurisdictions adopting product longevity rules.

As of **Phase 1 (research framework)**, infrastructure is in place, but **no substantive legal research conclusions are asserted** and **no forum (Supreme Court Art. 32 vs High Court Art. 226) is pre-selected**.

## Objectives

| ID | Objective |
|----|-----------|
| O1 | Map applicable Indian constitutional, statutory, and policy instruments |
| O2 | Build a verified judgment database (Supreme Court & High Courts) |
| O3 | Catalogue manufacturer software support policies with evidence captures |
| O4 | Compile comparative international law (persuasive only) |
| O5 | Produce cybersecurity, e-waste, and economic evidence packs |
| O6 | Draft PIL-ready documents only after citation validation gates |
| O7 | Automate structure checks and (later) citation linting |
| O8 | Maintain transparent task tracking and lean multi-agent orchestration |

## Repository Structure

Full tree: [`REPOSITORY_STRUCTURE.md`](REPOSITORY_STRUCTURE.md). Summary:

```text
National-Smartphone-Software-Support-Regulation/
├── README.md                 # This file
├── docs/START_HERE.md        # Contributor onboarding
├── VALIDATION.md             # SoT — validation / integrity
├── CITATION_POLICY.md        # SoT — citations
├── TASKS.md                  # Task dashboard
├── tasks/phase-00.md … 10.md # Granular checkboxes by phase
├── AGENTS.md                 # Seven core agents + skill packs
├── ROADMAP.md
├── PROJECT_SPECIFICATION.md
├── research/                 # Domain research (by topic)
│   ├── constitution/
│   ├── statutes/
│   ├── judgments/
│   ├── government/
│   ├── manufacturers/
│   ├── cybersecurity/
│   ├── environment/
│   ├── international/
│   ├── economics/
│   ├── technical/
│   ├── consumer-law/
│   └── forum/                # Art. 32 vs 226 (later; not pre-judged)
├── evidence/                 # Tables, timelines, annexures
├── litigation/               # Court drafts (Phase 9 hard gate)
├── templates/
├── validation/
├── scripts/
├── prompts/agents/           # Skill packs for core agents
├── output/
└── logs/
```

## Research methodology (summary)

Full integrity rules: **[`VALIDATION.md`](VALIDATION.md)**.  
Full citation formats: **[`CITATION_POLICY.md`](CITATION_POLICY.md)**.

1. Primary sources first.  
2. Secondary sources labelled.  
3. Capture URL + access date for web sources.  
4. Separate Fact | Law | Analysis | Open questions.  
5. No promotion to `litigation/` without validation + Phase 9 approval.  

## Contribution

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).  
**Do not** open PRs that invent case law or statutes.

## Disclaimer

This repository is for **research, education, and public-interest preparation**. It is **not** legal advice. Court filings require qualified counsel.

## Roadmap summary

| Phase | Name | Status |
|-------|------|--------|
| 0 | Repository foundation | **Complete** |
| 1 | Research infrastructure | **Complete (framework)** |
| 2–8 | Research & evidence | Pending |
| 9 | Litigation drafting | Pending (hard gate) |
| 10 | Hardening & release | Pending |

See [`ROADMAP.md`](ROADMAP.md) and [`TASKS.md`](TASKS.md).

## Current progress

- [x] Phase 0 foundation  
- [x] Phase 1 framework (templates, validation assets, scripts)  
- [x] Architecture cleanup (navigation, SoT docs, 7 agents, split tasks)  
- [x] Forum path reserved — **decision not made**  
- [ ] Substantive legal research (Phase 2+)  
- [ ] PIL drafting (Phase 9 only)  

### Tooling

```bash
python scripts/check_structure.py
python scripts/list_open_tasks.py
python scripts/new_research_note.py --domain statutes --slug my-note --title "Title"
```

---

*Phase 1 framework complete. Architecture cleanup applied. Substantive research not started.*
