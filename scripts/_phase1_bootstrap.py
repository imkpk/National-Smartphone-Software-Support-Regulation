#!/usr/bin/env python3
"""One-shot Phase 1 scaffolding writer. Safe to re-run."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]

domains = {
    "research/constitution": (
        "Constitutional Research",
        "Map relevant Articles and doctrine. No invented fundamental rights. Forum-neutral.",
    ),
    "research/statutes": (
        "Statutory Research",
        "Central Acts and rules with section numbers from India Code / Gazette.",
    ),
    "research/judgments": (
        "Judgments Corpus",
        "Supreme Court and High Court briefs with official citations only.",
    ),
    "research/government": (
        "Government Policy",
        "MeitY, DoT, Consumer Affairs, MoEFCC, CPCB, BIS, CERT-In and related soft law.",
    ),
    "research/manufacturers": (
        "Manufacturer Policies",
        "Official OEM software support pages; URL + access date mandatory.",
    ),
    "research/cybersecurity": (
        "Cybersecurity Research",
        "Patch lifecycle, unsupported devices, authoritative technical sources only.",
    ),
    "research/environment": (
        "Environment / E-Waste",
        "EPR, e-waste data, software-forced obsolescence pathway (analysis labelled).",
    ),
    "research/international": (
        "Comparative International Law",
        "Persuasive only. Stamp non-binding-in-India on every note.",
    ),
    "research/economics": (
        "Economics",
        "Consumer and lifecycle costs; models marked ESTIMATE.",
    ),
    "research/technical": (
        "Technical Baseline",
        "Descriptive OS/security update mechanics; no reverse engineering.",
    ),
    "research/consumer-law": (
        "Consumer Law",
        "CPA 2019 interface with software support / disclosure.",
    ),
    "research/forum": (
        "Forum Analysis",
        "Art. 32 vs Art. 226 objective comparison. Do not pre-judge forum until memo complete.",
    ),
}

for path, (title, blurb) in domains.items():
    p = root / path
    p.mkdir(parents=True, exist_ok=True)
    (p / "README.md").write_text(
        f"""# {title}

**Domain path:** `{path}/`  
**Phase for substantive content:** 2+ (this README is Phase 1 scaffolding)  
**Status:** Index only — no substantive research yet

## Purpose

{blurb}

## Rules

- Bind to root [`VALIDATION.md`](../../VALIDATION.md) and [`CITATION_POLICY.md`](../../CITATION_POLICY.md).
- Use templates from [`templates/`](../../templates/).
- Label claims: FACT | LAW | ANALYSIS | NORM | OPEN.
- Prefer primary / official sources.

## Contents

| File | Status |
|------|--------|
| *(none yet)* | — |

## Related agents

See [`AGENTS.md`](../../AGENTS.md).

---
*Phase 1 domain index*
""",
        encoding="utf-8",
    )

(root / "research" / "README.md").write_text(
    """# Research

Central research workspace for **National-Smartphone-Software-Support-Regulation**.

## Domains

| Folder | Domain | Substantive phase |
|--------|--------|-------------------|
| `constitution/` | Constitution of India | 2 |
| `statutes/` | Central statutes & rules | 2 |
| `judgments/` | SC & HC case law | 3 |
| `government/` | Policies & institutions | 4 |
| `manufacturers/` | OEM software support | 5 |
| `technical/` | Technical baseline | 5 |
| `cybersecurity/` | Cyber risk pathways | 6 |
| `environment/` | E-waste / environment | 6 |
| `economics/` | Economics / lifecycle | 6 |
| `consumer-law/` | Consumer protection deep dive | 2–6 |
| `international/` | Comparative law | 7 |
| `forum/` | Art. 32 vs Art. 226 analysis | before litigation |

## Workflow

1. Use a template from `/templates`.
2. Write in the correct domain folder.
3. Pass research-gate checklist in `/validation`.
4. Update `TASKS.md`.
5. Log completion in `/logs`.

## Hard rules

- **No fabricated citations.**
- **No litigation promotion** from incomplete research.
- **Forum remains open** until `research/forum/` analysis is complete and counsel reviews.

---
*Phase 1*
""",
    encoding="utf-8",
)

(root / "evidence" / "README.md").write_text(
    """# Evidence

