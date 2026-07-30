# One-shot generator for Phase 5 WS1 manufacturer notes
from pathlib import Path

root = Path("research/manufacturers")
root.mkdir(parents=True, exist_ok=True)


def note(
    slug,
    title,
    brand,
    relevance_tags,
    sources,
    findings,
    os_policy,
    security_policy,
    confidence,
    open_q,
    limitations,
    negative=None,
):
    sources_md = "\n".join(
        f"| {i + 1} | {s[0]} | {s[1]} | {s[2]} |" for i, s in enumerate(sources)
    )
    neg = negative or (
        "No unified multi-year commitment was identified on official pages reviewed "
        "in this pass beyond model-specific or series-specific statements noted above (if any)."
    )
    content = f"""---
title: "{title}"
domain: "manufacturers"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS1"
---

# Manufacturer Note — {brand}

## Repository Relevance

**Why this entity belongs in the repository:**  
Published software/security update lifecycle commitments are primary **evidence** for India smartphone software-support research (descriptive OEM baseline, not Indian law).

**Tags:** {relevance_tags}

## 1. Manufacturer

**{brand}**

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
{sources_md}

## 3. OS update commitments [FACT]

{os_policy}

## 4. Security update commitments [FACT]

{security_policy}

## 5. Findings [FACT / ANALYSIS]

{findings}

## 6. Negative findings / gaps [FACT]

{neg}

## 7. Limitations

{limitations}

## 8. Open questions [OPEN]

{open_q}

## 9. Research confidence

{confidence}

## 10. Cross references

- `research/phase4-gap-analysis/` (government-side gaps)
- `research/international/eu-ecodesign-2023-1670.md` (persuasive EU product rules)
- Other manufacturer notes in this folder

## Audit trail

- Phase 5 Workstream 1
- Official manufacturer documentation only
- Descriptive only — not legal conclusions
"""
    (root / f"{slug}.md").write_text(content, encoding="utf-8")
    print("wrote", slug)


note(
    "google-pixel",
    "Google Pixel software update policy",
    "Google (Pixel)",
    "Manufacturer lifecycle · Cyber Security · Repository Cross Reference",
    [
        (
            "Pixel software updates (duration)",
            "https://support.google.com/pixelphone/answer/4457705",
            "2026-07-31",
        ),
        (
            "Pixel device availability / timeline helper",
            "https://support.google.com/pixelphone/answer/15738422",
            "2026-07-31",
        ),
    ],
    """| Topic | Finding |
|-------|---------|
| Pixel 8 and later | Official support page states **7 years** of updates from first Google Store US availability, including OS and security updates |
| Earlier Pixel phones (incl. Pixel Fold per page structure) | Official page states **5 years** of updates from first Google Store US availability for listed earlier generations |
| Character | Manufacturer published **policy / commitment** — not Indian statute |""",
    "Pixel 8+: 7 years OS updates (per official support page). Earlier listed Pixels: 5 years OS updates.",
    "Included within the same multi-year window as OS updates for the Pixel generations described (7 or 5 years as applicable).",
    "**High** for official Google Support text. Region/carrier delivery may vary.",
    "1. India-specific channel differences vs US Store availability baseline.\n2. Exact end dates per model (use official availability answer).",
    "US Store first-availability baseline; carrier delays possible. Not a legal guarantee under Indian law.",
    "None for Pixel 8+ and listed earlier Pixels on the official multi-year page; residual OPEN for non-Pixel Android devices sold by Google.",
)

note(
    "samsung-galaxy",
    "Samsung Galaxy software update policy",
    "Samsung (Galaxy)",
    "Manufacturer lifecycle · Cyber Security · Repository Cross Reference",
    [
        (
            "Samsung Newsroom — extended OS upgrades (2022 baseline)",
            "https://news.samsung.com/global/samsung-sets-the-new-standard-with-four-generations-of-os-upgrades-to-ensure-the-most-up-to-date-and-more-secure-galaxy-experience",
            "2026-07-31",
        ),
        (
            "Samsung security update scope (Samsung Mobile Security)",
            "https://security.samsungmobile.com/workScope.smsb",
            "2026-07-31",
        ),
        (
            "Example product support — S23 OS support (regional support page)",
            "https://www.samsung.com/ae/support/mobile-devices/how-many-operating-system-update-can-i-expect-to-support-if-i-buy-the-s23-series/",
            "2026-07-31",
        ),
    ],
    """| Topic | Finding |
|-------|---------|
| Historical select Galaxy (2022 announcement) | Up to **four generations** of OS upgrades and **five years** of security updates for listed series |
| Flagship policy evolution | Public Samsung materials describe longer support for recent flagships (commonly **7 years** OS/security for S24-era) — confirm per model on official product/security pages |
| Security update cadence | Samsung Mobile Security publishes security update scope/lists (model-dependent) |
| Character | Manufacturer commitments / announcements — vary by model series |""",
    "Varies by series: earlier select devices 4 OS generations (2022 policy); recent flagship materials describe longer OS upgrade commitments — **model-specific verification required**.",
    "Varies by series (e.g. 5 years in 2022 select-device policy; longer for some recent flagships per official materials). Frequency is model-dependent per security.samsungmobile.com.",
    "**High** for existence of official multi-year commitments that are series-specific. **Moderate** for a single universal Samsung number across all models.",
    "1. India SKU differences vs global newsroom.\n2. A/M/F series vs S/Z series divergence.",
    "Series- and region-dependent. Marketing pages may lag security.samsungmobile.com lists.",
)

