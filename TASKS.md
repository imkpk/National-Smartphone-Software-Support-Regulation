# Tasks — Dashboard

**Project:** National-Smartphone-Software-Support-Regulation  
**Purpose:** Index and status only. Granular checkboxes live under [`tasks/`](tasks/).  
**Rules:** [`VALIDATION.md`](VALIDATION.md) · [`CITATION_POLICY.md`](CITATION_POLICY.md)

> Check a box in the phase file only when the work is complete and validation rules are satisfied.  
> **Phase 4 Complete (v0.6.0).** Phase 5 **in progress** (WS1–WS5 complete; WS6 audit → v0.6.6). See `PHASE_05_SPECIFICATION.md` · `REPOSITORY_OS.md`.

---

## Quick links

| Resource | Link |
|----------|------|
| Start here (5 minutes) | [`docs/START_HERE.md`](docs/START_HERE.md) |
| Phase task files | [`tasks/README.md`](tasks/README.md) |
| Roadmap | [`ROADMAP.md`](ROADMAP.md) |
| Validation (SoT) | [`VALIDATION.md`](VALIDATION.md) |
| Citation (SoT) | [`CITATION_POLICY.md`](CITATION_POLICY.md) |

---

## Phase status

| Phase | File | Status | Done | Open | Total |
|------:|------|--------|------|-----:|-----:|------:|
| 0 | [`tasks/phase-00.md`](tasks/phase-00.md) | Complete | 30 | 0 | 30 |
| 1 | [`tasks/phase-01.md`](tasks/phase-01.md) | Complete (framework) | 55 | 0 | 55 |
| 2 | [`tasks/phase-02.md`](tasks/phase-02.md) | **Nearly complete** (statutes done; Art. 12/47 residual) | 47 | 2 | 49 |
| 3 | [`tasks/phase-03.md`](tasks/phase-03.md) | **Complete** | 34 | 0 | 34 |
| 4 | [`tasks/phase-04.md`](tasks/phase-04.md) | **Complete** | 16 | 8 | 24 |
| 5 | [`tasks/phase-05.md`](tasks/phase-05.md) | **In progress** (WS1–WS6 audit complete) | 57 | 11 | 68 |
| 6 | [`tasks/phase-06.md`](tasks/phase-06.md) | Pending | 0 | 24 | 24 |
| 7 | [`tasks/phase-07.md`](tasks/phase-07.md) | Pending | 0 | 32 | 32 |
| 8 | [`tasks/phase-08.md`](tasks/phase-08.md) | Pending | 0 | 15 | 15 |
| 9 | [`tasks/phase-09.md`](tasks/phase-09.md) | Pending (hard gate) | 0 | 24 | 24 |
| 10 | [`tasks/phase-10.md`](tasks/phase-10.md) | Pending (+ cross-cutting) | 0 | 33 | 33 |
| | | **Totals** | **239** | **149** | **388** |

---

## What to work on next

1. Do **not** start Phase 9 without PM approval in `CHANGELOG.md`.  
2. **Phase 3 Complete** — `PHASE_03_COMPLETION_REPORT.md`.  
3. **Phase 4 Complete** — `PHASE_04_COMPLETION_REPORT.md` (v0.6.0).  
4. **Phase 5 WS1–WS6** — manufacturers + Android + hardware + comparative + gap + repository audit (v0.6.1–0.6.6). Further Phase 5 WS — **not auto-started**.  
5. Phase 2 residual: Art. 12 optional / Art. 47 remove-from-scope.  
6. Forum remains **open**.  
7. List open tasks:

```bash
python scripts/list_open_tasks.py
```

---

## Maintenance

- Edit checkboxes **only** in `tasks/phase-XX.md`.  
- Update this dashboard’s counts when a phase batch completes (or re-run a count when tooling allows).  
- Historical Phase 0–1 completed tasks remain in their phase files for audit.

---

*Dashboard — architecture cleanup 2026-07-30*