Annexure-ready artefacts derived from **validated** research only.

## Subfolders

| Folder | Use |
|--------|-----|
| `tables/` | Comparison and coverage tables |
| `charts/` | Figures with source footnotes |
| `timelines/` | Chronologies |
| `annexures/` | Numbered annexure packs / captures |

## Rules

- Every artefact cites underlying sources.
- No decorative charts without data provenance.
- Client documents (grievances, invoices) go here only when primary files are available.

**Phase 1:** Structure only. Population starts Phase 5–8.

---
*Phase 1*
""",
    encoding="utf-8",
)

(root / "litigation" / "README.md").write_text(
    """# Litigation

**STATUS: NOT STARTED (Phase 9 hard gate)**

Court-oriented drafts (synopsis, PIL, affidavit, prayers) must **not** be written until:

1. Research Phases 2–8 produce validated input packs  
2. Forum analysis in `research/forum/` is complete  
3. Project Manager records Phase 9 approval in `CHANGELOG.md`  
4. Citation Validation + QA gates pass  

All drafts must carry: `DRAFT — NOT FOR FILING` until human counsel certification.

## Subfolders

| Folder | Intended content |
|--------|------------------|
| `synopsis/` | Court synopsis |
| `pil/` | Writ petition body |
| `affidavit/` | Supporting affidavit |
| `prayers/` | Interim / final prayers extracts |
| `drafts/` | Working scratch (still gated) |

---
*Phase 1 banner — do not populate yet*
""",
    encoding="utf-8",
)

# Templates
templates_dir = root / "templates"
templates_dir.mkdir(exist_ok=True)

front_matter = """---
title: ""
domain: ""
status: PROVISIONAL
last_updated: YYYY-MM-DD
agent: ""
phase: 
labels_allowed: [FACT, LAW, ANALYSIS, NORM, OPEN, SECONDARY, UNVERIFIED, DISPUTED, OUTDATED]
---
"""

templates = {
    "00_yaml_front_matter.md": f"""# YAML Front-Matter Convention

All research notes should begin with YAML front matter:

```yaml
{front_matter.strip()}
```

## Status vocabulary

| Status | Meaning |
|--------|---------|
| PROVISIONAL | Working draft |
| VERIFIED | Primary sources checked |
| SECONDARY | Secondary only |
| UNVERIFIED | Hypothesis |
| DISPUTED | Conflict |
| OUTDATED | Superseded |

See root `VALIDATION.md`.
""",
    "constitutional_provision_note.md": f"""{front_matter}# Constitutional Provision Note — [Article X]

## Scope

## Text / official source

- Source URL / India Code reference:
- Access date:

## Verified facts [FACT]

## Law [LAW]

## Analysis [ANALYSIS]

## Strategic notes [NORM] (optional; not law)

## Uncertainties [OPEN]

## Sources

## Audit trail

- Author:
- Reviewer:
- Validation gate: pending / pass / fail
""",
    "statute_section_note.md": f"""{front_matter}# Statute Note — [Act], [Section/Rule]

## Instrument

- Short title:
- Year:
- Section / Rule / Schedule:
- Official source (India Code / Gazette):
- Access date:

## Verified facts [FACT]

## Law [LAW]

## Applicability to software support [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "judgment_brief.md": f"""{front_matter}# Judgment Brief — [Case Name]

## Citation block (required)

- Case name:
- Court:
- Citation(s): *(SCC / AIR / SCR / INSC / neutral — do not invent)*
- Year:
- Bench strength (if known):
- Pin-cite status: PROVISIONAL | VERIFIED

## Facts (brief) [FACT]

## Holding / ratio [LAW]

## Relevant paragraphs (only if verified)

## Application to this project [ANALYSIS]

## Why it matters [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "government_policy_memo.md": f"""{front_matter}# Government Policy Memo — [Title]

## Issuing authority

## Document title and date

## Official URL / Gazette ID

## Access date

## Verified facts [FACT]

## Legal character [LAW] (statute / rules / soft law / press note)

## Relevance [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "oem_policy_capture.md": f"""{front_matter}# OEM Policy Capture — [Brand]

