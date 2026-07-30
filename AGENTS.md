# Multi-Agent Architecture

**Project:** National-Smartphone-Software-Support-Regulation  
**Document status:** Active  
**Runtime model:** **Seven core agents** (human and/or supervised LLM)  
**Extensibility:** Domain specialisations are **skill packs**, not separate permanent agents  

All agents are bound by [`VALIDATION.md`](VALIDATION.md) (validation SoT) and [`CITATION_POLICY.md`](CITATION_POLICY.md) (citation SoT).

---

## 1. Design principle

| Prefer | Avoid |
|--------|--------|
| Few runtime roles with clear handoffs | 18 concurrent “agents” for a small team |
| Domain parameter on Research Agent | One permanent agent per research folder |
| Citation Validation as a **separate pass** | Self-certifying research without review |

```text
                 ┌─────────────────────────┐
                 │ 1. Project Manager      │
                 │    (orchestrates)       │
                 └───────────┬─────────────┘
                             │
                 ┌───────────v─────────────┐
                 │ 2. Research Agent       │
                 │    (domain=…)           │
                 └───────────┬─────────────┘
                             │
                 ┌───────────v─────────────┐
                 │ 3. Citation Validation  │
                 └───────────┬─────────────┘
                             │
          ┌──────────────────┼──────────────────┐
          v                  v                  v
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │ 4. Evidence    │ │ 5. Drafting    │ │ 6. QA          │
 │    Agent       │ │    (Phase 9+)  │ │    Agent       │
 └────────────────┘ └────────────────┘ └────────┬───────┘
                                                 │
                                      ┌──────────v──────────┐
                                      │ 7. Git / Release    │
                                      └─────────────────────┘
```

---

## 2. Global rules (all agents)

1. Never invent judgments, statutes, notifications, quotations, or statistics.  
2. Prefer primary / official sources ([`CITATION_POLICY.md`](CITATION_POLICY.md)).  
3. Label claims: FACT | LAW | ANALYSIS | NORM | OPEN ([`VALIDATION.md`](VALIDATION.md)).  
4. Write only to assigned paths.  
5. Do not populate `litigation/` without Phase 9 approval.  
6. Forum (Art. 32 vs Art. 226) is **not pre-judged**.  
7. On conflict between speed and accuracy, choose accuracy.  
8. Update the correct `tasks/phase-XX.md` checkbox when work completes.

---

## 3. Core agents (runtime)

### 3.1 Project Manager

| Field | Content |
|-------|---------|
| **Mission** | Deliver phases with clear priorities, phase gates, and honest progress. |
| **Responsibilities** | Own `TASKS.md` dashboard + `tasks/*` hygiene; enforce phase exit criteria; approve Phase 9 start in CHANGELOG; refuse out-of-phase litigation; coordinate humans. |
| **Inputs** | ROADMAP, TASKS dashboard, validation incidents. |
| **Outputs** | Sprint priorities, phase status updates, release notes coordination. |
| **Handoffs** | → Research Agent (batches); → Drafting (Phase 9 only); → Git/Release (merge/tag). |
| **Prompt stub** | `prompts/agents/project_manager.md` |

*Also covers light “orchestrator” duties described in `MASTER_PROMPT.md`.*

---

### 3.2 Research Agent (domain-parameterised)

| Field | Content |
|-------|---------|
| **Mission** | Produce citable research notes in the correct `research/<domain>/` folder. |
| **Responsibilities** | Use the matching template; gather primary sources; separate FACT/LAW/ANALYSIS; list OPEN questions; never invent authorities. |
| **Domain parameter** | One of: `constitution`, `statutes`, `judgments`, `government`, `manufacturers`, `cybersecurity`, `environment`, `international`, `economics`, `technical`, `consumer-law`, `forum`. |
| **Inputs** | Template; official sources; assigned task IDs from `tasks/phase-XX.md`. |
| **Outputs** | Notes under `research/<domain>/`. |
| **Handoffs** | → Citation Validation (required); → Evidence Agent (when facts are stable). |
| **Prompt stubs** | Prefer domain stubs under `prompts/agents/` as **skill packs** (e.g. `constitution.md`, `statute.md`) while acting as this single runtime role. |

---

### 3.3 Citation Validation Agent

| Field | Content |
|-------|---------|
| **Mission** | Fail closed on missing, weak, or fabricated citations. |
| **Responsibilities** | Apply `VALIDATION.md` and `CITATION_POLICY.md`; run research-gate checklist; quarantine UNVERIFIED claims used as authority. |
| **Inputs** | Any PR or draft under `research/` or `litigation/`. |
| **Outputs** | Pass/fail validation report; required fixes. |
| **Handoffs** | → Research Agent (fixes); → QA; → Git/Release (block merge on BLOCKER). |
| **Prompt stub** | `prompts/agents/citation_validation.md` |

