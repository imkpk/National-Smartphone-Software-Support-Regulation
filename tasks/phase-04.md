# Phase 04 Tasks

**Project:** National-Smartphone-Software-Support-Regulation  
**Parent dashboard:** [../TASKS.md](../TASKS.md)  
**Rules:** [../VALIDATION.md](../VALIDATION.md) · [../CITATION_POLICY.md](../CITATION_POLICY.md) · [../docs/DEFINITION_OF_DONE.md](../docs/DEFINITION_OF_DONE.md) · [../docs/DEFINITION_OF_DONE.md](../docs/DEFINITION_OF_DONE.md)  
**Progress:** 15 done · 9 open · 24 total  
**Phase status:** **In progress** — WS1–WS7 (Audit) when merged; next WS8 Completion  
**Specs:** [`../REPOSITORY_OS.md`](../REPOSITORY_OS.md) · [`../PHASE_04_SPECIFICATION.md`](../PHASE_04_SPECIFICATION.md)  

> Check boxes only when complete and validation rules are satisfied.

---

## Phase 4 — Government Policy & Institutions


### Institutions

- [x] **T169** Profile MeitY mandate and org touchpoints
- [x] **T170** Profile Department of Telecommunications mandate
- [x] **T171** Profile Department of Consumer Affairs / CCPA
- [x] **T172** Profile MoEFCC mandate
- [x] **T173** Profile CPCB role in e-waste
- [x] **T174** Profile BIS standards role
- [x] **T175** Profile CERT-In role
- [x] **T176** Profile TRAI relevance check (include or exclude with reasons)
- [x] **T177** Profile RBI/NPCI as stakeholder (not necessarily respondents)
- [x] **T178** Build institutional RACI matrix

### Policies & schemes

- [x] **T179** Catalogue Digital India official materials relevant to mobile end-points
- [x] **T180** Catalogue National Cyber Security Policy 2013 and successors check
- [x] **T181** Catalogue electronics manufacturing / PLI scheme interfaces *(WS5 programme note; operational PDF pins residual OPEN)*
- [ ] **T182** Catalogue any MeitY mobile security guidelines (if any) *(residual — not identified in WS1; remains OPEN)*
- [ ] **T183** Catalogue consumer awareness digital payment advisories (RBI samples) *(deferred — adjacent domain)*
- [x] **T184** Search for draft consultation papers on right to repair in India *(policy search log; deep consultation inventory → WS4)*
- [ ] **T185** Search for parliamentary questions on smartphone updates/e-waste *(Phase 3 committees covered reports; PQ catalogue residual)*
- [ ] **T186** Document grievance portals CPGRAMS metadata fields
- [ ] **T187** Draft RTI question set for MeitY on software support standards
- [ ] **T188** Draft RTI question set for BIS
- [ ] **T189** Draft RTI question set for CPCB mobile e-waste share
- [ ] **T190** Draft RTI question set for Consumer Affairs/CCPA
- [x] **T191** Create government sources master list with URLs *(policy sources in POLICY_SOURCE_REPORT + notes; full master list residual)*
- [x] **T192** Policy Agent validation pass *(POLICY_VALIDATION_REPORT.md)*

### Workstream 1 status (2026-07-30) — Government Policies

- Notes under `research/policy/` (NCSP 2013, NPE 2019, Digital India, NDCP 2018, repair/longevity search).
- Negative finding: no multi-year OS/security-support duty in policies reviewed.
- Reports: POLICY_* + PHASE_04_POLICY_WORKSTREAM_REPORT.md.
- **Merged** PR #17.

### Workstream 2 status (2026-07-31) — Government Institutions

- Notes under `research/institutions/` (MeitY, DoT, DCA/CCPA, MoEFCC, CPCB, BIS, CERT-In, TRAI, RBI/NPCI, RACI).
- Negative finding: no multi-year OS duty in institutional mandates reviewed.
- Reports: INSTITUTION_* + PHASE_04_INSTITUTIONS_WORKSTREAM_REPORT.md.
- **Merged** PR #18.

### Workstream 3 status (2026-07-31) — Standards & Technical Guidance

- Notes under `research/standards/` (CERT-In directions/guidelines; BIS OS search; MeitY CRO orientation).
- Negative finding: no multi-year OS product Indian Standard identified.
- Reports: STANDARDS_* + PHASE_04_STANDARDS_WORKSTREAM_REPORT.md.
- Repository Relevance on all new notes.
- **Merged** PR #20.

### Workstream 4 status (2026-07-31) — Public Consultations

- Notes under `research/consultations/` (MeitY DPDP draft rules; AI governance guidelines; BIS draft-comment process; search log).
- Negative finding: no official multi-year OS-support consultation identified.
- Reports: CONSULTATION_* + PHASE_04_CONSULTATIONS_WORKSTREAM_REPORT.md.
- **Merged** PR #21.

### Workstream 5 status (2026-07-31) — Government Programmes

- Notes under `research/programs/` (Digital India, Cyber Surakshit Bharat, PLI electronics, e-waste EPR, NeGD, search log).
- Negative finding: no multi-year OS-support government programme identified.
- Reports: PROGRAMME_* + PHASE_04_PROGRAMMES_WORKSTREAM_REPORT.md.
- **Merged** PR #22.

### Workstream 6 status (2026-07-31) — Gap Analysis

- Synthesis under `research/phase4-gap-analysis/` (WS1–WS5 only; no new research; no recommendations).
- Integrated finding: no multi-year OS floor identified across Phase 4 layers.
- Reports: GAP_* + PHASE_04_GAP_ANALYSIS_WORKSTREAM_REPORT.md.
- **Merged** PR #23.

### Workstream 7 status (2026-07-31) — Repository Audit

- Artefacts: `PHASE_4_AUDIT.md`, `AUDIT_SUMMARY.md`, `AUDIT_CHECKLIST.md`, health/validation/link/cross-ref/docs reports.
- Result: **PASS WITH MINOR ISSUES** (no Critical/Major).
- No new research; no research rewrite.
- Phase 4 **not** complete.
- Do **not** auto-start WS8 Completion without authorization.

---
## Definition of Done

**Inherits:** [docs/DEFINITION_OF_DONE.md](../docs/DEFINITION_OF_DONE.md) (repository-wide, mandatory).

Phase 4 is complete only when **all** of the following are true (in addition to repository-wide DoD):

- [ ] Institutional profiles (MeitY, DoT, Consumer Affairs, MoEFCC, CPCB, BIS, CERT-In as planned) exist with official sources.
- [ ] Policy/scheme inventory exists; soft law labelled as soft law.
- [ ] RTI question sets drafted if planned for the phase.
- [ ] Government sources master list with URLs and access discipline per CITATION_POLICY.
- [ ] Absences of software-support mandates recorded as negative findings when claimed—not asserted without search log.
- [ ] 
esearch/government README updated; validation gates satisfied.
- [ ] Task checkboxes + dashboard + CHANGELOG updated.
- [ ] Citation Validation + QA review recorded.
- [ ] **Completion approval:** PM marks Complete; **does not auto-start the next phase**.
