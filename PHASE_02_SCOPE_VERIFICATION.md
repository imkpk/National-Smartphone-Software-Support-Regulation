# Phase 2 Scope Verification — Articles 12 & 47

**Repository:** National-Smartphone-Software-Support-Regulation  
**Date:** 2026-07-30  
**Branch context:** `main` (post constitution + statutes workstreams)  
**Nature of work:** Scope verification only — **no new constitutional research**, no corpus expansion, no architecture change  

---

## 0. Repository state (inputs reviewed)

| Item | Finding |
|------|---------|
| **Version / progress** | CHANGELOG through **0.3.2** (statutes); README progress reflects constitution + statutes done |
| **Completed phases** | 0 (foundation), 1 (framework) |
| **Current phase** | Phase 2 — **nearly complete** |
| **Completed workstreams** | Constitution (assigned Articles); Statutes (assigned instruments); Consumer-law interface notes |
| **Remaining Phase 2 task IDs** | **T093** (Article 47), **T098** (Article 12) — only open Phase 2 checkboxes |
| **Outstanding DoD issue** | Prior reports treat Art. 12 / Art. 47 as residual blockers or optional gaps |
| **Existing reports** | `PHASE_02_COMPLETION_REPORT.md`, `PHASE_02_STATUTES_REPORT.md` |
| **Constitution corpus** | 11 Article notes + matrix/FR–DPSP map; coverage matrix already lists Art. 12/47 as “not covered this workstream” |

**Project objectives (relevant extract):** map constitutional provisions **relevant** to digital end-points, equality, privacy, environment, consumer welfare, and writ jurisdiction (`PROJECT_SPECIFICATION.md` §4; README mission). Methodology prioritises material contribution over encyclopaedic completeness (`VALIDATION.md` / quality-over-volume ethos in architecture review).

**Constraint applied:** Do not assume every Article is in scope. Prefer quality over size.

---

## 1. Article 12

### 1.1 Summary

Article 12 (Part III) defines **“the State”** for the purposes of Part III fundamental rights. In substance, it brings within “the State” the Government and Parliament of India, Government and Legislature of each State, and all local or other authorities within India or under the control of the Government of India (exact wording to be taken from official Constitution text if a note is ever written).  

It is a **definitional gateway**, not a substantive right about equality, privacy, environment, or product regulation.

*No new research note produced in this verification.* Existing corpus already flags Article 12 as the definitional cross-reference for “State” in `article-14.md` and related FR notes (OPEN / cross-ref language).

### 1.2 Relevance assessment (to project themes)

| Theme | Connection |
|-------|------------|
| Smartphone software support | **Indirect only** — relevant if/when Part III duties are argued against government actors; does not regulate OEM update cycles |
| Consumer protection | Peripheral — consumer statutes bind traders; Art. 12 is about Part III addressees |
| Cybersecurity | Indirect — State cyber institutions are “State”; still not an OS-support rule |
| Digital rights | **Supporting** — FR claims under Arts. 14/21 presuppose a State actor under Art. 12 |
| Environmental sustainability | Minimal — unless environmental FR claims against public authorities |
| Regulatory framework | Supporting — Union ministries (MeitY, DoT, etc.) are paradigmatically “State” |

### 1.3 Contribution class

**Supporting legal context** (definitional).

- Not a primary legal foundation for *software support standards content*.  
- Not peripheral in the abstract (FR theory needs it), but **largely non-dispositive** for this repository’s substantive map given that respondents are already framed as Union of India / statutory bodies.

### 1.4 Would excluding it weaken the repository?

**No material weakening of Phase 2 deliverables**, provided:

1. Existing FR notes continue to state that Part III binds the “State” (as already done); and  
2. Coverage matrix / OPEN list documents Art. 12 as definitional cross-reference rather than a silent gap.

A dedicated multi-section Article 12 memo is **not** required to understand CPA, E-Waste Rules, BIS pathways, or comparative eco-design—which now form the core of Phase 2.