## Capture metadata [FACT]

- Brand / legal entity:
- Page title:
- URL:
- Access datetime (ISO):
- Archive method (print-PDF / archive.org / other):
- Model / series scope:

## Stated OS upgrade support

## Stated security update support

## Distinctions / caveats (flagship vs entry, regions)

## Verified facts [FACT]

## Analysis [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "cybersecurity_note.md": f"""{front_matter}# Cybersecurity Note — [Topic]

## Scope

## Verified facts [FACT]

## Technical explanation [ANALYSIS] (cite platform docs)

## Risk pathways [ANALYSIS]

## What is NOT claimed [OPEN / limits]

## Sources (NVD, Android bulletins, CERT-In public, etc.)

## Audit trail
""",
    "environment_ewaste_note.md": f"""{front_matter}# Environment / E-Waste Note — [Topic]

## Scope

## Verified statistics [FACT] (publisher, year, page)

## Legal / policy instruments [LAW]

## Causal pathway discussion [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "comparative_jurisdiction_note.md": f"""{front_matter}# Comparative Jurisdiction Note — [Country / Region]

> **PERSUASIVE COMPARATIVE MATERIAL — NOT BINDING IN INDIA**

## Instrument(s)

- Title:
- Number / citation:
- Official source:
- Access date:

## Verified requirements [FACT]

## Relevance to Indian debate [ANALYSIS]

## Limits of analogy [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "economics_model_note.md": f"""{front_matter}# Economics Note — [Topic]

## Scope

## Assumptions (mandatory if modelling)

## Verified data [FACT]

## Estimates [label as ESTIMATE]

## Analysis [ANALYSIS]

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "technical_explainer.md": f"""{front_matter}# Technical Explainer — [Topic]

## Scope

## Verified platform documentation [FACT]

## Descriptive explanation [ANALYSIS]

## Boundaries (no reverse engineering / no exploits)

## Sources

## Audit trail
""",
    "consumer_law_issue_note.md": f"""{front_matter}# Consumer Law Issue Note — [Issue]

## Statutory anchor [LAW]

## Verified facts [FACT]

## Analysis [ANALYSIS]

## Interface with PIL strategy [ANALYSIS] (not a filing document)

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "evidence_table_schema.md": """# Evidence Table Schema

Use Markdown tables or CSV under `evidence/tables/`.

## Required columns (minimum)

| column | description |
|--------|-------------|
| id | Stable row ID |
| claim_or_item | Short description |
| value | Data point |
| source_tier | T0–T4 per VALIDATION.md |
| source | Citation or URL |
| access_date | ISO date |
| status | VERIFIED / SECONDARY / UNVERIFIED |
| notes | Caveats |

## File naming

`evidence/tables/YYYY-MM-DD_short-name.md` or `.csv`
""",
    "timeline_event_schema.md": """# Timeline Event Schema

| field | required | description |
|-------|----------|-------------|
| date | yes | YYYY-MM-DD or YYYY-MM or YYYY |
| event | yes | Neutral description |
| source | yes | Citation/URL |
| status | yes | VERIFIED / SECONDARY |
| category | no | legal / policy / industry / client |
| notes | no | |

Store under `evidence/timelines/`.
""",
    "annexure_index_row.md": """# Annexure Index Row Template

| Annexure No. | Description | Source path | Pages | Status |
|--------------|-------------|-------------|-------|--------|
| A-__ | | | | TO BE ANNEXED |

Map each petition assertion to an annexure ID in litigation phase.
""",
    "rti_application.md": """# RTI Application Template

**To:** Central Public Information Officer, [Ministry/Department]  
**From:** [Applicant]  
**Date:**  

## Subject

Request under the Right to Information Act, 2005 regarding smartphone software support standards / related records.

## Information sought

1.  
2.  
3.  

## Period

## Format

Electronic copies preferred.

## Declaration

I am a citizen of India. Fee as applicable.

---
*Template only — customise per public authority. Not legal advice.*
""",
    "validation_report.md": """# Validation Report

**File validated:**  
**Validator:** Citation Validation Agent / human  
**Date:**  
**Result:** PASS / FAIL / PASS WITH CONDITIONS  

## Checklist

