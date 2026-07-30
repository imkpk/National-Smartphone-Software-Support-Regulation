# -*- coding: utf-8 -*-
"""Generate Phase 3 Workstream 1 Supreme Court judgment briefs."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "research" / "judgments" / "supreme-court"
OUT.mkdir(parents=True, exist_ok=True)
TODAY = "2026-07-30"

CASES = []


def add(**kwargs):
    CASES.append(kwargs)


def write_all():
    for c in CASES:
        slug = c["slug"]
        text = f'''---
title: "{c["name"]}"
domain: "judgments"
court: "Supreme Court of India"
status: PROVISIONAL
last_updated: {TODAY}
agent: "Case Law Research Agent"
phase: 3
workstream: "SC-1"
pin_cite_status: "{c.get("pin", "PROVISIONAL")}"
relevance_strength: "{c["strength"]}"
---

# Judgment Brief — {c["name"]}

**Litigation advice:** None. Neutral case mapping only.  
**Pin-cite status:** {c.get("pin", "PROVISIONAL")} — re-verify paragraphs on SCC Online / official reports before court use.

## 1. Case Name

*{c["name"]}*

## 2. Citation

{c["citation"]}

## 3. Court

Supreme Court of India

## 4. Bench

{c["bench"]}

## 5. Date

Year of decision: **{c["year"]}** (exact calendar date to be confirmed from official reporter if required for filing)

## 6. Facts (neutral) [FACT]

{c["facts"]}

## 7. Issues [FACT/LAW]

{c["issues"]}

## 8. Holding [LAW]

{c["holding"]}

## 9. Important observations [LAW/ANALYSIS]

{c["observations"]}

## 10. Legal principles established [LAW]

{c["principles"]}

## 11. Relevance to this repository [ANALYSIS]

{c["relevance"]}

**Not asserted:** That this judgment creates a legal duty requiring smartphone manufacturers to provide OS or security updates for any specified minimum period.

## 12. Limitations

{c["limitations"]}

## 13. Open questions [OPEN]

{c["open_q"]}

## 14. Official citations / sources

1. {c["citation"]} — primary reporter citation (confirm on SCC Online / SCR / AIR / Court portal). Access date for this research note: {TODAY}.
2. Cross-links: `research/constitution/`, `research/statutes/` as applicable.

## Audit trail

- Phase 3 Workstream 1 (Supreme Court)
- Validation: `research/judgments/SUPREME_COURT_VALIDATION_REPORT.md`
'''
        (OUT / f"{slug}.md").write_text(text, encoding="utf-8")
        print("wrote", slug)


# --- PIL & procedure ---
add(
    slug="sp-gupta-1981",
    name="S.P. Gupta v. Union of India",
    citation="1981 Supp SCC 87; AIR 1982 SC 149",
    year="1981/1982",
    bench="Larger Bench (Judges' Transfer case; PIL locus exposition)",
    facts="Challenges relating to judicial appointments and transfers; the Court extensively discussed standing to sue in matters of public interest.",
    issues="Whether traditional locus standi bars public-spirited persons from approaching the Court for public injury; scope of public interest litigation.",
    holding="The Court relaxed rigid locus standi where legal wrong is caused to a person or determinate class unable to approach the Court, allowing bona fide public interest petitioners (as commonly understood). Exact ratio and paragraphs remain PROVISIONAL pending full-text pin-cite.",
    observations="PIL is a means of access to justice for public injury; courts must still police abuse. Foundational for later PIL guidelines cases.",
    principles="- Liberalised standing for bona fide public causes\n- Distinction between private injury and public injury\n- Caution against busybody petitioners (developed further later)",
    relevance="**Strength: High (procedure).** Maintainability doctrine for any future public-interest petition on systemic regulatory gaps. Does **not** decide product-regulation merits or OEM update duties.",
    limitations="Does not address consumer electronics, cybersecurity product standards, or e-waste. Standing is necessary but never sufficient for relief.",
    open_q="1. How do later PIL-abuse guidelines (e.g. *Chaufal*) refine *S.P. Gupta*?\n2. What factual showings distinguish genuine public injury from private commercial phone disputes?",
    strength="High",
)

add(
    slug="bandhua-mukti-morcha-1984",
    name="Bandhua Mukti Morcha v. Union of India",
    citation="(1984) 3 SCC 161",
    year="1984",
    bench="Supreme Court (confirm composition on reporter)",
    facts="Petition concerning bonded labour; the Court used flexible public interest procedure and investigative directions.",
    issues="Scope of the Court's power to fashion procedure in PIL; enforcement of fundamental rights of disadvantaged persons.",
    holding="Court affirmed flexible PIL procedure to vindicate fundamental rights, including fact-finding mechanisms as commonly summarised (PROVISIONAL pin-cites).",
    observations="Illustrates structural public-law remedial flexibility beyond traditional adversarial process.",
    principles="- Procedural flexibility in PIL\n- Court may appoint commissions / seek reports in appropriate cases",
    relevance="**Strength: Medium (procedure).** Complex systemic issues can be handled in PIL form with structured process. Not about smartphones or OS updates.",
    limitations="Labour-specific facts; remedies not transferable as product mandates.",
    open_q="1. Limits of investigative commissions in technology-policy PILs?",
    strength="Medium",
)

add(
    slug="pudr-1982",
    name="People's Union for Democratic Rights v. Union of India",
    citation="(1982) 3 SCC 235",
    year="1982",
    bench="Supreme Court (confirm on reporter)",
    facts="Allegations of labour-law violations in construction for Asian Games projects; petition treated as public interest matter.",
    issues="Whether non-observance of labour welfare laws could be enforced via constitutional litigation; standing of a social organisation.",
    holding="Court entertained the petition and emphasised enforcement of labour rights as constitutional concerns in the circumstances of the case (details PROVISIONAL).",
    observations="Early expansion of PIL into socio-economic rights enforcement themes.",
    principles="- Access to justice for workers via public petitioners\n- Link between statutory welfare and constitutional values",
    relevance="**Strength: Low–Medium (procedure / access).** Background PIL access theme. Weak direct link to software support.",
    limitations="Labour facts; not digital product regulation.",
    open_q="1. Whether socio-economic PIL templates map to consumer digital-security externalities without overreach?",
    strength="Low-Medium",
)

add(
    slug="balwant-singh-chaufal-2010",
    name="State of Uttaranchal v. Balwant Singh Chaufal",
    citation="(2010) 3 SCC 402",
    year="2010",
    bench="Supreme Court (confirm on reporter)",
    facts="The Court addressed misuse of PIL jurisdiction and laid down guidelines to check frivolous or motivated petitions.",
    issues="How courts should filter PILs; credentials, bona fides, and safeguards against abuse.",
    holding="Guidelines for entertaining PILs, including verification of credentials and prima facie correctness, and deterrence of abuse (as commonly understood). Pin-cites PROVISIONAL.",
    observations="Bona fides and discouragement of private interest masked as PIL.",
    principles="- Anti-abuse PIL guidelines\n- Emphasis on bona fides and public cause",
    relevance="**Strength: High (procedure).** Directly relevant to filing discipline for any future public-interest matter. Requires clean research record and no oblique commercial motive.",
    limitations="Does not decide merits of technology regulation.",
    open_q="1. How to document bona fides and exhaustion for a standards-gap petition?",
    strength="High",
)

add(
    slug="fertilizer-corporation-1981",
    name="Fertilizer Corporation Kamgar Union (Regd.) v. Union of India",
    citation="AIR 1981 SC 344; (1981) 1 SCC 568 (confirm parallel citations on reporter)",
    year="1981",
    bench="Supreme Court (confirm)",
    facts="Challenge by a workers' union relating to sale of plant/assets of a public sector undertaking; standing and public interest themes discussed.",
    issues="Locus of a trade union / workers in challenging governmental economic decisions affecting public property.",
    holding="The Court discussed standing in the context of public interest and workers' concerns (precise holding PROVISIONAL—verify full text). Often cited in early PIL standing lineage.",
    observations="Part of the historical expansion of standing beyond traditional personal injury.",
    principles="- Early standing expansion themes\n- Public property / public interest interface",
    relevance="**Strength: Low–Medium (historical PIL lineage).** Background maintainability history only. Weak direct link to smartphone software support.",
    limitations="Industrial/public sector facts; not consumer electronics.",
    open_q="1. Relative weight of early standing cases vs *S.P. Gupta*/*Chaufal* for modern PILs?",
    strength="Low-Medium",
)

add(
    slug="puttaswamy-privacy-2017",
    name="Justice K.S. Puttaswamy (Retd.) v. Union of India",
    citation="(2017) 10 SCC 1",
    year="2017",
    bench="Nine-Judge Bench",
    facts="Reference on whether privacy is a fundamental right under the Constitution, arising in the broader context of Aadhaar and related debates.",
    issues="Whether the right to privacy is protected as a fundamental right; its sources and contours under Part III.",
    holding="The Court held that privacy is a fundamental right protected under the Constitution, principally under Article 21 (and related freedoms), with a multi-opinion structure. Exact paragraph mapping PROVISIONAL pending full pin-cite verification.",
    observations="Informational privacy, dignity, and autonomy themes; privacy not absolute—subject to lawful restrictions as developed in the opinions.",
    principles="- Privacy as fundamental right\n- Informational privacy recognised\n- Limits via legality, legitimate aim, proportionality (as developed)",
    relevance="**Strength: High (digital rights / Art. 21).** Unpatched devices can threaten informational and financial privacy; central interpretive context for digital-personhood arguments. Does **not** impose OEM update-year duties.",
    limitations="Does not regulate product design or manufacturer software-support schedules. Application to private OEM conduct requires a State-action / regulatory theory (OPEN).",
    open_q="1. How does privacy doctrine interface with product-security regulation vs data-fiduciary duties?\n2. What State duties arise when essential services run on personal smartphones?",
    strength="High",
)

add(
    slug="puttaswamy-aadhaar-2019",
    name="Justice K.S. Puttaswamy (Aadhaar) v. Union of India",
    citation="(2019) 1 SCC 1",
    year="2018/2019",
    bench="Constitution Bench (confirm strength on reporter)",
    facts="Constitutional challenges to the Aadhaar scheme and related statutory framework.",
    issues="Validity of Aadhaar architecture, proportionality of data collection/use, and related rights issues.",
    holding="The Court upheld the Aadhaar framework in substantial part with important limitations and severances (details complex—PROVISIONAL; full brief required for any filing reliance).",
    observations="Deep judicial engagement with digital identity infrastructure and proportionality analysis.",
    principles="- Digital identity governance under constitutional scrutiny\n- Proportionality in data/identity systems",
    relevance="**Strength: Medium (digital governance).** Shows constitutional stakes of digital public infrastructure. Weak direct link to OEM OS support periods; supports seriousness of end-point security in a digitised State.",
    limitations="Aadhaar-specific; not a product-standards case.",
    open_q="1. Which holdings, if any, travel beyond Aadhaar to general digital-service security?",
    strength="Medium",
)

add(
    slug="anuradha-bhasin-2020",
    name="Anuradha Bhasin v. Union of India",
    citation="(2020) 3 SCC 637",
    year="2020",
    bench="Supreme Court (confirm)",
    facts="Challenges to internet restrictions/shutdowns in Jammu & Kashmir and related free speech/trade issues.",
    issues="Constitutionality and reviewability of internet shutdowns; freedom of speech and expression through the internet.",
    holding="The Court recognised freedom of speech and expression over the internet as a fundamental right facet and required legality, necessity, and proportionality for restrictions; suspension orders subject to review (details PROVISIONAL).",
    observations="Internet as a medium of speech and commerce; transparency and review of restrictive orders.",
    principles="- Speech via internet protected under Art. 19(1)(a) framework\n- Proportionality / review of shutdowns",
    relevance="**Strength: Medium (digital rights).** Constitutional importance of digital connectivity. Does **not** regulate handset software-support longevity; relevance to insecure devices is indirect.",
    limitations="About State restrictions on networks, not OEM update policies.",
    open_q="1. Boundary between access-to-internet jurisprudence and product-security regulation?",
    strength="Medium",
)

add(
    slug="francis-coralie-mullin-1981",
    name="Francis Coralie Mullin v. Administrator, Union Territory of Delhi",
    citation="(1981) 1 SCC 608",
    year="1981",
    bench="Supreme Court (confirm)",
    facts="Petition concerning conditions of detention and the meaning of life under Article 21.",
    issues="Whether Article 21 includes dignity and basic living conditions beyond mere animal existence.",
    holding="The Court held that the right to life includes the right to live with human dignity and something more than mere animal existence (classic formulation; pin-cites PROVISIONAL).",
    observations="Foundational dignity reading of Article 21 later used across many domains.",
    principles="- Life includes dignity\n- Article 21 not minimal physical survival alone",
    relevance="**Strength: Medium (Art. 21 baseline).** Dignity framing can colour digital participation arguments but is high-level. Does not create product-update duties.",
    limitations="Detention facts; broad principle often extended carefully.",
    open_q="1. Risk of over-extending dignity doctrine to consumer product features?",
    strength="Medium",
)

add(
    slug="maneka-gandhi-1978",
    name="Maneka Gandhi v. Union of India",
    citation="(1978) 1 SCC 248",
    year="1978",
    bench="Seven-Judge Bench (confirm)",
    facts="Challenge to impounding of a passport and the procedure under passport law; expansive reading of Articles 14, 19, and 21.",
    issues="Content of 'procedure established by law' under Article 21; interrelationship of Arts. 14, 19, and 21.",
    holding="The Court held that procedure under Article 21 must be fair, just, and reasonable, and read Articles 14, 19, and 21 as interconnected (widely accepted summary; pin-cites PROVISIONAL).",
    observations="Modern due-process-style reasoning in Indian constitutional law; non-arbitrariness themes.",
    principles="- Fair, just, reasonable procedure under Art. 21\n- Golden triangle: Arts. 14, 19, 21",
    relevance="**Strength: High (constitutional method).** Underpins reasonableness review of State action relevant to regulatory design or challenge. Not about smartphones per se.",
    limitations="Passport facts; doctrine is general.",
    open_q="1. How far reasonableness review reaches executive inaction on product standards?",
    strength="High",
)

add(
    slug="subhash-kumar-1991",
    name="Subhash Kumar v. State of Bihar",
    citation="(1991) 1 SCC 598",
    year="1991",
    bench="Supreme Court (confirm)",
    facts="Petition alleging pollution of river water from industrial discharge; also cautioned against misuse of PIL.",
    issues="Whether right to pollution-free water and air is part of Article 21; maintainability of PIL.",
    holding="The Court recognised that the right to life includes the right to pollution-free water and air for full enjoyment of life, while emphasising PIL must be genuine (summary PROVISIONAL).",
    observations="Environmental quality linked to Article 21; anti-abuse note for PILs.",
    principles="- Pollution-free environment as Art. 21 interest\n- Genuine PIL requirement",
    relevance="**Strength: Medium–High (environment / Art. 21).** Environmental constitutional framing may contextualise e-waste harms from premature device replacement. Does not regulate software support years.",
    limitations="Industrial water pollution facts; not e-waste or electronics specifically.",
    open_q="1. How to connect e-waste harms to Art. 21 without overstating?",
    strength="Medium-High",
)

add(
    slug="vellore-citizens-1996",
    name="Vellore Citizens' Welfare Forum v. Union of India",
    citation="(1996) 5 SCC 647",
    year="1996",
    bench="Supreme Court (confirm)",
    facts="PIL regarding pollution by tanneries in Tamil Nadu discharging untreated effluent.",
    issues="Whether precautionary principle and polluter pays are part of Indian environmental law; remedies for environmental harm.",
    holding="The Court held that the precautionary principle and the polluter pays principle are essential features of sustainable development and part of the law of the land (widely cited; pin-cites PROVISIONAL).",
    observations="Environmental harm remediation; directions for authority/compensation mechanisms in the case context.",
    principles="- Precautionary principle\n- Polluter pays principle\n- Sustainable development as legal feature",
    relevance="**Strength: High (environment).** Core doctrine for e-waste / premature obsolescence *policy* framing (precaution; cost internalisation). Does **not** impose OEM OS-update schedules by itself.",
    limitations="Tannery effluent facts; analogical extension to software obsolescence must be careful and labelled ANALYSIS.",
    open_q="1. Can 'polluter' concepts map to design-for-obsolescence without over-analogy?",
    strength="High",
)

add(
    slug="iclea-1996",
    name="Indian Council for Enviro-Legal Action v. Union of India",
    citation="(1996) 3 SCC 212",
    year="1996",
    bench="Supreme Court (confirm)",
    facts="Environmental damage from chemical industries; remediation and liability.",
    issues="Liability for environmental harm; application of polluter pays.",
    holding="The Court applied polluter pays / absolute liability concepts to require remediation and costs from polluting industries (summary PROVISIONAL).",
    observations="Reinforces enterprise responsibility for environmental damage.",
    principles="- Polluter pays / remediation costs\n- Environmental absolute liability themes",
    relevance="**Strength: Medium (environment).** Cost-internalisation for environmental externalities. Weak direct link to OS updates; stronger for e-waste EPR *policy* context already mapped in statutes.",
    limitations="Chemical industry facts.",
    open_q="1. Interaction with statutory EPR under E-Waste Rules 2022?",
    strength="Medium",
)

add(
    slug="mc-mehta-oleum-1987",
    name="M.C. Mehta v. Union of India (Oleum Gas Leak)",
    citation="(1987) 1 SCC 395",
    year="1987",
    bench="Constitution Bench (confirm)",
    facts="Oleum gas leak from Shriram food/fertilizer plant in Delhi; claims arising from hazardous industrial activity.",
    issues="Standard of liability for enterprises engaged in hazardous/inherently dangerous activities.",
    holding="The Court propounded absolute liability for such enterprises (as distinct from strict liability exceptions under *Rylands*), as commonly understood (pin-cites PROVISIONAL).",
    observations="Public safety / enterprise responsibility landmark.",
    principles="- Absolute liability for hazardous enterprises\n- Public interest remediation themes",
    relevance="**Strength: Low–Medium (public safety analogy only).** Historical enterprise-responsibility culture; **poor direct fit** to smartphone software support. Over-analogy risk is high.",
    limitations="Hazardous industrial gas leak—not consumer electronics software.",
    open_q="1. Should this case be de-emphasised in software-support briefs to avoid weak analogy?",
    strength="Low-Medium",
)

add(
    slug="nd-jayal-2004",
    name="N.D. Jayal v. Union of India",
    citation="(2004) 9 SCC 362",
    year="2004",
    bench="Supreme Court (confirm)",
    facts="Challenges related to the Tehri Dam project; environment and development balance.",
    issues="Application of sustainable development; judicial review of large projects.",
    holding="The Court discussed sustainable development as balancing ecology and development (summary PROVISIONAL).",
    observations="Sustainable development as a guiding principle in environmental decision-making.",
    principles="- Sustainable development balance\n- Environment–development interface",
    relevance="**Strength: Medium (environment policy).** Sustainable development framing for longevity/circular economy *policy*. No software-support mandate.",
    limitations="Dam/project facts.",
    open_q="1. How to use sustainable development without judicially writing technical standards?",
    strength="Medium",
)

add(
    slug="lda-mk-gupta-1994",
    name="Lucknow Development Authority v. M.K. Gupta",
    citation="(1994) 1 SCC 243",
    year="1994",
    bench="Supreme Court (confirm)",
    facts="Consumer dispute relating to housing/allotment by a development authority under the consumer protection framework (1986 Act era).",
    issues="Whether statutory authorities providing housing can be within consumer jurisdiction; scope of consumer protection.",
    holding="The Court adopted an expansive approach to consumer protection and accountability of public bodies providing services (summary PROVISIONAL).",
    observations="Consumerism as a social movement; accountability themes.",
    principles="- Expansive consumer protection ethos\n- Public body as service provider in appropriate cases",
    relevance="**Strength: Medium (consumer welfare ethos).** Seriousness of consumer protection jurisprudence. Does not decide software-update UTP/product-liability questions under CPA 2019 (different statute generation—careful).",
    limitations="Housing service facts; pre-CPA 2019 statute.",
    open_q="1. Which principles travel to CPA 2019 product-liability for digital products?",
    strength="Medium",
)

add(
    slug="cag-jagannathan-1986",
    name="Comptroller and Auditor General of India v. K.S. Jagannathan",
    citation="(1986) 2 SCC 679",
    year="1986",
    bench="Supreme Court (confirm)",
    facts="Service matter involving CAG; discussion of mandamus scope.",
    issues="When mandamus lies to compel performance of public duties.",
    holding="The Court discussed the scope of mandamus to enforce public duties and statutory obligations (summary PROVISIONAL).",
    observations="Classic administrative-law authority often cited for mandamus against public authorities.",
    principles="- Mandamus to enforce public duty\n- Limits where duty is discretionary (refinements in later cases)",
    relevance="**Strength: Medium–High (admin law).** Relevant if research frames directions to consider/formulate standards as public-duty enforcement—without becoming a filing strategy memo.",
    limitations="Service facts; general mandamus doctrine.",
    open_q="1. Mandamus to compel policy formulation vs enforce existing statutory duty—line drawing?",
    strength="Medium-High",
)

add(
    slug="siemens-engineering-1976",
    name="Siemens Engineering & Manufacturing Co. of India Ltd. v. Union of India",
    citation="(1976) 2 SCC 981",
    year="1976",
    bench="Supreme Court (confirm)",
    facts="Challenge related to customs/excise adjudication; need for reasoned quasi-judicial orders.",
    issues="Whether speaking orders are required when rights are affected.",
    holding="The Court emphasised that quasi-judicial authorities must give reasons (classic holding as commonly cited; pin-cites PROVISIONAL).",
    observations="Foundational reasoned-order jurisprudence in Indian administrative law.",
    principles="- Duty to give reasons in quasi-judicial decisions",
    relevance="**Strength: Medium (admin law).** Relevant to reasoned consideration of grievances if non-speaking closures are challenged. Not about OS updates as such.",
    limitations="Tax adjudication facts.",
    open_q="1. Application to pure policy-making vs quasi-judicial grievance disposal?",
    strength="Medium",
)

add(
    slug="punjab-communications-1999",
    name="Punjab Communications Ltd. v. Union of India",
    citation="(1999) 4 SCC 727",
    year="1999",
    bench="Supreme Court (confirm)",
    facts="Dispute involving governmental change of policy affecting the petitioner's expectations.",
    issues="Scope of legitimate expectation in Indian administrative law.",
    holding="The Court discussed legitimate expectation primarily as a procedural doctrine with limited substantive operation (summary PROVISIONAL).",
    observations="Expectation must be carefully founded; not a rigid promise of particular policy outcomes.",
    principles="- Legitimate expectation doctrine (mainly procedural)\n- Limits on substantive expectation",
    relevance="**Strength: Low–Medium (admin law).** Possible supporting vocabulary if State-promoted digitisation creates expectations of end-point security consideration—easy to overstate; keep weak.",
    limitations="Not a digital-security case.",
    open_q="1. Can legitimate expectation attach to unwritten cybersecurity baselines?",
    strength="Low-Medium",
)

add(
    slug="modern-dental-2016",
    name="Modern Dental College and Research Centre v. State of Madhya Pradesh",
    citation="(2016) 7 SCC 353",
    year="2016",
    bench="Constitution Bench (confirm)",
    facts="Challenges to regulations of private professional educational institutions.",
    issues="Standards of constitutional review; proportionality in rights-restricting measures.",
    holding="The Court elaborated proportionality as a tool of constitutional review in the Indian context (summary PROVISIONAL).",
    observations="Structured proportionality analysis for rights limitations.",
    principles="- Proportionality review framework",
    relevance="**Strength: Medium (review method).** Relevant to *future* design of regulations affecting trade under Art. 19(1)(g). Not about current OEM duties.",
    limitations="Education regulation facts.",
    open_q="1. How would proportionality apply to multi-year update mandates vs disclosure-only rules?",
    strength="Medium",
)

add(
    slug="vishaka-1997",
    name="Vishaka v. State of Rajasthan",
    citation="(1997) 6 SCC 241",
    year="1997",
    bench="Supreme Court (confirm)",
    facts="PIL arising from sexual harassment / rape of a social worker; absence of domestic law on workplace sexual harassment at the time.",
    issues="Whether the Court could lay down enforceable guidelines pending legislation.",
    holding="The Court issued guidelines treating them as law until suitable legislation, drawing on international conventions (landmark; pin-cites PROVISIONAL).",
    observations="High-water mark of judicial guideline-making in legislative vacuum—later used cautiously given separation of powers.",
    principles="- Judicial guidelines filling vacuum pending law\n- International law as interpretive aid",
    relevance="**Strength: Low–Medium (method caution).** Cautionary precedent about judicial law-making in vacuums. **Do not** treat as a template to invent multi-year Android update codes by judicial fiat.",
    limitations="Gender justice / workplace facts; extreme care against over-extension.",
    open_q="1. How should later separation-of-powers cautions limit Vishaka-style relief in tech regulation PILs?",
    strength="Low-Medium",
)

add(
    slug="ep-royappa-1974",
    name="E.P. Royappa v. State of Tamil Nadu",
    citation="(1974) 4 SCC 3",
    year="1974",
    bench="Supreme Court (confirm)",
    facts="Service dispute involving alleged arbitrary transfer/treatment of a civil servant.",
    issues="Content of equality under Article 14; arbitrariness.",
    holding="The Court articulated that equality is antithetical to arbitrariness (classic formulation; pin-cites PROVISIONAL).",
    observations="Foundational modern equality/non-arbitrariness discourse.",
    principles="- Non-arbitrariness as equality\n- Article 14 dynamic content",
    relevance="**Strength: High (Art. 14 method).** Central to analysing State regulatory action/inaction for arbitrariness. Does not regulate private OEM support policies directly.",
    limitations="Service jurisprudence origins.",
    open_q="1. Arbitrariness review of regulatory omissions vs positive acts?",
    strength="High",
)


if __name__ == "__main__":
    write_all()
    print("total", len(CASES))
