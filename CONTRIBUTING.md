# Contributing

Thank you for interest in **National-Smartphone-Software-Support-Regulation**.

This project prioritises **citation integrity** over speed. Contributions that invent legal authorities will be rejected.

---

## 1. Before You Start

1. Read [`docs/START_HERE.md`](docs/START_HERE.md)  
2. Read [`VALIDATION.md`](VALIDATION.md) — **mandatory** (validation SoT)  
3. Read [`CITATION_POLICY.md`](CITATION_POLICY.md) — **mandatory** for any sourced claim  
4. Read [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)  
5. Skim [`ROADMAP.md`](ROADMAP.md) and claim tasks via [`TASKS.md`](TASKS.md) → [`tasks/`](tasks/)  
6. Optionally read [`AGENTS.md`](AGENTS.md) (seven core agents) if using agent workflows  

## 2. Ways to Contribute

| Type | Where | Notes |
|------|-------|-------|
| Research notes | `research/**` | Primary sources preferred |
| Evidence tables/charts | `evidence/**` | Include data sources |
| Templates | `templates/` | Improve repeatability |
| Scripts / validators | `scripts/`, `validation/` | Tests appreciated |
| Documentation | `docs/`, root markdown | Clarity fixes welcome |
| Litigation drafts | `litigation/**` | **Only after Phase 9 gate**; counsel review required |

## 3. Workflow

1. Fork (or branch from `main`).  
2. Create a focused branch: `research/statutes-cpa`, `fix/typo-readme`, etc.  
3. Make minimal, reviewable commits.  
4. Ensure new claims are cited per VALIDATION.md and CITATION_POLICY.md.  
5. Open a Pull Request using the PR template.  
6. Respond to Citation Validation / QA review comments.

## 3A. Definition of Done (required for merge when applicable)

Pull Requests must satisfy the **applicable Definition of Done** before they may be merged when they:

- Complete a phase (or claim phase completion); or  
- Deliver the bulk of a phase’s required artefacts; or  
- Touch `litigation/` (Phase 9 hard gate + litigation DoD).

| Gate | Document |
|------|----------|
| Document / claim quality | [`VALIDATION.md`](VALIDATION.md) |
| Citation format | [`CITATION_POLICY.md`](CITATION_POLICY.md) |
| Phase completion | [`docs/DEFINITION_OF_DONE.md`](docs/DEFINITION_OF_DONE.md) + **Definition of Done** in `tasks/phase-XX.md` |

**Rules:**

1. A phase is not complete merely because files exist.  
2. Maintainers should not merge phase-completion PRs that skip DoD criteria.  
3. Small fixes (typos, dead links) still require VALIDATION where claims are involved, but need not close an entire phase DoD.  
4. Never invent legal authorities to “finish” a DoD checkbox.

## 4. Research Note Minimum Standard

Every new research file should include:

- Title and domain  
- Status (`PROVISIONAL` / `VERIFIED` / etc.)  
- Last updated date  
- Separated **Facts / Law / Analysis / Open Questions / Sources**  
- Citations for legal claims  

Use templates from `templates/` once available (Phase 1).

## 5. What Will Be Rejected

- Fabricated case law or statutes  
- Unsourced statistics presented as fact  
- Scraped personal data or sealed court documents  
- Offensive security / exploit code  
- Bulk uncited LLM dumps  
- “Complete PIL” submissions that bypass validation gates  

## 6. Attribution

Contributors are acknowledged via git history. Significant contributors may be listed in a future `AUTHORS` or `docs/credits.md` file.

## 7. License

By contributing, you agree that your contributions are licensed under the repository [`LICENSE`](LICENSE) (MIT), subject to the content notice regarding official legal texts.

## 8. Questions

Open a GitHub Discussion or Issue with label `question`. Do not request legal advice for personal cases in this repository.

---

*Quality over quantity. Cite or omit.*
