# Definition of Done (Repository-Wide)

**Authority:** Authoritative quality gate for **phase completion** and advancement  
**Project:** National-Smartphone-Software-Support-Regulation  
**Version:** 1.0.0  
**Last updated:** 2026-07-30  
**Status:** Mandatory for every phase  

| Concern | Governing document |
|---------|-------------------|
| **Document / claim quality** (citations, labels, no fabrication) | [`VALIDATION.md`](../VALIDATION.md) |
| **Citation formats** | [`CITATION_POLICY.md`](../CITATION_POLICY.md) |
| **Phase completion & advancement** | **This file** + phase-specific DoD in `tasks/phase-XX.md` |

A phase is **not** complete merely because files exist or checkboxes are ticked without evidence.

---

## 1. Purpose

Define objective, reviewable criteria that must be true before:

1. A phase may be marked **Complete** on [`TASKS.md`](../TASKS.md); and  
2. Work may **begin** on the next phase.

---

## 2. Inheritance rule

Every phase inherits **all** criteria in this document **plus** the phase-specific **Definition of Done** section in:

`tasks/phase-XX.md`

If repository-wide and phase-specific criteria conflict, the **stricter** requirement applies. Raise an issue rather than silently weakening gates.

---

## 3. Repository-wide Definition of Done

Before a phase is marked Complete, **all** applicable items below must be satisfied (N/A only if the phase has no work in that category—document N/A with reason in the phase completion note).

### 3.1 Research completeness

- [ ] Planned deliverables for the phase (per `ROADMAP.md` and `tasks/phase-XX.md`) exist in the correct folders.  
- [ ] Scope of the phase is covered or residual gaps are listed as explicit `OPEN` items with owners/next steps—not silently omitted.  
- [ ] No phase is closed with only empty placeholders where content was required.  
- [ ] Domain `README.md` indexes (if the phase owns research folders) list new artefacts or state “none this phase.”  

### 3.2 Validation requirements

- [ ] All new/changed content under `research/` and `litigation/` complies with [`VALIDATION.md`](../VALIDATION.md).  
- [ ] Research-gate / litigation-gate checklists used where applicable (`validation/`).  
- [ ] Zero known BLOCKER validation defects remain open for the phase’s artefacts.  
- [ ] Claim labels (FACT / LAW / ANALYSIS / NORM / OPEN) used as required.  

### 3.3 Citation requirements

- [ ] Citations meet [`CITATION_POLICY.md`](../CITATION_POLICY.md).  
- [ ] No fabricated authorities.  
- [ ] Every LAW/FACT claim in phase deliverables has a source or is marked OPEN/UNVERIFIED.  
- [ ] Comparative materials carry non-binding-in-India treatment where required by VALIDATION.md.  

### 3.4 Documentation updates

- [ ] Any new contributor-facing behaviour is reflected in the relevant doc (`docs/`, README progress if phase status changes).  
- [ ] Stale statements that contradict the completed phase are fixed (no “planned” language for delivered work).  

### 3.5 Navigation updates

- [ ] Links to new key artefacts from the appropriate index (`research/README.md`, domain README, `TASKS.md` dashboard counts as needed).  
- [ ] No known broken internal links introduced by the phase (spot-check new paths).  

### 3.6 Task tracking

- [ ] Checkboxes in `tasks/phase-XX.md` match reality (done work checked; incomplete work open).  
- [ ] [`TASKS.md`](../TASKS.md) dashboard status/counts updated for the phase.  
- [ ] No “done” checkbox without corresponding artefact or explicit N/A justification.  

### 3.7 Changelog updates

- [ ] [`CHANGELOG.md`](../CHANGELOG.md) records the phase completion (or material interim release) under the correct version heading.  
- [ ] Changelog does not claim research or litigation outcomes that were not delivered.  

### 3.8 Cross-reference verification

- [ ] Cross-links among phase artefacts, tasks, and governance docs resolve.  
- [ ] Assertion→source maps exist for litigation-bound claims when the phase produces them.  

### 3.9 Removal of placeholders / TODOs

- [ ] No active `TODO`, `TBD`, `FIXME`, or “lorem ipsum” remains in files marked complete/VERIFIED for the phase.  
- [ ] Remaining unknowns are captured as **OPEN** sections, not fake completion.  
- [ ] Synthetic/demo-only files remain clearly labelled as non-authority.  

### 3.10 Review requirements

- [ ] Citation Validation pass (agent or human) on phase research/litigation outputs.  
- [ ] QA pass for structure, clarity, and phase compliance.  
- [ ] For Phase 9+: human counsel review path acknowledged; drafts retain required banners until certified.  

### 3.11 Completion approval

- [ ] Project Manager (or maintainer acting as PM) records phase completion in `CHANGELOG.md` and/or a short `logs/` note.  
- [ ] Phase status on `TASKS.md` set to **Complete** only after the above.  
- [ ] Explicit statement: **next phase is not auto-started**.  

---

## 4. Phase advancement policy

1. **No phase may begin** until the previous phase satisfies its Definition of Done (repository-wide + phase-specific), except parallel research phases explicitly allowed in `ROADMAP.md` (e.g. some Phase 3–7 streams) **after Phase 1 is complete**.  
2. Phase 0 and Phase 1 are foundational; later phases depend on them.  
3. **Phase 9** additionally requires written PM approval in `CHANGELOG.md` before any drafting.  
4. Failing any BLOCKER validation item blocks phase completion regardless of checkbox count.  
5. Advancement is a **governance decision**, not an automated side effect of file creation.

---

## 5. Relationship to other gates

```text
VALIDATION.md          →  Is this document/claim acceptable?
CITATION_POLICY.md     →  Is this citation well-formed?
DEFINITION_OF_DONE.md  →  Is this phase finished enough to advance?
```

Pull requests must satisfy **VALIDATION** (and CITATION_POLICY) always.  
Phase-completion PRs / release notes must additionally satisfy **Definition of Done**.

---

## 6. Completion record template

When closing a phase, add a log entry (e.g. `logs/YYYY-MM-DD_phase-XX_complete.md`) or CHANGELOG subsection including:

- Phase number and name  
- Link to `tasks/phase-XX.md`  
- Confirmation that repository-wide DoD §3 was checked  
- Confirmation that phase-specific DoD was checked  
- Residual OPEN items  
- Explicit: “Next phase not started automatically”  

---

## 7. Waivers

Temporary waivers require:

1. Written reason in an issue or PR;  
2. PM acknowledgment;  
3. CHANGELOG note;  
4. Time-bound follow-up task in `tasks/`.  

Waivers never permit fabricated citations.

---

*End of Definition of Done v1.0.0*
