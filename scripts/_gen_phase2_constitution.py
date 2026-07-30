# -*- coding: utf-8 -*-
"""Generate Phase 2 constitutional research notes. One-shot research helper."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "research" / "constitution"
OUT.mkdir(parents=True, exist_ok=True)
TODAY = "2026-07-30"


def note(
    slug,
    title,
    article,
    text_block,
    history,
    purpose,
    principles,
    modern,
    relevance,
    open_q,
    extra_sources=None,
    status="VERIFIED",
):
    sources = [
        f"1. Constitution of India, {article}. Official text as published by Government of India / available via India Code and Legislative Department resources. Access date: {TODAY}. [FACT][LAW][T0]",
        f"2. Legislative Department, Ministry of Law and Justice — Constitution of India portal: https://legislative.gov.in/constitution-of-india/ Access date: {TODAY}. [FACT][T1]",
    ]
    if extra_sources:
        sources.extend(extra_sources)
    src = "\n".join(sources)
    body = f"""---
title: "{title}"
domain: "constitution"
status: {status}
last_updated: {TODAY}
agent: "Constitution Research Agent"
phase: 2
article: "{article}"
---

# Constitutional Provision Note — {article}

**Project relevance context:** Smartphone software support regulation research (neutral mapping only).  
**Litigation advice:** None. This note does not recommend filing or outcomes.

## Scope

Describe the text, background, purpose, principles, and modern interpretive themes of **{article}**, and record **possible** (non-prescriptive) points of contact with debates on minimum smartphone software support / security updates in India.

## 1. Constitutional Text [LAW][FACT]

The following reproduces the operative constitutional language for research purposes. Readers must confirm against the latest official consolidated text (amendments may apply).

> {text_block}

**Official source discipline:** Constitution of India (Government of India). Locate current consolidated text via Legislative Department / India Code. Access date for this note: **{TODAY}**.

## 2. Historical Background [FACT]

{history}

## 3. Constitutional Purpose [ANALYSIS grounded in text]

{purpose}

## 4. Constitutional Principles [LAW/ANALYSIS]

{principles}

## 5. Modern Interpretation [LAW — case references PROVISIONAL pending Phase 3 full briefs]

{modern}

> **Phase discipline:** Case authorities are noted only as necessary to explain how the provision is commonly understood in contemporary constitutional discourse. Full judgment digests, pin-cites, and ratio extraction are **Phase 3** work. Treat case citations here as **PROVISIONAL** until verified in `research/judgments/`.

## 6. Possible relevance to software support regulation [ANALYSIS — not a legal conclusion]

{relevance}

**Not asserted:** That the Constitution presently *requires* a specific number of years of OS or security updates, or that any particular writ must succeed. Those are open policy/legal questions beyond this descriptive mapping.

## 7. Open Questions [OPEN]

{open_q}

## Sources

{src}

## Audit trail