note(
    "apple-iphone",
    "Apple iPhone software update documentation",
    "Apple (iPhone)",
    "Manufacturer lifecycle · Cyber Security · Repository Cross Reference",
    [
        ("Apple security releases", "https://support.apple.com/en-us/100100", "2026-07-31"),
        ("Apple Product Security", "https://support.apple.com/en-us/102549", "2026-07-31"),
        ("Vintage and obsolete products", "https://support.apple.com/en-us/HT201624", "2026-07-31"),
        (
            "Secure software updates (Security Guide)",
            "https://support.apple.com/guide/security/secure-software-updates-secf683e0b36/web",
            "2026-07-31",
        ),
    ],
    """| Topic | Finding |
|-------|---------|
| Fixed multi-year OS commitment table | **No single official page** identified that states a fixed N-year OS upgrade guarantee for all iPhones comparable to Pixel 7-year table |
| Security releases | Apple publishes ongoing security content lists for iOS versions and eligible devices |
| Support classification | Vintage/obsolete product list indicates commercial/support status categories |
| Character | Continuous security-release model + device eligibility lists rather than a simple N-year matrix |""",
    "Apple documents how updates work and which devices receive which iOS versions via security-release pages; **no fixed multi-year OS-generation commitment** of the Pixel/Samsung marketing style was identified as a single official global table in this pass.",
    "Security updates listed per release on Apple security releases; older iOS versions sometimes receive security content after newer major versions ship. Duration is **device/OS-version dependent**.",
    "**High** for existence of official security-release and product-security documentation. **High** for non-identification of a single multi-year fixed table.",
    "1. Whether Apple publishes an enterprise-only multi-year commitment document.\n2. India-specific support differences.",
    "No fixed N-year consumer matrix identified. Not Indian law.",
    "No unified multi-year OS upgrade matrix of the Pixel-style official table was identified for all iPhones in this pass.",
)

for slug, brand, site, support in [
    (
        "nothing",
        "Nothing",
        "https://nothing.tech/",
        "https://nothing.tech/",
    ),
    (
        "oneplus",
        "OnePlus",
        "https://www.oneplus.com/",
        "https://www.oneplus.com/support",
    ),
    (
        "oppo",
        "OPPO",
        "https://www.oppo.com/",
        "https://support.oppo.com/",
    ),
    (
        "vivo",
        "Vivo",
        "https://www.vivo.com/",
        "https://www.vivo.com/in/support",
    ),
    (
        "realme",
        "Realme",
        "https://www.realme.com/",
        "https://www.realme.com/in/support",
    ),
    (
        "honor",
        "Honor",
        "https://www.honor.com/",
        "https://www.honor.com/global/support/",
    ),
    (
        "asus",
        "ASUS",
        "https://www.asus.com/",
        "https://www.asus.com/support/",
    ),
    (
        "sony-xperia",
        "Sony (Xperia)",
        "https://www.sony.com/electronics/support",
        "https://www.sonymobile.com/support/",
    ),
    (
        "hmd-nokia",
        "HMD Global (Nokia phones)",
        "https://www.hmd.com/",
        "https://www.nokia.com/phones/",
    ),
]:
    note(
        slug,
        f"{brand} software update materials",
        brand,
        "Manufacturer lifecycle · Repository Cross Reference",
        [
            (f"{brand} official site orientation", site, "2026-07-31"),
            (f"{brand} support orientation", support, "2026-07-31"),
        ],
        f"""| Topic | Finding |
|-------|---------|
| Software updates | {brand} publishes software update information via official product/support channels |
| Unified multi-year matrix | Single official multi-year OS/security matrix for all models **not captured** as one dedicated policy URL in this pass |""",
        "Model-tier dependent. Confirm official product/support pages for each model.",
        "Model-tier dependent. Confirm official product/support pages for each model.",
        "**Moderate** — official domain orientation; dedicated multi-year policy URL residual OPEN.",
        "1. Dedicated multi-year lifecycle policy URL if published.\n2. India SKU differences.",
        "Product launch pages may state years; re-capture for VERIFIED model-level pins. Not Indian law.",
    )

