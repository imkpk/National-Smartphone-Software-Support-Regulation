# Finish Phase 5 WS1 packaging: Classification blocks + tasks status
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manu = ROOT / "research" / "manufacturers"

CLS = """
## Classification

**FACT / ANALYSIS** — Published manufacturer software/security lifecycle materials. **Not** Indian law; **not** recommendations.
"""

for p in sorted(manu.glob("*.md")):
    if p.name.startswith("MANUFACTURER") or p.name == "README.md":
        continue
    t = p.read_text(encoding="utf-8")
    if "## Classification" in t:
        print("skip cls", p.name)
        continue
    marker = "\n## 1."
    if marker not in t:
        print("no marker", p.name)
        continue
    t = t.replace(marker, "\n" + CLS + "\n## 1.", 1)
    p.write_text(t, encoding="utf-8")
    print("added cls", p.name)

nf = manu / "negative-finding-oem-unified-multi-year-matrix.md"
t = nf.read_text(encoding="utf-8")
if "## Official sources" not in t and "Official sources" not in t:
    block = """
## Official sources [FACT]

See per-brand notes in this folder and `MANUFACTURER_SOURCE_REPORT.md` (Google Support, Samsung Newsroom/Security, Apple Support, Xiaomi Trust Zone, Motorola support, and other OEM domains listed therein).

## Negative findings [FACT]

See sections 3–4 below (no industry-wide multi-year matrix; uneven official documentation depth).

## Cross references

- Per-brand notes in `research/manufacturers/`
- `MANUFACTURER_COVERAGE_MATRIX.md` · `MANUFACTURER_COMPARISON_MATRIX.md` · `MANUFACTURER_LIFECYCLE_MATRIX.md`
- Phase 4 gap analysis (`research/phase4-gap-analysis/`) — government-side no multi-year legal floor
- `../../PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md`
"""
    t = t.replace("\n## 1.", "\n" + block + "\n## 1.", 1)
    nf.write_text(t, encoding="utf-8")
    print("patched negative finding")
else:
    print("negative finding sources ok")

# Update tasks/phase-05.md — mark WS1 OEM + matrix tasks complete
phase5 = ROOT / "tasks" / "phase-05.md"
text = phase5.read_text(encoding="utf-8")

# Tasks completed in WS1 (OEM notes + matrices; residual brands/technical left open)
done_ids = list(range(193, 238))  # T193–T237 incl. POCO under Xiaomi family note
done_ids += [247, 248, 249, 250, 251, 253]
# leave T238–T246 (iQOO/Tecno/Other residual), T252 PDF archive, T254–T260 technical

import re

def mark_done(m):
    tid = int(m.group(1))
    if tid in done_ids:
        return f"- [x] **T{tid}**"
    return m.group(0)

text2 = re.sub(r"- \[ \] \*\*T(\d+)\*\*", mark_done, text)

# Progress counts
done = len(re.findall(r"- \[x\] \*\*T\d+\*\*", text2))
open_n = len(re.findall(r"- \[ \] \*\*T\d+\*\*", text2))
total = done + open_n
text2 = re.sub(
    r"\*\*Progress:\*\*.*",
    f"**Progress:** {done} done · {open_n} open · {total} total  \n"
    f"**WS1 status:** Complete (OEM published policies inventory, 2026-07-31) — see "
    f"[`../PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md`](../PHASE_05_MANUFACTURERS_WORKSTREAM_REPORT.md)  \n"
    f"**Phase 5 overall:** In progress (technical baseline T254–T260 and residual brands remain)",
    text2,
    count=1,
)

# Append WS1 status section if missing
if "Workstream 1 status" not in text2:
    text2 += """

---

## Workstream 1 status (2026-07-31) — Manufacturers

- 15 OEM notes under `research/manufacturers/` (official documentation only).
- Matrices: coverage, comparison, lifecycle; source/citation/validation reports.
- Negative finding: no industry-wide multi-year matrix; uneven official documentation depth.
- POCO covered under Xiaomi family note; iQOO/Tecno/Infinix and other India-volume discovery residual.
- Technical baseline notes (T254–T260) **not** part of WS1 — remain open.
- PDF annexure archive (T252) residual OPEN.
- Phase 5 **not** complete; WS2 **not** started.

"""

phase5.write_text(text2, encoding="utf-8")
print(f"phase-05 tasks: {done} done, {open_n} open, {total} total")

# Update TASKS.md dashboard counts for phase 5
tasks = ROOT / "TASKS.md"
tt = tasks.read_text(encoding="utf-8")
# Phase 5 row
tt = re.sub(
    r"(\| 5 \| \[`tasks/phase-05\.md`\]\(tasks/phase-05\.md\) \| )[^\|]+(\| )\d+( \| )\d+( \| )\d+",
    rf"\g<1>**In progress** (WS1 manufacturers complete)\2{done}\3{open_n}\4{total}",
    tt,
    count=1,
)
# Totals row: recalculate from known phase table is fragile; update Phase 5 and totals comment
# Prior: 182 done, 206 open, 388 total with phase5 0/68
# New: done += done, open -= done for phase5
# Old phase5 was 0 done 68 open; now done/open as computed
old_done_total = 182
old_open_total = 206
# previously phase5 contributed 0 done / 68 open
new_done_total = old_done_total + done
new_open_total = old_open_total - done
tt = re.sub(
    r"\| \| \| \*\*Totals\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \|",
    f"| | | **Totals** | **{new_done_total}** | **{new_open_total}** | **388** |",
    tt,
    count=1,
)
tt = tt.replace(
    "4. **Phase 5 WS1** — manufacturers (`research/manufacturers/`) when 0.6.1 merges. Further Phase 5 WS — **not auto-started**.",
    "4. **Phase 5 WS1 complete** (when 0.6.1 merges) — `research/manufacturers/`. Further Phase 5 WS (technical baseline) — **not auto-started**.",
)
tasks.write_text(tt, encoding="utf-8")
print("TASKS.md updated")
print("done")
