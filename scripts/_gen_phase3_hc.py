# -*- coding: utf-8 -*-
from pathlib import Path
OUT = Path("research/judgments/high-courts")
OUT.mkdir(parents=True, exist_ok=True)
TODAY = "2026-07-30"

def brief(slug, name, citation, court, bench, year, facts, issues, decision, principles, observations, relevance, limitations, open_q, strength):
    t = f"""---
title: "{name}"
domain: "judgments"
court: "{court}"
status: PROVISIONAL
last_updated: {TODAY}
agent: "Case Law Research Agent"
phase: 3
workstream: "HC-2"
pin_cite_status: "PROVISIONAL"
relevance_strength: "{strength}"
persuasive_only: true
---

# Judgment Brief — {name}

**Litigation advice:** None. Neutral High Court mapping only.  
**Authority status:** High Court decisions are **persuasive**, not binding on other High Courts or the Supreme Court (unless affirmed).  
**Pin-cite status:** PROVISIONAL — re-verify on SCC Online / official HC portal before court use.

## 1. Case Name

*{name}*

## 2. Citation

{citation}

## 3. High Court

{court}

## 4. Bench

{bench}

## 5. Date

Year: **{year}** (exact calendar date to be confirmed from official judgment text)

## 6. Facts [FACT]

{facts}

## 7. Issues [FACT/LAW]

{issues}

## 8. Decision [LAW]

{decision}

## 9. Legal principles [LAW]

{principles}

## 10. Important observations [LAW/ANALYSIS]

{observations}

## 11. Relevance to this repository [ANALYSIS]

{relevance}

**Not asserted:** That this judgment creates a legal duty requiring smartphone manufacturers to provide OS or security updates for a specified minimum period.

## 12. Limitations

{limitations}

## 13. Open questions [OPEN]

{open_q}

## 14. Official sources

1. {citation} — confirm on SCC Online / High Court judgment portal / certified copy. Access date for this note: {TODAY}.
2. Cross-links: `research/constitution/`, `research/statutes/`, SC Workstream 1 briefs where applicable.

## Audit trail

- Phase 3 Workstream 2 (High Courts)
- Validation: `research/judgments/HIGH_COURT_VALIDATION_REPORT.md`
"""
    (OUT / f"{slug}.md").write_text(t, encoding="utf-8")
    print("wrote", slug)

brief(
    "faheema-shirin-kerala-2019",
    "Faheema Shirin R.K. v. State of Kerala",
    "2019 SCC OnLine Ker 2976 (confirm parallel citations on SCC Online / official Kerala HC portal)",
    "High Court of Kerala",
    "Single Judge / Division Bench as per judgment text (confirm on official text)",
    "2019",
    "A student challenged hostel restrictions that limited use of mobile phones / internet access in connection with educational pursuits. The petition engaged questions of privacy, autonomy, and access to information/education through digital means.",
    "Whether restrictions on mobile phone / internet use in a student hostel violated fundamental rights (including privacy / personal liberty dimensions under Article 21, as commonly discussed in reporting of the case). Exact framed issues to be confirmed from full judgment text.",
    "The Court is widely reported to have recognised that mobile phones / internet access can be integral to education and personal liberty/privacy interests in the modern context, and granted relief against blanket restrictions (precise operative directions PROVISIONAL—verify full text).",
    "- Digital access tools (phones/internet) can engage Article 21 interests in educational settings\n- Blanket bans may require justification consistent with constitutional standards\n- Privacy/autonomy themes in student life (as commonly summarised)",
    "Often cited in Indian digital-rights secondary literature as an early High Court engagement with mobile phones as instruments of learning and personal liberty after *Puttaswamy*. Treat secondary summaries carefully until full text is verified.",
    "**Strength: Medium (digital rights / devices as access tools).** Supports the idea that smartphones are constitutionally salient *end-point devices* for education and personal liberty. Does **not** regulate OEM software-support duration or security-update policies. Relevance to software support is **indirect** (device importance), not direct (update mandates).",
    "Hostel/education facts; High Court persuasive only; not an OEM liability or product-standards case; secondary reports vary—full text verification mandatory.",
    "1. Exact ratio on privacy vs institutional discipline?\n2. Does the judgment speak to device *security* or only *access*?",
    "Medium",
)

brief(
    "karmanya-singh-sareen-delhi-2016",
    "Karmanya Singh Sareen v. Union of India",
    "2016 SCC OnLine Del 4551 / W.P.(C) 7663/2016 (confirm authoritative citation on SCC Online / Delhi HC portal)",
    "High Court of Delhi",
    "Confirm bench on official judgment",
    "2016",
    "Petitioners challenged WhatsApp's privacy policy / data-sharing practices with Facebook, raising privacy and user-consent concerns regarding digital communications platforms.",
    "Whether changes to WhatsApp privacy policy / data sharing violated users' rights to privacy; scope of High Court intervention regarding platform privacy practices (confirm issues from full text).",
    "The Delhi High Court considered privacy concerns around messaging-platform data practices in the pre- and peri-*Puttaswamy* period; subsequent developments include Supreme Court privacy recognition (2017). Precise operative directions and final posture PROVISIONAL—verify full text and any appellate history.",
    "- Informational privacy concerns in digital platforms\n- User consent / data sharing as public-law issues in appropriate cases\n- High Court as forum for digital privacy grievances",
    "Frequently discussed in Indian privacy literature. Must not be confused with the Supreme Court *Puttaswamy* privacy Constitution Bench judgment.",
    "**Strength: Medium (privacy / digital governance).** Reinforces judicial attention to digital privacy and platform practices. Does **not** impose multi-year OS/security update duties on handset manufacturers. Connection to software support is **weak-to-medium** (privacy ecosystem), not product-update longevity.",
    "Platform/privacy policy facts; not OEM hardware/software support; citation and subsequent history need verification; persuasive HC authority only.",
    "1. Appellate/SC treatment of the WhatsApp privacy litigation stream?\n2. Relevance, if any, to end-point device security vs app-layer privacy?",
    "Medium",
)