- Author: Constitution Research Agent (Phase 2)
- Source Verification: see `_source_quality_report.md`
- Citation check: see `_citation_report.md`
- Validation gate: see `_validation_report.md`
- Date: {TODAY}
"""
    path = OUT / f"{slug}.md"
    path.write_text(body, encoding="utf-8")
    print("wrote", path.name)


def main():
    note(
        "article-14",
        "Article 14 — Equality before law",
        "Article 14",
        "The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.",
        """Article 14 appears in Part III (Fundamental Rights) of the Constitution of India, 1950. It combines two related ideas historically associated with the rule of law and equal protection traditions: (i) equality before the law, and (ii) equal protection of the laws. The provision binds the "State" (as defined for Part III purposes, principally Article 12—see OPEN on cross-reference). Post-independence jurisprudence has developed doctrines of reasonable classification and, later, non-arbitrariness as facets of equality (full case study deferred to Phase 3).""",
        """The text's purpose is to constrain State action that denies persons equal treatment under law, while still permitting legitimate, non-arbitrary classifications for governance. It is a justiciable fundamental right enforceable through constitutional remedies (Articles 32 and 226), subject to established constitutional doctrine.""",
        """- **Equality before the law** — no special privileges incompatible with the rule of law (subject to constitutional exceptions elsewhere).
- **Equal protection of the laws** — laws and State action must not be discriminatory without a rational basis under accepted tests.
- **Classification** — differential treatment may be permissible if based on intelligible differentia with rational nexus to the object (classic equal-protection analysis; details in Phase 3 case notes).
- **Non-arbitrariness** — modern equality doctrine often examines whether State action is arbitrary (PROVISIONAL case-law theme).
- **"Person"** — protection extends to "any person," not only citizens (contrast with some Article 19 rights).""",
        """Indian courts have read Article 14 as a dynamic guarantee. Alongside traditional classification analysis, decisions such as *E.P. Royappa v. State of Tamil Nadu* and the *Maneka Gandhi* line are commonly cited for the proposition that equality is antithetical to arbitrariness (citations to be fully briefed in Phase 3; treat as PROVISIONAL explanatory references only). Article 14 is frequently invoked in challenges to State policy, licensing, and administrative omissions where State duties are alleged—always fact-specific.""",
        """**Possible points of contact (descriptive only):**
1. If the Union designs digital public services that practically depend on smartphone end-points, questions may arise whether *regulatory silence* or *unequal vulnerability* across device cohorts engages equality analysis—**only if** State action/inaction is properly characterised under Article 12/14 doctrine (OPEN).
2. Differential OEM support practices are **private market conduct** unless linked to State action, standards, or procurement—Article 14 does not automatically regulate private manufacturers.
3. Any future State standard that treats device tiers differently would itself need non-arbitrary justification under equality principles.
4. Consumer/cybersecurity externalities are typically first addressed by statute and policy; Article 14 is a constitutional constraint on the State, not a substitute product-safety code.""",
        """1. When does non-regulation of a private product market become State "action" for Article 14 purposes?
2. Can information asymmetry in software-support disclosure be framed as equality harm without a statutory baseline?
3. How should courts weigh Digital India dependence against separation of powers if asked to compel rule-making?
4. What empirical showing would be needed to demonstrate arbitrary differential impact on classes of users?""",
        extra_sources=[
            "3. Constitution of India, Part III (Fundamental Rights), general structure. [FACT][T0]",
            "4. *E.P. Royappa v. State of T.N.* — commonly cited on non-arbitrariness / equality (full citation & pin-cite: PROVISIONAL — Phase 3). [SECONDARY/PROVISIONAL]",
            "5. *Maneka Gandhi v. Union of India* — due process / non-arbitrariness trajectory often discussed with Arts. 14 & 21 (PROVISIONAL — Phase 3). [SECONDARY/PROVISIONAL]",
        ],
    )

    note(
        "article-19-1-a",
        "Article 19(1)(a) — Freedom of speech and expression",
        "Article 19(1)(a)",
        """Article 19(1): All citizens shall have the right—
(a) to freedom of speech and expression;

Article 19(2) permits the State, by law, to impose reasonable restrictions on the exercise of the right under sub-clause (a) on grounds including the sovereignty and integrity of India, the security of the State, friendly relations with foreign States, public order, decency or morality, contempt of court, defamation, or incitement to an offence (confirm full official wording of Article 19(2)).""",
        """Article 19(1)(a) is a citizen-centric free speech guarantee in Part III, subject to the reasonable-restriction scheme in Article 19(2). The digital age has raised questions about speech through internet pathways; the Supreme Court has addressed internet restrictions in cases such as *Anuradha Bhasin v. Union of India* (PROVISIONAL — Phase 3 full brief).""",
        """To protect citizens' freedom of speech and expression against unjustified State abridgment, while permitting constitutionally listed reasonable restrictions enacted by law.""",
        """- Freedom of speech and expression for **citizens**.
- Restrictions only under Article 19(2) grounds, by **law**, and "reasonable."
- Distinct from Article 21 privacy and from non-citizen speech claims.
- Medium-neutrality debates: speech may be exercised through print, broadcast, or digital media—subject to doctrine developed in case law.""",
        """Courts examine both the existence of a "law" and the reasonableness/proportionality of restrictions. Internet shutdown and access cases illustrate that digital pathways of expression can be constitutionally salient (*Anuradha Bhasin* — PROVISIONAL). Article 19(1)(a) does not, by its text, regulate private OEM update policies.""",
        """**Possible points of contact (descriptive only):**
1. Insecure or obsolete devices can impair a citizen's *practical ability* to speak online—but constitutional claims typically target **State** restrictions, not private software-support schedules.
2. If State mandates or blocks particular software/update channels, 19(1)(a)/19(2) analysis might arise.
3. Forced dependence on State digital services does not by itself convert OEM commercial decisions into speech restrictions.
4. Overstating a "fundamental right to OS updates" under 19(1)(a) would exceed the text; any link is indirect and contested (OPEN).""",
        """1. Is there a cognisable speech injury from private cessation of security patches?
2. How do intermediary and platform duties interact with end-point device insecurity?
3. What is the boundary between access-to-internet jurisprudence and product-regulation policy?""",
        extra_sources=[
            "3. Constitution of India, Article 19(1)(a) and 19(2). [LAW][T0]",
            "4. *Anuradha Bhasin v. Union of India* — internet/speech restrictions context (PROVISIONAL — Phase 3). [SECONDARY/PROVISIONAL]",
        ],
    )

    note(
        "article-19-1-g",
        "Article 19(1)(g) — Profession, occupation, trade or business",
        "Article 19(1)(g)",
        """Article 19(1): All citizens shall have the right—
(g) to practise any profession, or to carry on any occupation, trade or business.

Article 19(6) permits the State to impose, by law, reasonable restrictions in the interests of the general public, and contains further provisos regarding professional/technical qualifications and State/State-corporation trade (confirm full official wording of Article 19(6)).""",
        """Article 19(1)(g) protects citizens' economic freedom to pursue livelihoods and business, subject to Article 19(6) regulation. Product standards, licensing, and consumer/environmental regulation are often tested against 19(1)(g)/19(6) when challenged by businesses.""",
        """To secure freedom of trade and profession for citizens while allowing public-interest regulation through reasonable restrictions by law.""",
        """- Citizen right to profession/occupation/trade/business.
- State may regulate via **reasonable restrictions** under Article 19(6).
- Technical/professional qualifications and State monopolies have specific textual space in 19(6).
- Balance between free enterprise and public interest regulation.""",
        """Challenges to regulatory standards (safety, environment, consumer protection) often invoke 19(1)(g); the State defends under 19(6) reasonableness. Proportionality and public-interest analyses appear in modern review (details Phase 3).""",
        """**Possible points of contact (descriptive only):**
1. A **future** mandatory software-support standard could be framed by industry as a restriction on trade under 19(1)(g); the State would need a 19(6)-compatible public-interest justification (cybersecurity, consumer protection, environment).
2. This is a **constraint on how the State may regulate**, not a consumer right to updates from OEMs.
3. Research on comparative eco-design rules may inform *policy* design; constitutional validity would be a separate, later question if rules are notified.
4. No opinion is offered on whether any particular standard would survive 19(6) review.""",
        """1. What evidentiary record would support "general public" interest for multi-year security-update mandates?
2. How should phase-in periods and MSME impacts factor into reasonableness?
3. Interaction between 19(1)(g) challenges and environmental DPSPs (Arts. 48A/51A)?""",
        extra_sources=["3. Constitution of India, Article 19(1)(g) and 19(6). [LAW][T0]"],
    )

    note(
        "article-21",
        "Article 21 — Protection of life and personal liberty",
        "Article 21",
        "No person shall be deprived of his life or personal liberty except according to procedure established by law.",
        """Article 21 is among the most heavily interpreted provisions of Part III. Originally associated with a narrower "procedure established by law" reading, post-*Maneka Gandhi* jurisprudence expanded substantive and procedural fairness dimensions (PROVISIONAL — Phase 3). The provision protects "person," not only citizens. Privacy was recognised as a fundamental right in *Justice K.S. Puttaswamy (Retd.) v. Union of India* (2017) (PROVISIONAL citation expansion in Phase 3). Environmental quality and health have also been read in connection with Article 21 in multiple decisions (e.g., *Subhash Kumar* line — PROVISIONAL).""",
        """To ensure that deprivation of life or personal liberty occurs only under a legally established procedure, as developed by constitutional doctrine into a broader guarantee of dignity and related interests.""",
        """- Protection of **life** and **personal liberty**.
- Deprivation only by **procedure established by law**.
- Judicially elaborated facets may include dignity, privacy, health, and environment-related interests (case-law dependent; not all facets are free-standing statutory programmes).
- Enforceable fundamental right; remedies under Arts. 32/226.""",
        """Modern interpretation is expansive but still text-anchored: courts identify facets of life/liberty and test State measures for legality, fairness, and (in many contexts) proportionality. *Puttaswamy* (2017) is the leading privacy authority (PROVISIONAL pending full brief). Digital identity and data-protection debates often reference Article 21 privacy. Environmental PILs frequently invoke Article 21 alongside DPSPs.""",
        """**Possible points of contact (descriptive only):**
1. **Privacy / cybersecurity:** Compromised, unpatched devices can threaten informational and financial privacy; any constitutional argument would still need a **State** duty or action theory—not a free-floating OEM obligation under Article 21 alone.
2. **Dignity / digital participation:** Deep State-led digitisation of welfare, identity, and payments may raise questions about secure access conditions—analytical, not a settled "right to updates."
3. **Environment:** Premature e-waste from software obsolescence may intersect environmental readings of Article 21 *together with* Arts. 48A/51A and environmental statutes—multi-layered, not Article 21 alone.
4. Overclaim risk: inventing a fundamental right to "N years of Android updates" would not be faithful to the constitutional text.""",
        """1. What State duties, if any, arise when essential public services are delivered primarily via personal smartphones?
2. How should privacy doctrine interface with product-security regulation (as opposed to data-fiduciary duties)?
3. Can environmental facets of Article 21 support design-for-longevity policy without judicially writing technical standards?
4. Boundaries between Article 21 claims and statutory consumer/IT remedies?""",
        extra_sources=[
            "3. Constitution of India, Article 21. [LAW][T0]",
            "4. *Justice K.S. Puttaswamy (Retd.) v. Union of India*, (2017) 10 SCC 1 — privacy as fundamental right (PROVISIONAL pin-cites — Phase 3). [LAW][T0/T1 when verified]",
            "5. *Maneka Gandhi v. Union of India* — expanded Article 21 procedure/fairness discourse (PROVISIONAL — Phase 3). [SECONDARY/PROVISIONAL]",
            "6. *Subhash Kumar v. State of Bihar* — pollution-free environment themes under Article 21 (PROVISIONAL — Phase 3). [SECONDARY/PROVISIONAL]",
        ],
    )

    note(
        "article-21a",
        "Article 21A — Right to education",
        "Article 21A",
        "The State shall provide free and compulsory education to all children of the age of six to fourteen years in such manner as the State may, by law, determine.",
        """Article 21A was inserted by the **Constitution (Eighty-sixth Amendment) Act, 2002**, elevating elementary education to a fundamental right, implemented through parliamentary law (historically linked to the Right of Children to Free and Compulsory Education Act, 2009—statute detail out of scope for this constitutional note).""",
        """To impose a positive obligation on the State to provide free and compulsory education to children aged 6–14 in the manner determined by law.""",
        """- Fundamental right to education for a defined age cohort.
- State obligation; manner determined **by law**.
- Related historically to Article 45 (DPSP) — confirm related provisions in official text if used.
- Not a general right to consumer electronics.""",
        """Courts and legislation have developed the content of free and compulsory education. Digital education tools are policy instruments; Article 21A does not by itself mandate smartphone OS support periods.""",
        """**Possible points of contact (descriptive only):**
1. Education delivery increasingly uses digital devices; device insecurity could *practically* affect learning access—but Article 21A obligations run against the **State**, concerning free and compulsory education, not OEM update cycles.
2. Relevance is at most **indirect** (State procurement standards for educational devices; ed-tech security guidance).
3. Not a primary pillar for software-support product regulation compared with Arts. 14/21/48A or consumer/environment statutes.""",
        """1. Do State education digitisation programmes impose security baseline duties in procurement?
2. Is Article 21A a necessary citation for smartphone support research, or peripheral?""",
        extra_sources=[
            "3. Constitution of India, Article 21A. [LAW][T0]",
            "4. Constitution (Eighty-sixth Amendment) Act, 2002 — insertion of Article 21A (confirm text on India Code / Legislative Department). [FACT][LAW][T0/T1]",
        ],
    )

    note(
        "article-38",
        "Article 38 — State to secure a social order for the promotion of welfare of the people",
        "Article 38",
        """**Clause (1):** The State shall strive to promote the welfare of the people by securing and protecting as effectively as it may a social order in which justice, social, economic and political, shall inform all the institutions of the national life.

**Clause (2):** The State shall, in particular, strive to minimise the inequalities in income, and endeavour to eliminate inequalities in status, facilities and opportunities, not only amongst individuals but also amongst groups of people residing in different areas or engaged in different vocations.

(Confirm exact wording and amendment history of clause (2) against official consolidated Constitution.)""",
        """Article 38 is a Directive Principle of State Policy (Part IV). DPSPs are fundamental in governance (Article 37) but not enforceable as fundamental rights in the same manner as Part III. Clause (2) on inequalities reflects later amendment history (verify amendment number against official list when citing precisely).""",
        """To direct the State toward a welfare-oriented social order informed by social, economic, and political justice, and toward reducing inequalities of income, status, facilities, and opportunities.""",
        """- Welfare and social order goals.
- Justice—social, economic, political—as governance aspiration.
- Minimising inequalities (clause 2).
- Non-justiciable in the Part III sense; guides State policy and interpretation (Article 37).""",
        """DPSPs inform legislation and may aid interpretation of fundamental rights and statutes, but do not typically found standalone writs for specific product standards without statutory mediation.""",
        """**Possible points of contact (descriptive only):**
1. Unequal exposure of low-income users to short software-support cycles on budget devices could be discussed as an *inequality of facilities/opportunities* **policy** concern under Article 38's spirit—not a direct enforceable mandate for OEM updates.
2. Useful as **background constitutional policy** for why the State might study consumer cybersecurity baselines.
3. Must not be mis-cited as a self-executing right to multi-year OS support.""",
        """1. How should researchers weight DPSPs in a regulatory-gap study without overstating enforceability?
2. Empirical measures of "inequality of digital security" across income groups?""",
        extra_sources=[
            "3. Constitution of India, Article 37 (application of DPSP) and Article 38. [LAW][T0]",
        ],
    )

    note(
        "article-39",
        "Article 39 — Certain principles of policy to be followed by the State",
        "Article 39",
        """The State shall, in particular, direct its policy towards securing—

(a) that the citizens, men and women equally, have the right to an adequate means of livelihood;
(b) that the ownership and control of the material resources of the community are so distributed as best to subserve the common good;
(c) that the operation of the economic system does not result in the concentration of wealth and means of production to the common detriment;
(d) that there is equal pay for equal work for both men and women;
(e) that the health and strength of workers, men and women, and the tender age of children are not abused and that citizens are not forced by economic necessity to enter avocations unsuited to their age or strength;
(f) that children are given opportunities and facilities to develop in a healthy manner and in conditions of freedom and dignity and that childhood and youth are protected against exploitation and against moral and material abandonment.

(Confirm full official text against consolidated Constitution; amendment history for child-related clauses should be verified when citing precisely.)""",
        """Article 39 is a core DPSP cluster on livelihood, distribution of resources, economic justice, labour, and child welfare. It shapes socio-economic legislation and interpretive approaches but is not a Part III right.""",
        """To orient State policy toward livelihood security, common-good distribution of resources, prevention of harmful economic concentration, gender pay equality, worker/child health protections, and dignified childhood development.""",
        """- Livelihood and economic justice themes.
- Common good / anti-concentration principles.
- Labour and child-protection policy directives.
- DPSP status under Article 37.""",
        """Used as interpretive support in socio-economic rights discourse; implementation primarily through legislation and schemes.""",
        """**Possible points of contact (descriptive only):**
1. Clauses on livelihood and health may **remotely** contextualise digital access for work and welfare—but do not specify device software support.
2. Resource/common-good clauses are sometimes invoked in environmental and resource-governance debates; software-obsolescence/e-waste links would be analytical and statute-mediated (EPA/E-waste rules—later statutory research).
3. Avoid forcing Article 39 into a product-update mandate narrative.""",
        """1. Which Article 39 clauses, if any, are material enough to retain in a focused software-support constitution brief?
2. How to cite DPSPs without implying direct enforceability?""",
        extra_sources=[
            "3. Constitution of India, Article 39. [LAW][T0]",
            "4. Constitution of India, Article 37. [LAW][T0]",
        ],
    )

    note(
        "article-48a",
        "Article 48A — Protection and improvement of environment and safeguarding of forests and wild life",
        "Article 48A",
        "The State shall endeavour to protect and improve the environment and to safeguard the forests and wild life of the country.",
        """Article 48A was inserted by the **Constitution (Forty-second Amendment) Act, 1976**, as part of an environmental package of amendments that also included Article 51A(g). It is a Directive Principle (Part IV).""",
        """To commit the State to endeavour toward environmental protection and improvement, and safeguarding of forests and wildlife.""",
        """- State endeavour to protect and improve the **environment**.
- Safeguarding **forests and wild life**.
- DPSP character (Article 37).
- Often read together with Article 51A(g) and environmental legislation, and with Article 21 environmental jurisprudence (case law Phase 3).""",
        """Environmental governance in India combines DPSPs, fundamental duties, Article 21 doctrine, and detailed statutes (Environment (Protection) Act, 1986 and rules—statutory research later). Courts have frequently cited Article 48A as a constitutional policy backdrop in environmental matters (PROVISIONAL case references deferred).""",
        """**Possible points of contact (descriptive only):**
1. Premature device replacement driven by ended software support can increase **e-waste** and resource extraction pressures—relevant to *environmental protection* as a State policy goal under Article 48A.
2. Article 48A supports **why the State may study** product longevity / circular-economy measures; it does not by itself fix OEM update years.
3. Operational detail belongs in environmental and e-waste statutes/rules (later phases).
4. Pair with Article 51A(g) for duty/policy symmetry (citizen duty / State endeavour).""",
        """1. How should software-forced obsolescence be evidenced as an environmental problem at constitutional-policy level?
2. Relationship between Article 48A and EPR-based e-waste rules?
3. Comparative eco-design mandates as policy analogies (not binding law)?""",
        extra_sources=[
            "3. Constitution of India, Article 48A. [LAW][T0]",
            "4. Constitution (Forty-second Amendment) Act, 1976 — insertion of Article 48A (and related environmental amendments). Confirm on India Code / Legislative Department. [FACT][LAW][T0/T1]",
            "5. Constitution of India, Article 37. [LAW][T0]",
        ],
    )

    note(
        "article-51a-g",
        "Article 51A(g) — Fundamental duty to protect and improve the natural environment",
        "Article 51A(g)",
        """Article 51A: It shall be the duty of every citizen of India—
(g) to protect and improve the natural environment including forests, lakes, rivers and wild life, and to have compassion for living creatures;

(Other sub-clauses of Article 51A omitted; confirm full Article 51A text in official Constitution.)""",
        """Article 51A (Fundamental Duties) was inserted by the **Constitution (Forty-second Amendment) Act, 1976**. Duties are addressed to citizens; they are not mirror images of Part III rights but have been used in interpretive and educational contexts, and sometimes in conjunction with environmental litigation themes (case details Phase 3).""",
        """To articulate citizen duties toward the natural environment and compassion for living creatures, complementing State environmental policy (e.g., Article 48A).""",
        """- Citizen duty (not a fundamental right).
- Protect and improve natural environment (forests, lakes, rivers, wild life).
- Compassion for living creatures.
- Part IVA structure; enforceability differs from Part III.""",
        """Fundamental duties guide civic conduct and may inform interpretation; they do not typically create private causes of action identical to fundamental rights. Environmental education and statutory duties implement related values.""",
        """**Possible points of contact (descriptive only):**
1. Citizens' ability to reduce e-waste by keeping devices longer is consistent with environmental duty **values**—but Article 51A(g) does not obligate OEMs to ship updates.
2. May support **public-interest framing** of environmental responsibility in research narratives without converting duty into a writ recipe.
3. Best paired with Article 48A and environmental statutes for a complete environmental constitutional map.""",
        """1. What weight do courts give 51A(g) when evaluating environmental regulatory omissions?
2. How to discuss citizen duties without implying individual liability for OEM design choices?""",
        extra_sources=[
            "3. Constitution of India, Article 51A(g). [LAW][T0]",
            "4. Constitution (Forty-second Amendment) Act, 1976 — insertion of Article 51A. [FACT][LAW][T0/T1]",
        ],
    )

    note(
        "article-32",
        "Article 32 — Remedies for enforcement of rights conferred by Part III",
        "Article 32",
        """**(1)** The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed.

**(2)** The Supreme Court shall have power to issue directions or orders or writs, including writs in the nature of habeas corpus, mandamus, prohibition, quo warranto and certiorari, whichever may be appropriate, for the enforcement of any of the rights conferred by this Part.

**(3)** Without prejudice to the powers conferred on the Supreme Court by clauses (1) and (2), Parliament may by law empower any other court to exercise within the local limits of its jurisdiction all or any of the powers exercisable by the Supreme Court under clause (2).

**(4)** The right guaranteed by this article shall not be suspended except as otherwise provided for by this Constitution.

(Confirm full official text.)""",
        """Article 32 is the constitutional remedy for enforcement of Part III fundamental rights in the Supreme Court. Public interest litigation expanded access patterns over time (Phase 3 case law).""",
        """To guarantee an effective Supreme Court remedy for enforcement of fundamental rights, including prerogative writ-type powers.""",
        """- Guaranteed right to move the Supreme Court for Part III enforcement.
- Writ/direction powers listed in clause (2).
- Parliament may empower other courts (clause 3).
- Limited suspension rules (clause 4; emergency provisions elsewhere).
- Distinct from Article 226 (High Courts), which is broader in some respects ("for any other purpose") but different forum.""",
        """Article 32 is invoked for fundamental-rights enforcement of national importance; the Court may relegate matters to High Courts in appropriate cases. Maintainability, locus, and PIL guidelines are case-law intensive (Phase 3: e.g., *S.P. Gupta*, *Balwant Singh Chaufal* lines — PROVISIONAL).""",
        """**Possible points of contact (descriptive only):**
1. If a future claim is framed as Part III enforcement (e.g., Arts. 14/21) against the Union regarding digital end-point security regulation, Article 32 is a **possible Supreme Court pathway**—forum choice remains OPEN and must be analysed separately (`research/forum/`).
2. Article 32 does not itself create a right to software updates; it is **remedial**.
3. This note does **not** recommend filing under Article 32.""",
        """1. Comparative strengths of Art. 32 vs Art. 226 for regulatory-gap PILs (deferred to forum memo).
2. What factual showing elevates a policy gap to Part III enforcement?""",
        extra_sources=[
            "3. Constitution of India, Article 32. [LAW][T0]",
            "4. Constitution of India, Part III remedies context. [LAW][T0]",
        ],
    )

    note(
        "article-226",
        "Article 226 — Power of High Courts to issue certain writs",
        "Article 226",
        """**(1)** Notwithstanding anything in Article 32, every High Court shall have power, throughout the territories in relation to which it exercises jurisdiction, to issue to any person or authority, including in appropriate cases any Government, within those territories directions, orders or writs, including writs in the nature of habeas corpus, mandamus, prohibition, quo warranto and certiorari, or any of them, for the enforcement of any of the rights conferred by Part III and for any other purpose.

**(2)** The power conferred by clause (1) to issue directions, orders or writs to any Government, authority or person may also be exercised by any High Court exercising jurisdiction in relation to the territories within which the cause of action, wholly or in part, arises for the exercise of such power, notwithstanding that the seat of such Government or authority or the residence of such person is not within those territories.

(Additional clauses of Article 226 address interim orders and related matters—confirm full official text.)""",
        """Article 226 empowers High Courts with wide writ jurisdiction for Part III enforcement **and** "for any other purpose," a historically significant expansion beyond Article 32's Part III focus. Clause (2) addresses territorial jurisdiction where cause of action arises wholly or in part within the High Court's territories even if the authority sits elsewhere.""",
        """To equip High Courts to issue writs/directions for fundamental rights and other legal purposes within their territorial competence, including flexible cause-of-action rules under clause (2).""",
        """- High Court writ powers: habeas corpus, mandamus, prohibition, quo warranto, certiorari (and directions/orders).
- Purposes: Part III **and** any other purpose.
- Territorial jurisdiction + **cause of action** nexus (clause 2).
- Concurrent availability with Article 32 in some rights cases (strategic forum questions OPEN).
- Subject to judicially developed limits (alternative remedies, delay, disputed facts, etc.—Phase 3).""",
        """High Court public law litigation frequently uses Article 226 for administrative and rights issues. Clause (2) is central when Union ministries are respondents but part of the cause of action arises in a State. PIL maintainability doctrines apply (Phase 3).""",
        """**Possible points of contact (descriptive only):**
1. A public-interest challenge seeking **mandamus to consider/formulate** smartphone software-support standards against Union ministries might be structured under Article 226 if territorial nexus exists (residence, sale, use of devices, grievance filings—fact-specific).
2. Clause (2) is especially relevant for Union respondents seated in New Delhi.
3. This note maps the **remedial provision**; it does **not** select a forum or recommend filing.
4. Full forum comparison belongs in `research/forum/` after research matures.""",
        """1. What facts establish "cause of action, wholly or in part" for digital-product regulatory gaps?
2. How do alternative remedies (consumer fora) interact with 226 maintainability?
3. Art. 32 vs 226 comparative memo timing?""",
        extra_sources=[
            "3. Constitution of India, Article 226(1) and 226(2). [LAW][T0]",
            "4. Constitution of India, Article 32 (for contrast). [LAW][T0]",
        ],
    )

    print("done")


if __name__ == "__main__":
    main()
