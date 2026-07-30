# Master Prompt — Placeholder (Not Activated)

**Status:** `PLACEHOLDER ONLY`  
**Phase:** 0 — Foundation  
**Do not treat this file as an executable system prompt yet.**

---

## 1. Purpose of This File

This document reserves the location and design intent for the **Master Orchestration Prompt** that will later drive the multi-agent autonomous research system described in [`AGENTS.md`](AGENTS.md).

Per Phase 0 instructions:

- **Do NOT** create the final master prompt.  
- **Do NOT** begin autonomous legal research from this file.  
- **Do** describe how the autonomous system will operate when activated.

---

## 2. Intended Future Role

When activated (target: Phase 10, with drafts from Phase 1+), the Master Prompt will:

1. Instantiate the **Chief Architect** as the root coordinator.  
2. Dispatch work to specialised agents (Constitution, Statute, Judgments, OEM, Cyber, Environment, etc.).  
3. Enforce [`VALIDATION.md`](VALIDATION.md) as hard constraints on every output.  
4. Update [`TASKS.md`](TASKS.md) checkboxes via controlled commits.  
5. Refuse any request to invent citations, judgments, or statutes.  
6. Gate promotion of content into `litigation/` behind explicit human approval tokens.  
7. Write run manifests to `logs/` and artefacts to `output/`.

---

## 3. Operating Model (Design Only)

```text
┌─────────────────────────────────────────────┐
│             HUMAN GOVERNANCE                 │
│  (Counsel · Maintainer · Project Manager)    │
└─────────────────────┬───────────────────────┘
                      │ approval / scope
                      v
┌─────────────────────────────────────────────┐
│         MASTER ORCHESTRATOR (future)         │
│  - Reads ROADMAP + TASKS + VALIDATION        │
│  - Plans sprint batch                        │
│  - Assigns agents                            │
└───────────┬─────────────────────┬───────────┘
            │                     │
            v                     v
   Research Agents          Validation Agents
   (domain packs)           (citation · QA)
            │                     │
            └──────────┬──────────┘
                       v
              Git Manager Agent
           (branch · PR · changelog)
```

### 3.1 Cycle (planned)

1. **Select** next open tasks from `TASKS.md` within active phase.  
2. **Brief** domain agent with inputs path + output path + validation rules.  
3. **Produce** draft memo in `research/...` with status `PROVISIONAL`.  
4. **Validate** via Citation Validation + QA agents.  
5. **Merge** only if gates pass; else return with defect list.  
6. **Log** duration, sources accessed, residual `OPEN` questions.

### 3.2 Hard Stops (planned)

The orchestrator must abort or escalate if:

- A task requires a citation that cannot be found.  
- An agent proposes a case name without a reporter citation.  
- Litigation drafting is requested before Phase 9 approval.  
- User request conflicts with `CODE_OF_CONDUCT.md` or illegal activity.

---

## 4. Activation Preconditions

The final Master Prompt must **not** be written or enabled until:

| # | Precondition | Phase |
|---|--------------|-------|
| 1 | Templates exist for all research note types | 1 |
| 2 | Validation schemas exist | 1 |
| 3 | Agent prompt library stubs in `prompts/` | 1–2 |
| 4 | At least one human-reviewed sample memo per major domain | 2–7 |
| 5 | Incident response path tested with a synthetic hallucination drill | 10 |
| 6 | Project Manager records activation in `CHANGELOG.md` | 10 |

---

## 5. What Will Be Contained in the Final Master Prompt (Outline Only)

> The following is an **outline**, not the prompt text.

1. Identity & mission statement of the orchestrator  
2. Incorporation by reference: VALIDATION, SPEC, ROADMAP, AGENTS  
3. Tool-use policy (read/write paths allowed)  
4. Agent dispatch contracts (JSON or YAML task envelopes)  
5. Output format contracts  
6. Citation and anti-hallucination constitution (full text or link)  
7. Escalation matrix to humans  
8. Logging schema  
9. Explicit prohibition list (fabricated law, exploits, personal data abuse)  
10. Shutdown / safe-completion criteria  

---

## 6. Interim Human Procedure (Until Activation)

Until the Master Prompt is finalised:

- Humans (or ad-hoc agent sessions) execute tasks **phase by phase**.  
- Each session must open by re-reading `VALIDATION.md` and the relevant `AGENTS.md` section.  
- Session prompts should be stored under `prompts/sessions/` (create when first used).  
- No session may mark a citation `VERIFIED` without source check.

---

## 7. Placeholder Token

```text
MASTER_PROMPT_STATUS=INACTIVE
MASTER_PROMPT_VERSION=null
NEXT_ACTION=Complete Phase 1 templates before drafting final orchestrator prompt
```

---

## 8. Change Log Pointer

Activation and subsequent versions of the true Master Prompt will be recorded in [`CHANGELOG.md`](CHANGELOG.md).

---

*End of Master Prompt placeholder*
