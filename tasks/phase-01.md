# Phase 01 Tasks

**Project:** National-Smartphone-Software-Support-Regulation  
**Parent dashboard:** [../TASKS.md](../TASKS.md)  
**Rules:** [../VALIDATION.md](../VALIDATION.md) · [../CITATION_POLICY.md](../CITATION_POLICY.md) · [../docs/DEFINITION_OF_DONE.md](../docs/DEFINITION_OF_DONE.md) · [../docs/DEFINITION_OF_DONE.md](../docs/DEFINITION_OF_DONE.md)  
**Progress:** 55 done · 0 open · 55 total  

> Check boxes only when complete and validation rules are satisfied.

---

## Phase 1 — Research Infrastructure

**Status:** Complete (framework). Substantive legal research not started.

### Templates

- [x] **T031** Draft template: constitutional provision note
- [x] **T032** Draft template: statute/section note
- [x] **T033** Draft template: judgment brief
- [x] **T034** Draft template: government policy memo
- [x] **T035** Draft template: OEM policy capture
- [x] **T036** Draft template: cybersecurity note
- [x] **T037** Draft template: environment/e-waste note
- [x] **T038** Draft template: comparative law jurisdiction note
- [x] **T039** Draft template: economics model note
- [x] **T040** Draft template: technical explainer
- [x] **T041** Draft template: consumer-law issue note
- [x] **T042** Draft template: evidence table schema
- [x] **T043** Draft template: timeline event schema
- [x] **T044** Draft template: annexure index row
- [x] **T045** Draft template: RTI application
- [x] **T046** Draft template: validation report
- [x] **T047** Draft template: litigation assertion→source map
- [x] **T048** Add YAML front-matter convention for research notes
- [x] **T049** Document status tag vocabulary in templates/README
- [x] **T050** Add sample filled template (synthetic, non-legal) for style only

### Schemas & validation assets

- [x] **T051** Create validation/citation-schema.json (or YAML)
- [x] **T052** Create validation/source-tier-definitions.md
- [x] **T053** Create validation/research-gate-checklist.md
- [x] **T054** Create validation/litigation-gate-checklist.md
- [x] **T055** Create validation/banned-patterns.md (hallucination red flags)
- [x] **T056** Create scripts/check_structure.py
- [x] **T057** Create scripts/list_open_tasks.py (optional parser for TASKS.md)
- [x] **T058** Create scripts/new_research_note.py scaffolding helper
- [x] **T059** Add scripts/README.md usage docs
- [x] **T060** Add requirements.txt or pyproject.toml stub
- [x] **T061** Add .env.example if APIs later needed (no secrets)
- [x] **T062** Create logs/.gitkeep policy note in docs/logging.md
- [x] **T063** Create docs/repository-tour.md
- [x] **T064** Create docs/how-to-cite.md
- [x] **T065** Create docs/phase-gates.md
- [x] **T066** Create prompts/README.md for agent prompt library
- [x] **T067** Add stub prompts for each core agent under prompts/agents/
- [x] **T068** Create automation/README.md describing future orchestrator
- [x] **T069** Wire CI structure-check to real script when ready
- [x] **T070** Document contribution example PR in docs/examples.md

### Indexes

- [x] **T071** Add research/README.md domain index
- [x] **T072** Add research/constitution/README.md
- [x] **T073** Add research/statutes/README.md
- [x] **T074** Add research/judgments/README.md
- [x] **T075** Add research/government/README.md
- [x] **T076** Add research/manufacturers/README.md
- [x] **T077** Add research/cybersecurity/README.md
- [x] **T078** Add research/environment/README.md
- [x] **T079** Add research/international/README.md
- [x] **T080** Add research/economics/README.md
- [x] **T081** Add research/technical/README.md
- [x] **T082** Add research/consumer-law/README.md
- [x] **T083** Add evidence/README.md
- [x] **T084** Add litigation/README.md with NOT STARTED banner
- [x] **T085** Add docs/glossary.md (empty structure)

---
## Definition of Done

**Inherits:** [docs/DEFINITION_OF_DONE.md](../docs/DEFINITION_OF_DONE.md) (repository-wide, mandatory).

Phase 1 is complete only when **all** of the following are true (in addition to repository-wide DoD):

- [x] Research templates exist and are indexed under 	emplates/.
- [x] Validation assets exist under alidation/ and align with VALIDATION.md.
- [x] Domain indexes exist under 
esearch/* (including forum path).
- [x] Structure check script passes (scripts/check_structure.py).
- [x] Agent model and orchestration docs exist (AGENTS, MASTER_PROMPT).
- [x] Litigation remains gated (no premature PIL content required for Phase 1).
- [x] Task tracking split or equivalent dashboard usable for later phases.
- [ ] **Completion approval:** PM/maintainer records Phase 1 complete in CHANGELOG/logs without starting Phase 2 automatically.

**Advancement:** Phase 2 (or other unlocked research phases per ROADMAP) may begin only after Phase 1 DoD is satisfied.