---

### 3.4 Evidence Agent

| Field | Content |
|-------|---------|
| **Mission** | Turn **validated** research into annexure-ready tables, timelines, and captures. |
| **Responsibilities** | `evidence/**` artefacts with source columns; no decorative charts without provenance. |
| **Inputs** | Citation-validated research notes. |
| **Outputs** | `evidence/tables|timelines|charts|annexures/`. |
| **Handoffs** | → Drafting (Phase 9); → QA. |
| **Prompt stub** | `prompts/agents/evidence.md` |

---

### 3.5 Drafting Agent

| Field | Content |
|-------|---------|
| **Mission** | Court-oriented drafts **only** after Phase 9 approval. |
| **Responsibilities** | Synopsis, PIL body, affidavit, prayers; `DRAFT — NOT FOR FILING` banner; assertion→source map. |
| **Inputs** | Validated research pack; evidence map; PM approval. |
| **Outputs** | `litigation/**`. |
| **Handoffs** | → Citation Validation; → QA; → human counsel. |
| **Prompt stub** | `prompts/agents/drafting.md` |

---

### 3.6 Quality Assurance Agent

| Field | Content |
|-------|---------|
| **Mission** | Holistic quality: structure, clarity, consistency, phase compliance, tone. |
| **Responsibilities** | Editorial review; README/progress honesty; ensure FACT/LAW/ANALYSIS separation; release readiness with PM. |
| **Inputs** | Near-final artefacts; citation validation results. |
| **Outputs** | QA checklist results; polish requests. |
| **Rules** | Cannot override citation BLOCKERs. |
| **Handoffs** | → PM; → Git/Release. |
| **Prompt stub** | `prompts/agents/quality_assurance.md` |

---

### 3.7 Git / Release Agent

| Field | Content |
|-------|---------|
| **Mission** | Repository integrity, history, and release discipline. |
| **Responsibilities** | Branches, PRs, tags, secrets hygiene, CHANGELOG commits, remote sync. Includes light **platform/structure** stewardship (paths, `.gitignore`) formerly split across “Chief Architect” and “Git Manager.” |
| **Inputs** | Approved PRs; release requests. |
| **Outputs** | Clean `main`; version tags. |
| **Handoffs** | → All agents via PR feedback. |
| **Prompt stubs** | `prompts/agents/git_manager.md` (primary); architecture notes may still reference historical `chief_architect.md` as a skill pack. |

---

## 4. Extensibility (not extra permanent agents)

Domain depth is expressed as **skill packs** (prompt stubs + templates), not new runtime agents:

| Skill pack (examples) | Maps to Research Agent domain= |
|----------------------|--------------------------------|
| Constitution, statute, judgments, government, OEM, cyber, environment, economics, technical, consumer-law, forum | corresponding `domain` value |
| RTI drafting | Research or Evidence with `templates/rti_application.md` |
| Red-team citation holes | Citation Validation mode (no invented sources) |

Optional historical / detailed matrices may live in docs later; **do not re-expand the core seven** without an ADR and cleanup review.

Legacy prompt files under `prompts/agents/` (e.g. `supreme_court.md`, `high_court.md`) remain as **skill packs** for Research Agent specialisation. They are **not** additional always-on agents.

---

## 5. Handoff protocol

### 5.1 Task envelope

```yaml
task_id: "T086"
phase: 2
agent: "Research Agent"
domain: "constitution"
prompt_skill: "prompts/agents/constitution.md"
template: "templates/constitutional_provision_note.md"
output_path: "research/constitution/<slug>.md"
constraints:
  - "VALIDATION.md"
  - "CITATION_POLICY.md"
```

### 5.2 Definition of done (research)

1. File in correct `research/<domain>/` folder  
2. Status tag set  
3. Sources complete per CITATION_POLICY  
4. OPEN questions listed  
5. Citation Validation not blocked  
6. Checkbox updated in `tasks/phase-XX.md`  

---

## 6. Conflict resolution

| Conflict | Resolver |
|----------|----------|
| Priority / phase gates | Project Manager |
| Citation validity | Citation Validation Agent |
| Editorial / structure quality | QA Agent |
| Path / git policy | Git / Release Agent |
| Doctrinal disagreement after validation | Human counsel |

---

## 7. Activation notes

- A single human may wear multiple hats; **Citation Validation must remain a separate pass**.  
- Do not run “18 agents” in parallel for its own sake.  
- Master orchestration: [`MASTER_PROMPT.md`](MASTER_PROMPT.md).

---

*Core seven agents — architecture cleanup 2026-07-30*
