# Validation Constitution

**Project:** National-Smartphone-Software-Support-Regulation  
**Authority:** **Single source of truth (SoT)** for validation, integrity gates, claim classification, source tiers, status tags, and anti-hallucination rules  
**Binding on:** all agents, contributors, and automation  
**Severity model:** `BLOCKER` > `MAJOR` > `MINOR` > `NOTE`  
**Related SoT:** Citation *formats and required bibliographic elements* → [`CITATION_POLICY.md`](CITATION_POLICY.md) (do not fork citation field lists elsewhere)  
**Phase completion (not this file):** [`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md) — whether a **phase** may close and the repository may advance  
**Operational checklists:** [`validation/`](validation/) (implement this constitution; must not contradict it)

### Validation vs Definition of Done

| Instrument | Verifies | Does **not** decide |
|------------|----------|---------------------|
| **This file (`VALIDATION.md`)** | Document quality, claim integrity, anti-hallucination, source tiers, status tags | Whether an entire phase is complete |
| **[`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md)** | Phase completion criteria, task/changelog/navigation closure, advancement policy | Fine-grained citation field formats (see CITATION_POLICY) |

Both are mandatory. A phase full of files that fail VALIDATION is incomplete. A phase that passes VALIDATION on a few notes but fails DoD (coverage, reviews, changelog, approval) is also incomplete.

---

## 1. Purpose

Prevent **legal hallucinations**, **fabricated citations**, **unsourced statistics**, and **premature litigation claims**. This document is the quality constitution of the repository **for document and claim quality**.

## 2. Cardinal Rules (Non-Negotiable)

| # | Rule | Severity if breached |
|---|------|----------------------|
| R1 | **Every legal claim requires a citation.** | BLOCKER |
| R2 | **Every judgment requires an official citation** (e.g., SCC, AIR, SCR, INSC, or court neutral citation as applicable). Case name alone is insufficient for `VERIFIED` status. | BLOCKER |
| R3 | **Every statute/rule requires Act/Rules name, year, and section/rule number.** | BLOCKER |
| R4 | **Every government policy requires an official source** (ministry URL, Gazette ID, policy PDF from gov domain). | BLOCKER |
| R5 | **No fabricated citations.** If a source cannot be found, do not invent one. Mark `UNVERIFIED` or delete the claim. | BLOCKER |
| R6 | **No fabricated judgments, notifications, or OEM promises.** | BLOCKER |
| R7 | **Separate verified facts from analysis.** Use explicit headings or labels. | MAJOR |
| R8 | **Do not present secondary reporting as primary law.** | MAJOR |
| R9 | **Comparative foreign law is persuasive only** unless Indian law incorporates it. | MAJOR |
| R10 | **Litigation drafts remain `DRAFT` until human counsel certification.** | BLOCKER for filing exports |

## 3. Claim Classification

Every substantive statement in `research/` and `litigation/` must be classifiable as one of:

| Class | Label | Requirements |
|-------|-------|--------------|
| Factual | `FACT` | Empirical or documentary; source required |
| Legal | `LAW` | Proposition of law; citation required |
| Analytical | `ANALYSIS` | Reasoning; must rest on labelled FACT/LAW |
| Normative | `NORM` | Policy recommendation; not to be phrased as existing law |
| Open | `OPEN` | Unknown; research task required |

**Forbidden:** Blending `LAW` and `NORM` in a single sentence without labelling (e.g., “India requires 5 years of updates” when no such statute is verified).

## 4. Source Tiers

| Tier | Examples | May support `VERIFIED`? |
|------|----------|-------------------------|
| T0 Primary law | Constitution, India Code, Gazette, official law reports, EUR-Lex, official OEM policy pages | Yes |
| T1 Official secondary | Ministry press notes, CPCB dashboards, parliamentary answers | Yes, with date |
| T2 Reputable secondary | Peer-reviewed journals, UN/ITU reports | Yes for facts; not for Indian black-letter law |
| T3 News / blogs | Tech journalism, opinion | Background only; not sole basis for `LAW` |
| T4 Anonymous / unsourced | Forums, “common knowledge” | No |

## 5. Status Tags (Mandatory Vocabulary)

