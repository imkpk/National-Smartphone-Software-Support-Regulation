# National Smartphone Software Support Regulation

**Open-source legal research repository on minimum smartphone software support standards in India**

[![Status](https://img.shields.io/badge/status-Phase%200%20Foundation-blue)]()
[![Research](https://img.shields.io/badge/legal%20research-not%20started-lightgrey)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Validation](https://img.shields.io/badge/hallucinations-forbidden-red)](VALIDATION.md)

---

## Project Vision

To build the **world’s most comprehensive, rigorously cited, and openly auditable** research corpus on the regulation of smartphone **operating system upgrades** and **security updates** in India—bridging constitutional law, consumer protection, cybersecurity, environmental policy, comparative international regulation, and public interest litigation readiness.

## Mission

Engineer a Fortune-500-grade open research system that:

1. Collects and organises **primary legal authorities** (Constitution, statutes, rules, judgments, government policies).
2. Documents **manufacturer software support policies** with source URLs and capture dates.
3. Integrates **cybersecurity, e-waste, economics, and technical** evidence.
4. Produces **court-ready litigation work product** only after multi-agent validation.
5. Enforces a zero-tolerance policy against **fabricated citations and legal hallucinations**.

## Problem Statement

India is among the world’s largest smartphone markets. Smartphones are essential end-points for UPI, banking, Aadhaar-linked services, DigiLocker, healthcare, education, employment, and digital identity.

Despite this dependence, many devices—especially high-volume budget and mid-range models—historically receive limited OS and security support relative to hardware life. That creates:

- **Cybersecurity exposure** on unpatched devices  
- **Consumer information asymmetry** at the point of sale  
- **Premature electronic waste** while hardware remains functional  
- **Regulatory asymmetry** relative to jurisdictions adopting product longevity rules (e.g., EU Ecodesign for smartphones)

As of repository foundation (Phase 0), **no research conclusions are asserted**. This repository exists to investigate the problem with academic and forensic discipline before any litigation package is finalised.

## Objectives

| ID | Objective |
|----|-----------|
| O1 | Map all applicable Indian constitutional, statutory, and policy instruments |
| O2 | Build a verified judgment database (Supreme Court & High Courts) |
| O3 | Catalogue manufacturer software support policies with evidence captures |
| O4 | Compile comparative international law on software support / repair / eco-design |
| O5 | Produce validated cybersecurity, e-waste, and economic evidence packs |
| O6 | Draft PIL-ready documents only after citation validation gates pass |
| O7 | Automate structure checks, citation linting, and export pipelines |
| O8 | Maintain transparent task tracking and multi-agent orchestration |

## Repository Structure

```text
National-Smartphone-Software-Support-Regulation/
├── README.md                 # This file
├── LICENSE
├── PROJECT_SPECIFICATION.md  # Full product/research specification
├── ROADMAP.md                # Phase 0–10 roadmap
├── TASKS.md                  # 300+ granular checkbox tasks
├── AGENTS.md                 # Multi-agent architecture
├── VALIDATION.md             # Anti-hallucination & quality rules
├── MASTER_PROMPT.md          # Placeholder for autonomous orchestration
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── .github/                  # Issues, templates, CI placeholders
├── docs/                     # Human-facing documentation
├── research/                 # Domain research (primary work product)
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
│   └── consumer-law/
├── evidence/                 # Charts, tables, timelines, annexures
├── litigation/               # PIL drafts (empty until authorised phases)
├── templates/                # Document & research templates
├── prompts/                  # Agent prompt libraries
├── automation/               # Orchestration configs
├── validation/               # Schemas, checklists, lint rules
├── scripts/                  # Tooling
├── output/                   # Generated exports (gitignored content-heavy)
└── logs/                     # Run logs (gitignored content-heavy)
```

## Research Methodology

1. **Primary sources first** — Constitution, India Code, Gazette, official court reports, ministry portals, EUR-Lex, OEM sites.  
2. **Secondary sources labelled** — commentaries, news, blogs never substitute for primary law.  
3. **Capture discipline** — URL + access date + archive method for web sources.  
4. **Separation of layers** — *Fact* | *Law* | *Analysis* | *Open Question* in every research note.  
5. **Validation gates** — no promotion to `litigation/` or `output/court/` without Citation Validation Agent sign-off.  
6. **Uncertainty explicit** — “Not verified”, “Secondary only”, “Conflicting sources” are first-class statuses.

## Citation Policy

- Every legal claim requires a **citation**.  
- Every judgment requires **case name + official citation** (SCC / AIR / SCR / neutral citation as applicable).  
- Every statute requires **Act name + year + section/rule**.  
- Every policy requires an **official source link or document ID**.  
- **No fabricated citations.** If uncertain, mark `UNVERIFIED` and do not cite as authority.  
- Full rules: [`VALIDATION.md`](VALIDATION.md).

## Contribution Guide

Contributions are welcome after reading:

- [`CONTRIBUTING.md`](CONTRIBUTING.md)  
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)  
- [`VALIDATION.md`](VALIDATION.md)  
- [`AGENTS.md`](AGENTS.md) (if working in agent workflows)

**Do not** open PRs that invent case law or statutes. Prefer small, cited, reviewable commits.

## Disclaimer

This repository is for **research, education, and public-interest preparation**. It is **not** legal advice. Nothing herein creates an attorney–client relationship. Court filings must be reviewed by qualified counsel admitted to the relevant bar. Open-source publication does not guarantee completeness or currency of the law.

## Roadmap Summary

| Phase | Name | Status |
|-------|------|--------|
| 0 | Repository foundation | **In progress / this release** |
| 1 | Research infrastructure & templates | Pending |
| 2 | Indian constitutional & statutory map | Pending |
| 3 | Judgments corpus | Pending |
| 4 | Government policy & institutional map | Pending |
| 5 | Manufacturer & technical evidence | Pending |
| 6 | Cybersecurity, environment, economics | Pending |
| 7 | Comparative international law | Pending |
| 8 | Evidence pack & annexure factory | Pending |
| 9 | Litigation drafting (PIL package) | Pending |
| 10 | Validation, automation, public release hardening | Pending |

See [`ROADMAP.md`](ROADMAP.md) and [`TASKS.md`](TASKS.md).

## Current Progress

- [x] Repository name and root scaffold  
- [x] Directory structure for research, evidence, litigation, automation  
- [x] Governance documents (spec, roadmap, tasks, agents, validation)  
- [x] Contribution / conduct / license / changelog  
- [ ] Legal research (explicitly **not started** in Phase 0)  
- [ ] PIL drafting (explicitly **not started** in Phase 0)  
- [ ] Judgment research (explicitly **not started** in Phase 0)  

---

**Maintainer standard:** Treat every file as if it may be scrutinised by a High Court, the Supreme Court, peer reviewers, and the public simultaneously.

*Phase 0 — Foundation only.*
