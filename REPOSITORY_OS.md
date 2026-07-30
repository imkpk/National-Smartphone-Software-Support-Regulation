# Repository Operating System

**Status:** Permanent orchestration constitution  
**Version:** 1.0.0  
**Last updated:** 2026-07-31  
**Stability:** **Do not rewrite casually.** Phase-specific objectives live in `PHASE_XX_SPECIFICATION.md` files, not here.

**Bound by:** [`VALIDATION.md`](VALIDATION.md) · [`CITATION_POLICY.md`](CITATION_POLICY.md) · [`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md) · [`MASTER_PROMPT.md`](MASTER_PROMPT.md)

---

## 0. Identity

This file is the **stable operating system** for autonomous and supervised agents working on  
`National-Smartphone-Software-Support-Regulation`.

It does **not** authorise inventing law, skipping validation, advocacy, litigation drafting before Phase 9 gates, or architecture changes outside explicit human instruction.

**Repository state always overrides previous chat prompts.**

---

## 1. Boot sequence (every iteration)

1. `git checkout main && git pull` (or equivalent sync to latest main).  
2. Read: `README.md`, `CHANGELOG.md`, `TASKS.md`, `ROADMAP.md`, active `PHASE_XX_SPECIFICATION.md` (if any), `VALIDATION.md`, `research/`, `orchestration/`.  
3. Determine: version · phase · completed workstreams · remaining work · defects · negative findings.  
4. Run **Optimistic Resume Engine** (§3).  
5. Run **Dependency Engine** (§4).  
6. Run **Self-Healing Documentation Engine** (§5) if documentation drift found.  
7. Select **exactly one** unfinished workstream (or stop if phase complete / blocked).  
8. Plan → research (if needed) → validate → knowledge graph update → documentation → **Repository Gate++** (§7).  
9. Open **one PR**. **STOP.** Wait for human merge. Never auto-start the next workstream after PR open without merge confirmation on main.

---

## 2. Agents (roles)

| Agent | Responsibility |
|-------|----------------|
| Repository State | Latest main inventory, version, health |
| Planning | One workstream plan, prerequisites, expected outputs |
| Research | Official sources only; no advocacy/litigation |
| Repository Relevance | §6 — gate before any new entity document |
| Citation | Official locators, access dates, tiers |
| Validation | VALIDATION.md + workstream validation report |
| Documentation | README / TASKS / CHANGELOG / indexes only |
| Knowledge Graph | §8 — indexes, cross-refs, no orphans |
| Repository Gate++ | §7 — PASS / PASS WITH MINOR ISSUES / FAIL |
| Audit | Phase audit artefacts only when phase-spec schedules them |
| Completion | Phase close package only when authorised by phase-spec + audit |
| Iteration Planner | Next workstream name only after merge |

No agent may exceed its role. Research agents do not rewrite completed validated workstreams.

---

## 3. Optimistic Resume Engine

**Before starting any workstream:**

| Check | Action |
|-------|--------|
| Expected outputs all exist + validation PASS | Mark workstream complete; update `orchestration/STATE_REPORT.md`; **select next** unfinished workstream (do not re-research) |
| Outputs exist, validation FAIL | Generate **only** missing/failing artefacts |
| Outputs partial | Resume **only** missing work |
| Repository ahead of prompt | **Repository wins** |

**Never** repeat completed work · overwrite validated research · duplicate research.

---

## 4. Dependency Engine

Every workstream (in phase specification) declares:

- Prerequisites  
- Required repository state  
- Expected outputs  
- Validation rules  
- Repository gate  
- Completion rules  

**Verify dependencies before execution.** If prerequisites missing → **STOP**.  
Never skip dependencies · never reorder workstreams · never execute two workstreams in one PR.

---

## 5. Self-Healing Documentation Engine

Each iteration, compare **documentation only** against reality:

- README · TASKS · CHANGELOG · research indexes · phase task files · version badges · navigation links · folder structure notes  

If inconsistent → **repair documentation automatically**.

**Never** rewrite research notes, legal analysis, or evidence under this engine.  
Research corrections require a **dedicated workstream** or explicit defect PR.

---

## 6. Repository Relevance Agent (mandatory)

**Before researching any entity** (person, institution, document, programme, policy, standard, committee, consultation, body, scheme):

Ask: **Why is this entity in the repository?**

Every **new** research document MUST include a section:

### Repository Relevance

Select one or more tags:

| Tag |
|-----|
| Statutory Authority |
| Regulatory Authority |
| Policy Maker |
| Technical Standard |
| Consumer Protection |
| Cyber Security |
| Telecommunications |
| Digital Governance |
| Electronics Manufacturing |
| Environmental Responsibility |
| Electronic Waste |
| Administrative Responsibility |
| Inter-Ministerial Coordination |
| International Comparative Context |
| Repository Cross Reference |
| Peripheral Stakeholder |
| Not Relevant |

**Peripheral Stakeholder** requires: why included · why not primary · which repo docs reference it.

**Not Relevant** → **STOP**. Do not create the document. Log exclusion in [`research/exclusions/not-relevant-log.md`](research/exclusions/not-relevant-log.md).

**Grandfathering:** Research notes created before REPOSITORY_OS v1.0 may lack this section until a dedicated retrofit workstream. **All new notes (Phase 4 WS3 onward)** must include it.

---

## 7. Repository Gate++

### Verdicts

| Verdict | When |
|---------|------|
| **PASS** | All critical checks green |
| **PASS WITH MINOR ISSUES** | Only administrative issues |
| **FAIL** | Any Critical failure → **STOP**, no complete claim |

### Check classes

Repository structure · folder integrity · internal links · version · naming · cross-references · coverage · validation · citation quality · duplicate research · negative findings · documentation · statistics · research indexes · phase status · dependency graph · analytical artefacts · **repository relevance** · self-healing status · optimistic resume state · knowledge graph reachability  

**Critical examples:** invented law · empty required files · missing validation report · two workstreams in one PR · architecture change without authorisation · missing official sources for LAW/POLICY claims.

---

## 8. Repository Knowledge Graph

When a document is added or completed, update all that apply:

- Domain `README.md`  
- `research/README.md`  
- Coverage / source / citation / validation reports  
- Negative findings (if applicable)  
- Workstream report · phase report  
- TASKS / CHANGELOG / root README progress  
- Cross-references  

**No orphan documents.** Every research document must be reachable from at least one index.

---

## 9. Claim classification

Substantive statements use:

`FACT` · `LAW` · `POLICY` · `PROGRAMME` · `GUIDANCE` · `STANDARD` · `ANALYSIS` · `NORM` · `OPEN` · `UNKNOWN`

Never mix categories in one sentence without labels.  
Distinguish: binding · non-binding · draft · consultation · guidance · recommendation.

---

## 10. Official sources only

Government of India · MeitY · DoT · CERT-In · BIS · CCPA · CPCB · NITI Aayog · MyGov · PIB · Gazette · Parliament · India Code · official consultations/standards/reports/FAQs/notifications/policy PDFs.

Reject blogs, media as sole authority, opinion, unverified AI summaries.

---

## 11. Document format (minimum)

New research documents should include:

1. Purpose  
2. Scope  
3. **Repository Relevance** (§6)  
4. Official Sources  
5. Repository Cross References  
6. Findings  
7. Negative Findings (if applicable)  
8. Limitations  
9. Open Questions  
10. Research Confidence  

Workstream packages also require: Coverage Matrix · Source Report · Citation Report · Validation Report · Negative Finding (if applicable) · Workstream Report.

---

## 12. Documentation update rules

Update only: README · CHANGELOG · TASKS · relevant `tasks/phase-XX.md` · research indexes · orchestration state.  
Never rewrite previous phase research unless a documented defect workstream.

---

## 13. Autonomous scheduler (supervised)

```text
while phase != Complete:
  refresh main
  optimistic resume
  dependency check
  select ONE unfinished workstream
  plan → research (if needed) → validate → knowledge graph → docs → Gate++
  open PR
  STOP  # wait for human merge
```

Human merge is mandatory between iterations.  
Never begin next phase automatically after phase complete.

---

## 14. Stop conditions

Immediately **STOP** if: validation fails · Gate++ FAIL · official evidence unavailable · architecture/governance modification requested without authorisation · scope creep · multiple workstreams attempted · litigation requested before Phase 9 gate.

---

## 15. Phase specifications

| File | Role |
|------|------|
| **This file (`REPOSITORY_OS.md`)** | Stable OS — engines, agents, gates |
| `PHASE_XX_SPECIFICATION.md` | Phase objectives, workstreams, deliverables, exclusions, completion criteria only |

Do **not** fork OS rules into per-phase master prompts.

---

## 16. Relationship to other SoTs

| Concern | Authority |
|---------|-----------|
| Claim integrity / anti-hallucination | `VALIDATION.md` |
| Citation formats | `CITATION_POLICY.md` |
| Phase completion ceremony | `docs/DEFINITION_OF_DONE.md` + phase-spec |
| Agent roster (domain) | `AGENTS.md` |
| Historical orchestration contract | `MASTER_PROMPT.md` (defers to this file for engines) |

---

*REPOSITORY_OS v1.0.0 — permanent*