# Inclusion criteria as separate doc not a judgment
Path("research/judgments/high-courts/hc-inclusion-criteria.md").write_text(f"""---
title: "High Court inclusion criteria (relevance rubric)"
domain: "judgments"
status: VERIFIED
last_updated: {TODAY}
phase: 3
workstream: "HC-2"
---

# High Court Inclusion Criteria — Relevance Rubric

**Purpose:** Ensure HC cases enter the corpus only with material connection to repository objectives.  
**Authority level:** All HC judgments are **persuasive only**.

## Include if (one or more)

1. Interprets consumer protection / unfair practices / product-related consumer remedies in a way that can inform software-support disclosure or defect theories.  
2. Addresses digital rights, privacy, or internet/mobile access with clear end-point device salience.  
3. Addresses environmental/e-waste regulation with producer responsibility themes.  
4. Clarifies administrative-law duties of government regulators material to standards-setting.  
5. Clarifies constitutional remedies / PIL procedure at High Court level relevant to systemic petitions.

## Exclude if

1. Technology is merely incidental (e.g. phone used only as evidence of crime).  
2. Purely private contractual disputes without public-law principle of wider application.  
3. Citation cannot be verified to a standard reporter or official portal.  
4. Relevance would require strained analogy to invent an OEM update-year duty.

## Quality over quantity

Prefer fewer high-signal cases over encyclopaedic dumps.

## Sources

Repository PROJECT_SPECIFICATION scope; VALIDATION.md; Phase 3 task list T161.
""", encoding="utf-8")
print("criteria ok")

Path("research/judgments/high-courts/telangana-hc-pil-procedure-note.md").write_text(f"""---
title: "Telangana High Court PIL / e-filing procedure — research note"
domain: "judgments"
status: SECONDARY
last_updated: {TODAY}
phase: 3
workstream: "HC-2"
---

# Telangana High Court — PIL Procedure Research Note

**Not a judgment brief.** Institutional procedure inventory for Task T162.

## Status

Official practice directions, e-filing rules, and PIL filing checklists of the High Court for the State of Telangana must be read from the **current official court website** and e-filing portal. Rules change; this note does not freeze a dated checklist as law.

## What to capture (when annexing)

1. Current PIL/category designation for public interest matters  
2. E-filing mandatory fields and affidavit formats  
3. Advance service requirements on Union / State respondents  
4. Any specific format for synopsis / list of dates  

**Official starting points (confirm live):** High Court of Telangana official website / e-filing portal (tshc.gov.in or successor URL). Access date for this inventory note: {TODAY}.

## Relevance [ANALYSIS]

If a future petition is considered in Telangana HC under Article 226, local procedure is essential. This does **not** decide forum choice (still OPEN between Art. 32 and Art. 226).

## Limitations

No substitute for certified practice directions PDF. Marked SECONDARY until official PDFs annexed to `evidence/annexures/`.

## Open questions [OPEN]

1. Latest PIL practice direction number and date  
2. Any special roster for environmental / consumer PILs
""", encoding="utf-8")
print("telangana ok")

# limited e-waste note
Path("research/judgments/high-courts/hc-ewaste-search-note.md").write_text(f"""---
title: "High Court e-waste / environment PIL search note"
domain: "judgments"
status: SECONDARY
last_updated: {TODAY}
phase: 3
workstream: "HC-2"
---

# High Court E-Waste / Environment PIL — Search Note

**Not a judgment brief.** Documents search outcome for Task T164.

## What was searched [FACT]

Public secondary indexes and news/legal databases for High Court PILs specifically establishing producer software-support duties or OS-update mandates. Also oriented search for e-waste management enforcement PILs.

## What was found [FACT/ANALYSIS]

- Environmental and e-waste **regulatory** themes are primarily statutory (E-Waste Rules 2022) and Supreme Court environmental doctrine (see SC Workstream 1: *Vellore*, *Subhash Kumar*, etc.).  
- No High Court judgment was located in this pass that **directly** orders smartphone manufacturers to provide multi-year OS/security updates.  
- Scattered HC environmental PILs may exist on local dumping/recycling; they require case-by-case SCC Online verification before inclusion as named briefs.

## What was not found [FACT]

No verified HC citation in this workstream establishing a **minimum software-support period** duty on OEMs.

## Relevance

Supports **negative finding** document. Future researchers may add named e-waste HC briefs if official citations are verified and material.

## Sources

Search protocol date: {TODAY}; SC environment briefs; statutes e-waste note.
""", encoding="utf-8")
print("ewaste search ok")