### 1.5 Litigation-readiness

| Effect of inclusion | Effect of exclusion from Phase 2 gate |
|---------------------|--------------------------------------|
| Slight improvement: explicit definition note for pleadings against Union/authorities | Minimal harm if FR notes already assume Union = State and Phase 9 can add a short definitional paragraph |

Full Article 12 doctrine (instrumentality tests, other authorities, etc.) is **case-law heavy** and better as a **short definitional card at litigation pack time** or a slim optional note—not a Phase 2 research epic.

### 1.6 Better in a later phase?

**Yes, if at all:**  

- **Phase 9** (litigation drafting) — one definitional subsection in maintainability/respondents; or  
- **Phase 3** only if judgment digests on “other authorities” become necessary.  

Not a blocker for closing statutory + primary FR/DPSP mapping.

### 1.7 Risks

| Inclusion risks | Exclusion risks |
|-----------------|-----------------|
| Scope creep; encyclopaedic constitution notes | Under-specifying “State” if later FR claims against non-obvious authorities |
| Duplicates content already implied in Art. 14/21/32 notes | Incomplete for readers new to Indian constitutional structure |

### 1.8 Recommendation (exactly one)

### ✓ Optional

**Meaning for Phase 2:** Do **not** treat a full Article 12 research note as **required** for Phase 2 Definition of Done.  

May keep T098 as **optional** (nice-to-have definitional note) or cancel it from the Phase 2 gate while retaining a one-line coverage-matrix entry: “Article 12 — definitional gateway for Part III; not a software-support standard.”

---

## 2. Article 47

### 2.1 Summary

Article 47 is a **Directive Principle** (Part IV) directing the State to regard the raising of the level of nutrition and the standard of living of its people and the improvement of public health as among its primary duties, and to endeavour to bring about prohibition of intoxicating drinks and drugs (except for medicinal purposes)—confirm exact text against official Constitution if ever cited.  

It is a **public health / nutrition / standard-of-living DPSP**, not a digital, consumer-product, or e-waste provision.

*No new research note produced.*

### 2.2 Relevance assessment (to project themes)

| Theme | Connection |
|-------|------------|
| Smartphone software support | **No material direct connection** |
| Consumer protection | Peripheral at most (general welfare backdrop); CPA 2019 already covers consumer domain |
| Cybersecurity | None material |
| Digital rights | None material |
| Environmental sustainability | Weak/strained (health–environment overlap is speculative for OS updates) |
| Regulatory framework | Does not supply standards, EPR, or disclosure tools |

Contrast with **already completed** DPSPs that *do* map cleanly: **Article 48A** (environment), **Article 38/39** (welfare/inequality backdrop). Article 47 would largely **duplicate low-intensity welfare backdrop** already available via Arts. 38/39 without adding software-specific leverage.

### 2.3 Contribution class

**No material contribution** to the repository’s core research question (minimum smartphone software support regulation), beyond generic “State should improve public health,” which does not advance statutory mapping already done (CPA, IT Act, E-Waste Rules, BIS, Legal Metrology).

### 2.4 Would excluding it weaken the repository?

**No.** Exclusion improves focus. The corpus already risks DPSP over-inclusion (38, 39, 48A, 51A(g)); adding 47 increases size without analytical yield.

### 2.5 Litigation-readiness

**Does not meaningfully improve** litigation-readiness for a software-support / e-waste / consumer-standards theory of the case. Health-based constitutional framing for unpatched phones would be attenuated and is not required by the project’s stated primary pathways (consumer law, cyber institutions, e-waste, standards, Arts. 14/21/48A).

### 2.6 Better in a later phase?

**No need** unless a future evidence pack develops a specific public-health empirical thesis (e.g. documented health-system dependence on insecure devices). Even then, Article 47 would remain a weak supporting DPSP citation, not a Phase 2 foundation piece.

### 2.7 Risks