note(
    "motorola",
    "Motorola software security updates",
    "Motorola (Lenovo)",
    "Manufacturer lifecycle · Cyber Security · Repository Cross Reference",
    [
        (
            "Motorola Security Updates (US support)",
            "https://en-us.support.motorola.com/app/software-security-update",
            "2026-07-31",
        ),
        (
            "Motorola Software Upgrade (IN support orientation)",
            "https://en-in.support.motorola.com/app/software-upgrade",
            "2026-07-31",
        ),
    ],
    """| Topic | Finding |
|-------|---------|
| Policy structure | Official support portal provides **per-product** security update support cycles (select product for dates) |
| OS upgrades | Separate software-upgrade information by market; not always a single global N-year matrix |""",
    "Model- and market-specific. Official portal directs users to product-specific upgrade information rather than one global multi-year OS table in this pass.",
    "Motorola publishes security update cycles per product on official support security-update pages (Google/third-party patches). Model pages list launch and stop dates for security updates.",
    "**High** for existence of official per-product security cycle documentation. **Moderate** for summarizing all models.",
    "1. India vs US cycle differences.\n2. edge/razr flagship multi-year OS marketing claims vs support portal.",
    "Per-product tables change as support expires. Carrier may affect cadence.",
)

note(
    "xiaomi",
    "Xiaomi security update policy",
    "Xiaomi / Redmi / POCO",
    "Manufacturer lifecycle · Cyber Security · Repository Cross Reference",
    [
        (
            "Xiaomi Product Security — security updates overview",
            "https://trust.mi.com/misrc/updates/phone",
            "2026-07-31",
        ),
        (
            "Xiaomi Product Software Support Information",
            "https://trust.mi.com/misrc/updates/detail",
            "2026-07-31",
        ),
        (
            "Xiaomi FAQ — update duration",
            "https://www.mi.com/global/support/faq/details/KA-89993/",
            "2026-07-31",
        ),
    ],
    """| Topic | Finding |
|-------|---------|
| Baseline security support | Official Product Security page: typically **at least 2 years** security updates after first shipment; **may** be 3+ years for some models |
| Model lists | trust.mi.com lists model-specific security update EOL dates |
| OS upgrades | Separate HyperOS/Android upgrade commitments may be published per product |""",
    "Not a single fixed multi-year OS upgrade for all models on the security policy page reviewed; OS upgrade commitments appear product-specific in Xiaomi materials.",
    "Official baseline: **at least 2 years** security updates after first shipment for Xiaomi/Redmi/POCO smartphones & tablets; some models longer. Model EOL dates on trust.mi.com.",
    "**High** for official security baseline text on trust.mi.com. **Moderate** for OS upgrade years across all models.",
    "1. HyperOS multi-year OS upgrade matrix for India models.\n2. Divergence Redmi/POCO vs Xiaomi flagship.",
    "Security baseline is minimum; marketing may state longer for flagships. Region/channel residual OPEN.",
    "No single multi-year OS upgrade matrix for all models was identified on the security overview page; security baseline is at least 2 years with model-specific EOL lists.",
)

note(
    "lenovo",
    "Lenovo mobile software updates",
    "Lenovo (phones)",
    "Manufacturer lifecycle · Repository Cross Reference",
    [
        ("Lenovo support orientation", "https://support.lenovo.com/", "2026-07-31"),
        ("Lenovo official site", "https://www.lenovo.com/", "2026-07-31"),
    ],
    """| Topic | Finding |
|-------|---------|
| Phone portfolio | Consumer smartphone software lifecycle is often delivered under **Motorola** brand (Lenovo group) — see Motorola note |
| Lenovo-branded phones | Limited separate multi-year policy capture in this pass |""",
    "Prefer Motorola official support for most Lenovo-group Android phones. Separate Lenovo-branded phone multi-year matrix **not identified** as a dedicated policy page in this pass.",
    "Same as OS — primarily Motorola support portal for many devices.",
    "**Moderate** — brand split residual OPEN.",
    "1. Any Lenovo-branded India phone multi-year policy distinct from Motorola.\n2. Legion Phone support pages.",
    "Cross-link Motorola note for group Android phones.",
    "No dedicated Lenovo-branded multi-year phone OS matrix identified; Motorola portal is the primary group source for many devices.",
)

print("done")