- [ ] Legal claims cited  
- [ ] Judgments have official citations  
- [ ] Statutes have section numbers  
- [ ] No fabricated authorities  
- [ ] FACT/LAW/ANALYSIS separated  
- [ ] Status tags present  
- [ ] Sources section complete  

## Defects

| # | Location | Severity | Description | Fix required |
|---|----------|----------|-------------|--------------|

## Sign-off

""",
    "litigation_assertion_source_map.md": """# Litigation Assertion → Source Map

**Status:** Use only in Phase 9+  
**Draft banner:** DRAFT — NOT FOR FILING  

| Assertion ID | Pleading location | Claim class | Source research path | Annexure ID | Validation |
|--------------|-------------------|-------------|----------------------|-------------|------------|
| A001 | | FACT/LAW | | | |

""",
    "forum_analysis_memo.md": f"""{front_matter}# Forum Analysis Memo — Article 32 vs Article 226

**Rule:** Objective comparison only. Do **not** pre-judge forum in Phase 1.

## Scope

Compare suitability of:

1. Supreme Court under Article 32  
2. High Court under Article 226 (specify candidate High Court only after nexus facts)

## Verified constitutional text [LAW]

## Factors matrix [ANALYSIS]

| Factor | Art. 32 SC | Art. 226 HC | Notes / sources |
|--------|------------|-------------|-----------------|
| Nature of rights claimed | | | |
| Territorial nexus | | | |
| Alternative remedies | | | |
| Policy vs justiciability | | | |
| National uniformity | | | |
| Precedent on similar PILs | | | |
| Client facts (residence, sale, grievances) | | | |

## Arguments for each forum [ANALYSIS]

## Risks of each forum [ANALYSIS]

## Recommendation [NORM]

*(Leave blank until research complete and counsel reviews.)*

## Uncertainties [OPEN]

## Sources

## Audit trail
""",
    "sample_synthetic_style_only.md": f"""{front_matter.replace('title: ""', 'title: "Synthetic style sample (non-legal)"').replace('status: PROVISIONAL', 'status: PROVISIONAL')}# Synthetic Style Sample (NON-LEGAL — DO NOT CITE)

This file demonstrates formatting only. It contains **no** legal research.

## Verified facts [FACT]

- The repository uses Markdown.  
  - Source: this repository's README.md (structural fact about the project).

## Analysis [ANALYSIS]

- Consistent headings aid review.

## Uncertainties [OPEN]

- None for this synthetic sample.

## Sources

1. Repository README.md (project file).

## Audit trail

- Created for Phase 1 style demonstration only.
""",
}

for name, content in templates.items():
    (templates_dir / name).write_text(content, encoding="utf-8")

(templates_dir / "README.md").write_text(
    """# Templates

Phase 1 research and process templates. Copy a file, fill it, and save under the correct `research/` or `evidence/` path.

## Catalogue

| Template | Use |
|----------|-----|
| `00_yaml_front_matter.md` | Status vocabulary + front matter |
| `constitutional_provision_note.md` | Constitution |
| `statute_section_note.md` | Acts / rules |
| `judgment_brief.md` | Case law |
| `government_policy_memo.md` | Policies |
| `oem_policy_capture.md` | OEM support pages |
| `cybersecurity_note.md` | Cyber research |
| `environment_ewaste_note.md` | E-waste |
| `comparative_jurisdiction_note.md` | Foreign law |
| `economics_model_note.md` | Economics |
| `technical_explainer.md` | Technical |
| `consumer_law_issue_note.md` | Consumer law |
| `forum_analysis_memo.md` | Art. 32 vs 226 (do not pre-judge) |
| `evidence_table_schema.md` | Tables |
| `timeline_event_schema.md` | Timelines |
| `annexure_index_row.md` | Annexures |
| `rti_application.md` | RTI |
| `validation_report.md` | Validation gate |
| `litigation_assertion_source_map.md` | Phase 9 mapping |
| `sample_synthetic_style_only.md` | Format demo only |

## Status tags

See `00_yaml_front_matter.md` and root `VALIDATION.md`.

---
*Phase 1*
""",
    encoding="utf-8",
)

print("Templates OK:", len(templates))
print("Root:", root)