```text
VERIFIED      — Primary/official source checked by human or dual-agent process
SECONDARY     — Reliable secondary only; pending primary confirmation
UNVERIFIED    — Claim retained as hypothesis; must not be used in prayers as established law
DISPUTED      — Sources conflict
OUTDATED      — Superseded instrument or expired web capture
PROVISIONAL   — Working draft citation pending pin-cite
```

## 6. Domain-Specific Rules

### 6.1 Constitution

- Cite article number.  
- Amendments noted where relevant (e.g., 42nd Amendment for Arts. 48A / 51A).  
- Do not invent “fundamental right to OS updates.”

### 6.2 Statutes & Rules

- Prefer India Code / eGazette.  
- Quote section numbers carefully; amendments must be tracked.  
- Subordinate legislation: cite parent Act + rules name + year + rule number.

### 6.3 Judgments

Required bibliographic fields for each case note follow [`CITATION_POLICY.md`](CITATION_POLICY.md). Summary:

1. Case name  
2. Citation(s)  
3. Court & bench strength (if known)  
4. Year  
5. Facts (brief)  
6. Holding / ratio  
7. Pin-cite status (`PROVISIONAL` until verified)  
8. Application to project (clearly labelled `ANALYSIS`)

**Never** invent paragraph numbers.

### 6.4 Government policy

- Record issuing body, title, date, URL, access date.  
- Soft law ≠ statute; label as policy.

### 6.5 Manufacturers

- Capture URL + access datetime.  
- State series/model scope; no brand-wide generalisation without evidence.  
- Distinguish marketing claims vs support portal matrix.

### 6.6 Statistics (cyber, e-waste, economics)

- Name the report and year.  
- Label models as `ESTIMATE` when not measured.  
- Forbidden: false precision (“23.47% of UPI fraud caused by OS EOL”) without study.

### 6.7 International law

- Header on every comparative note: `PERSUASIVE COMPARATIVE MATERIAL — NOT BINDING IN INDIA`.  
- Cite instrument number (e.g., Regulation (EU) 2023/1670).

## 7. File Gate Checklist (Research)

Before merging research into `main`:

- [ ] Claims classified (FACT/LAW/ANALYSIS/NORM/OPEN)  
- [ ] Citations present for LAW and FACT  
- [ ] Status tags applied  
- [ ] No empty “see judgment X” without citation  
- [ ] Sources section at end of memo  
- [ ] Open questions listed  
- [ ] Filename and folder match domain  

## 8. File Gate Checklist (Litigation)

- [ ] Every pleading assertion maps to research note or annexure ID  
- [ ] No prayer that asserts unenacted Indian law as existing  
- [ ] Process-oriented relief preferred where separation of powers applies  
- [ ] `DRAFT — NOT FOR FILING` banner present until counsel sign-off  
- [ ] Citation Validation Agent report attached or linked  
- [ ] QA Agent checklist complete  

## 9. Automation Validation (Target State)

Scripts under `scripts/` and rules under `validation/` should eventually enforce:

| Check | Description |
|-------|-------------|
| Structure | Required directories exist |
| Front-matter | Optional YAML status fields |
| Citation pattern | Heuristic detection of uncited legal language |
| Banlist | Phrases like “as held in *Fake Case*” patterns from known bad lists |
| Link rot | Periodic URL check (non-blocking warnings) |

Until automation exists, **manual compliance** with this document is mandatory.

## 10. Incident Response (Hallucination Found)

1. Open issue with label `validation/blocker`.  
2. Quarantine file: set status `UNVERIFIED` or revert commit.  
3. Remove or rewrite offending claim within 48 hours for `main`.  
4. Log incident in `logs/validation-incidents.md` (create when first needed).  
5. Add regression note to Citation Validation Agent prompts.

## 11. Roles in Validation

| Role | Duty |
|------|------|
| Citation Validation Agent | Final gate on citations |
| Quality Assurance Agent | Holistic quality, structure, tone |
| Research Director | Prioritises verification backlog |
| Drafting Agent | Must not invent authorities to fill gaps |
| All agents | Refuse tasks that require fabrication |

## 12. Acceptance Slogan

> **If it cannot be cited, it cannot be claimed.**  
> **If it cannot be verified, it cannot be filed.**

---

*End of Validation Constitution*
