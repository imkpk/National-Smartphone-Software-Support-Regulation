# Phase Gate & Quality Review Prompt

**Status:** Active  
**Version:** 1.0.0  
**Location:** `prompts/phase_gate_quality_review.md`  
**Purpose:** Strict quality and process review of the repository after research batches.  
**Authority:** Bound by `VALIDATION.md`, `CITATION_POLICY.md`, `docs/DEFINITION_OF_DONE.md`, and `MASTER_PROMPT.md`.

---

## Context

You are reviewing the repository  
`imkpk/National-Smartphone-Software-Support-Regulation`.

This is a rigorous open-source legal research repository preparing the foundation for possible public-interest litigation on minimum smartphone OS and security update standards in India.

Current verified status (update as needed):

- Phase 0 (Foundation) → Complete
- Phase 1 (Research Infrastructure) → Complete
- Phase 2 Constitution workstream → Substantially complete
- Phase 2 Statutes workstream → In progress / recently advanced
- Substantive judgments, OEM policies, comparative law, and litigation drafting → **Not started**
- Forum choice (Art. 32 Supreme Court vs Art. 226 High Court) remains deliberately open

---

## Your Task

Perform a strict quality and process review. Be precise and critical. Do not inflate scores.

### Evaluation Dimensions

Rate each area from 1–10 and give a short justification:

1. Repository Architecture
2. Governance & Validation Discipline
3. Research Workflow & Phase Discipline
4. Documentation Quality
5. Multi-agent Design
6. Long-term Maintainability & Scalability

### Mandatory Checks

1. Has the repository respected phase gates? (Especially: no premature move into litigation or unvalidated claims)
2. Are constitutional / statutory notes using provisional language or OPEN status where conclusions are not yet fully supported by primary sources?
3. Has forum neutrality (Art. 32 vs 226) been preserved?
4. Is there clear separation between **FACT | LAW | ANALYSIS | NORM | OPEN**?
5. Are citation and validation rules being followed (`VALIDATION.md` + `CITATION_POLICY.md`)?
6. Does every research note that claims relevance have a documented rationale for inclusion?

### Required Recommendations (only if justified)

- Research Dependency Graph (`research/DEPENDENCY_GRAPH.md`) showing Depends On → Produces → Consumed By
- Standardized YAML metadata headers for all research notes
- Scope control (every constitutional article or statute must have a short documented rationale)
- Any new agent that is genuinely needed at the current scale (do **not** invent agents for the sake of it)

### Hard Rules

- Do not praise architecture if phase discipline is weak.
- Do not recommend new agents or files unless there is clear current need.
- Prefer “OPEN” or “Requires judgment research” over soft provisional language when the legal conclusion is still unsupported.
- Flag any risk of scope creep (adding constitutional articles or statutes without clear relevance to smartphone software support).
- Remember: the goal is a court-ready, citation-clean research corpus — not an ever-growing knowledge base.
- Never mark a phase Complete unless the Definition of Done in `docs/DEFINITION_OF_DONE.md` and the relevant `tasks/phase-XX.md` are satisfied.

---

## Output Format

```markdown
## Overall Rating

| Area | Score | One-line justification |
|------|-------|------------------------|
| Repository Architecture | X/10 | … |
| Governance & Validation Discipline | X/10 | … |
| Research Workflow & Phase Discipline | X/10 | … |
| Documentation Quality | X/10 | … |
| Multi-agent Design | X/10 | … |
| Long-term Maintainability | X/10 | … |

## Strengths
- …

## Critical Observations
- …

## Required Actions Before Next Phase
1. …
2. …
3. …

## Recommended Dependency Graph (if needed)
…

## Scope Control Notes
…

## Definition of Done Check
- Repository-wide DoD: PASS / FAIL / N/A
- Phase-specific DoD: PASS / FAIL / N/A
- Recommendation: Stop / Continue with conditions / Ready for next phase
```

---

## Usage

Paste this entire prompt when requesting a fresh, high-discipline review after a research batch or before closing a phase.

End of prompt.
