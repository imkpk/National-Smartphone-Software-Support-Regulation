# Tasks directory

Granular checkbox tasks for **National-Smartphone-Software-Support-Regulation**, split by phase to reduce merge conflicts and improve navigation.

## Layout

| File | Phase |
|------|-------|
| [`phase-00.md`](phase-00.md) | Repository foundation |
| [`phase-01.md`](phase-01.md) | Research infrastructure |
| [`phase-02.md`](phase-02.md) | Constitutional & statutory map |
| [`phase-03.md`](phase-03.md) | Judgments corpus |
| [`phase-04.md`](phase-04.md) | Government policy & institutions |
| [`phase-05.md`](phase-05.md) | Manufacturers & technical |
| [`phase-06.md`](phase-06.md) | Cybersecurity, environment, economics |
| [`phase-07.md`](phase-07.md) | Comparative international law |
| [`phase-08.md`](phase-08.md) | Evidence pack & annexures |
| [`phase-09.md`](phase-09.md) | Litigation drafting (hard gate) |
| [`phase-10.md`](phase-10.md) | Hardening, automation, cross-cutting, meta |

**Dashboard:** [`../TASKS.md`](../TASKS.md)

## Rules

1. Prefer primary sources; never invent citations ([`VALIDATION.md`](../VALIDATION.md), [`CITATION_POLICY.md`](../CITATION_POLICY.md)).  
2. One logical unit of work per checkbox when possible.  
3. Do not start Phase 9 without recorded approval.  
4. Forum (Art. 32 vs Art. 226) is not pre-judged.  
5. **Phase completion** requires [`docs/DEFINITION_OF_DONE.md`](../docs/DEFINITION_OF_DONE.md) **and** the **Definition of Done** section at the bottom of each `phase-XX.md`. Files existing ≠ phase done.

## Tooling

```bash
python scripts/list_open_tasks.py
python scripts/list_open_tasks.py --all
```

---

*Architecture cleanup — tasks split*