| Inclusion risks | Exclusion risks |
|-----------------|-----------------|
| Dilutes repository focus; implies every DPSP is project-relevant | Essentially none for this project’s scope |
| Invites strained “public health” overclaims | None identified |

### 2.8 Recommendation (exactly one)

### ✓ Remove from Phase 2

**Meaning:** Remove Article 47 / T093 as a **Phase 2 required (or residual open) task**. Do not expand the constitutional corpus for Art. 47 unless a later, evidence-led change control revisits scope.

Optional one-line in coverage matrix: “Article 47 — out of primary project scope (public health DPSP; no material software-support link).”

---

## 3. Strength of connection (comparative)

| Article | Strength of connection to project core | Class |
|---------|----------------------------------------|--------|
| **12** | Medium (definitional for FR claims against State) | Supporting context |
| **47** | Very low / none material | No material contribution |

---

## 4. Final decision — Phase 2 Definition of Done

### 4.1 Are either Articles **Required** for Phase 2?

| Article | Required for Phase 2 DoD? |
|---------|---------------------------|
| 12 | **No** (Optional only) |
| 47 | **No** (Remove from Phase 2) |

Therefore **Phase 2 should not remain open solely because of T093/T098**.

### 4.2 Recommendation on Phase 2 status

**Yes — recommend updating Phase 2 to COMPLETE**, after administrative task hygiene:

| File | Recommended update (not performed in this verification run) |
|------|---------------------------------------------------------------|
| `tasks/phase-02.md` | Cancel or re-label T093 as **removed from Phase 2 scope**; re-label T098 as **optional / deferred** (not a gate); mark Phase 2 DoD residual Art. 12/47 items satisfied by scope decision; update progress to 49/49 or 47 done + 2 cancelled |
| `TASKS.md` | Set Phase 2 status to **Complete**; adjust counts; next work = Phase 3 only when authorised |
| `CHANGELOG.md` | Record Phase 2 formal close based on scope verification (cite this file) |
| `research/constitution/coverage-matrix.md` | Optional one-line status for Art. 12 (optional/definitional) and Art. 47 (out of Phase 2 scope) — **only if** a follow-up admin commit is approved |
| `README.md` Current progress | Align: Phase 2 complete; Phase 3 not started |

### 4.3 Why Phase 2 need **not** stay open

1. **Substantive Phase 2 missions are met:** constitution (material Articles), statutes (planned instruments), consumer-law interface, negative finding on OS-year mandate, matrices, validation reports.  
2. **Art. 47** fails materiality.  
3. **Art. 12** is definitional supporting context already flagged in FR notes; optional, not a completeness gate.  
4. Keeping Phase 2 open for these two IDs would **prioritise checklist volume over repository quality**, contrary to verification rules.  
5. Phase 3 (judgments) and later phases remain correctly blocked until a human authorises them—not by Art. 12/47.

### 4.4 What this verification does **not** do

- Does not authorise Phase 3.  
- Does not write Art. 12 or Art. 47 research notes.  
- Does not itself edit TASKS/CHANGELOG (stop condition: report only).  
- Does not assert litigation strategy.

---

## 5. Recommendation summary table

| Article | Recommendation | Phase 2 gate? |
|---------|----------------|---------------|
| **Article 12** | **Optional** | No — do not block Phase 2 close |
| **Article 47** | **Remove from Phase 2** | No — do not research for Phase 2 |

| Overall | Recommendation |
|---------|----------------|
| Phase 2 DoD | **Update task scope; then mark Phase 2 COMPLETE** |
| Next human action | Admin commit to TASKS / phase-02 / CHANGELOG / README per §4.2 |
| Phase 3 | Still **not started**; requires separate authorisation |

---

## 6. Stop condition

Verification report complete.  

**Stopped.** No Phase 3. No additional constitutional research. No task-file edits in this run.

---

*End of PHASE_02_SCOPE_VERIFICATION.md*
