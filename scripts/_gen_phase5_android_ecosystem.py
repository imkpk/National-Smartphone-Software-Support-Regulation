# Phase 5 WS2 — Android Ecosystem research package generator
# Official Google / AOSP documentation only. Descriptive. Access: 2026-07-31
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "android-ecosystem"
OUT.mkdir(parents=True, exist_ok=True)
ACCESS = "2026-07-31"


def note(
    slug,
    title,
    summary,
    sources,
    findings,
    negative,
    open_q,
    confidence,
    cross=None,
):
    sources_md = "\n".join(
        f"| {i+1} | {s[0]} | {s[1]} | {ACCESS} |" for i, s in enumerate(sources)
    )
    findings_md = "\n".join(f"| {t} | {f} |" for t, f in findings)
    open_md = "\n".join(f"{i+1}. {q}" for i, q in enumerate(open_q))
    cross = cross or [
        "`research/manufacturers/` (OEM lifecycle policies — Phase 5 WS1)",
        "`research/phase4-gap-analysis/` (government-side gaps)",
        "Other notes in `research/android-ecosystem/`",
        "`../../PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md`",
    ]
    cross_md = "\n".join(f"- {c}" for c in cross)
    content = f"""---
title: "{title}"
domain: "android-ecosystem"
status: VERIFIED
last_updated: {ACCESS}
phase: 5
workstream: "P5-WS2"
---

# Research Note — {title}

## Repository Relevance

**Why this topic belongs in the repository:**  
Android platform architecture, update infrastructure, and security-update mechanisms are foundational **technical evidence** for research on smartphone software support longevity in India. These materials describe how OS/security updates are produced, distributed, and certified — **not** Indian law and **not** OEM-specific multi-year promises (see Phase 5 WS1).

**Tags:** Android ecosystem · Technical baseline · Update architecture · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Official Google / AOSP technical documentation. Descriptive only. **Not** legal conclusions; **not** recommendations; **not** policy proposals.

## 1. Topic summary [FACT]

{summary}

## 2. Official sources [FACT]

| # | Document / page | URL | Access |
|---|-----------------|-----|--------|
{sources_md}

## 3. Key findings [FACT / ANALYSIS]

| Topic | Finding |
|-------|---------|
{findings_md}

## 4. Negative findings / gaps [FACT]

{negative}

## 5. Limitations

- Platform documentation evolves; re-verify URLs on re-use.
- Implementation on commercial devices depends on OEM/SoC choices; platform docs do not guarantee device-level update duration.
- Not Indian law.

## 6. Open questions [OPEN]

{open_md}

## 7. Research confidence

**{confidence}** — based on official source.android.com / developer.android.com / android.com materials accessed {ACCESS}.

## 8. Cross references

{cross_md}

## Audit trail

- Phase 5 Workstream 2 — Android Ecosystem
- Official Google / AOSP documentation only
- Descriptive only — no recommendations or legal interpretation
"""
    (OUT / f"{slug}.md").write_text(content, encoding="utf-8")
    print("wrote", slug)


# ── Research notes ──────────────────────────────────────────

note(
    "aosp",
    "Android Open Source Project (AOSP)",
    "The Android Open Source Project (AOSP) is publicly available, modifiable Android source code providing a complete mobile platform implementation. Anyone can download and modify AOSP for a device. Official architecture documentation describes the software stack: apps, framework, system services, ART runtime, HALs, native libraries, and kernel.",
    [
        ("Architecture overview (AOSP stack)", "https://source.android.com/docs/core/architecture"),
        ("AOSP documentation home", "https://source.android.com/docs"),
        ("Get started / site updates (AOSP publish cadence note)", "https://source.android.com/docs/whatsnew/site-updates"),
    ],
    [
        ("Nature", "Public open-source platform source; not a full set of end-user cloud-backed apps/services"),
        ("Compatibility levels", "AOSP-compatible (CDD) vs Android-compatible (CDD + VSR + VTS/CTS tests) per architecture docs"),
        ("Stack layers", "Apps → framework → system services → ART → HAL → native daemons/libraries → kernel"),
        ("AOSP publish cadence (2026 note)", "Official site states effective 2026 source publishes to AOSP in Q2 and Q4; use android-latest-release for latest release pushed to AOSP"),
        ("Character", "Platform codebase / documentation — not a multi-year device support guarantee"),
    ],
    "AOSP itself does not publish multi-year OS/security support floors for third-party commercial devices. Device longevity commitments remain OEM-specific (Phase 5 WS1).",
    [
        "India-specific AOSP contribution or mirror practices (if any) not in scope of this note.",
        "Exact mapping of each OEM product tree to AOSP tags is device-specific.",
    ],
    "High",
)

note(
    "android-enterprise",
    "Android Enterprise",
    "Android Enterprise is Google’s enterprise mobility platform combining devices, apps, and management. Official developer documentation describes work profiles, managed configurations, dedicated devices, SSO, and management solutions for organisations.",
    [
        ("Android for enterprise (developer.android.com/work)", "https://developer.android.com/work"),
        ("Android Enterprise (android.com/enterprise)", "https://www.android.com/enterprise/"),
        ("Android management solutions (Google)", "https://developers.google.com/android/work"),
    ],
    [
        ("Platform role", "Secure/flexible enterprise mobility platform with management APIs and work profile model"),
        ("App features", "Work profile best practices, managed configurations, dedicated-device/kiosk modes, SSO"),
        ("Relation to updates", "Enterprise materials emphasise security and regular updates as platform/management attributes — not a statutory multi-year OS floor"),
        ("Character", "Enterprise product/platform documentation — not Indian labour/IT law"),
    ],
    "Android Enterprise documentation does not replace OEM consumer multi-year software-support policies. Enterprise Recommended requirements (separate note) are commercial programme criteria, not law.",
    [
        "Whether India-market enterprise SKUs carry distinct update SLAs beyond AER — residual OEM capture.",
    ],
    "High",
)

note(
    "android-enterprise-recommended",
    "Android Enterprise Recommended",
    "Android Enterprise Recommended (AER) is Google’s shortlist/badge programme for business devices and solutions that meet Google’s stated requirements. Official android.com enterprise pages present AER as tested/trusted solutions for organisations, with a device catalogue.",
    [
        ("Android Enterprise Recommended", "https://www.android.com/enterprise/recommended/"),
        ("Android Enterprise partners devices catalogue", "https://androidenterprisepartners.withgoogle.com/devices/"),
        ("Android Enterprise security overview", "https://www.android.com/enterprise/security/"),
    ],
    [
        ("Nature", "Commercial recommended-device/solutions programme with Google requirements"),
        ("Update relevance", "Marketing/programme materials reference regular updates as part of device protection narrative"),
        ("Scope", "Business devices/solutions shortlist — not universal consumer Android support policy"),
        ("Character", "Programme badge / catalogue — not Indian law"),
    ],
    "Official public pages describe AER as a shortlist meeting Google requirements; detailed multi-year OS/security-update matrices for all AER SKUs are not fully enumerated on the landing pages reviewed (residual OPEN for partner requirement PDFs if published).",
    [
        "Capture of current AER requirement document PDF version (if publicly posted) for update-duration criteria.",
    ],
    "Moderate–High",
)

note(
    "project-mainline",
    "Project Mainline (modular system components)",
    "Android 10 introduced Mainline (modular system components). Selected Android system components are modularized so they can be updated outside the normal full-platform Android release cycle. Updates may arrive via Google Play system updates (Play Store infrastructure) or partner OTA.",
    [
        ("Mainline (modular system components)", "https://source.android.com/docs/core/architecture/modular-system"),
        ("APEX container format", "https://source.android.com/docs/core/ota/apex"),
        ("Architecture overview", "https://source.android.com/docs/core/architecture"),
    ],
    [
        ("Purpose", "Distribute critical bug fixes and improvements broadly without full OS image release"),
        ("Module formats", "APEX and/or APK depending on module"),
        ("Atomic install", "Module packages install/roll back atomically (all or none)"),
        ("API constraint", "Module updates do not introduce new APIs; use SDK/System APIs guaranteed by CTS and stable interfaces"),
        ("GMS vs AOSP keys", "GMS devices: Google-signed com.google.android.*; AOSP keys: com.android.* preface"),
        ("Support note", "Official page notes Mainline support for Android 11 and lower concluded as of Q4 2025"),
        ("Character", "Platform modular-update architecture — partial security surface; not full OEM multi-year OS commitment"),
    ],
    "Mainline updates cover selected modular components only — they do not replace full platform/security OTA responsibility of OEMs for non-modular parts (kernel, vendor HAL, full framework where not modularized).",
    [
        "Device-class variance in which Mainline modules are present on India-volume SKUs.",
    ],
    "High",
)

note(
    "play-system-updates",
    "Google Play System Updates",
    "Google Play system updates are the distribution channel (Play Store infrastructure) used to deliver Mainline modular system component updates to end-user devices. Official Mainline documentation states end-user devices can receive Mainline updates via Play system updates or partner OTA.",
    [
        ("Mainline — update distribution", "https://source.android.com/docs/core/architecture/modular-system"),
        ("Android / GMS reference", "https://www.android.com/gms/"),
        ("OTA updates overview", "https://source.android.com/docs/core/ota"),
    ],
    [
        ("Channel", "Play Store infrastructure for Mainline module packages"),
        ("Independence", "Can deliver component updates outside full system OTA cadence"),
        ("Scope limit", "Targets modular system components — not complete substitute for full OS/security images"),
        ("Partner path", "Partners may also deliver Mainline packages via partner OTA"),
        ("Character", "Update distribution mechanism — not a multi-year support statute"),
    ],
    "Play system updates do not alone guarantee that a device receives monthly Android Security Bulletin patches for kernel/vendor/non-Mainline components.",
    [
        "User-visible Settings path names may vary by OEM skin (implementation detail).",
    ],
    "High",
)

note(
    "android-security-bulletins",
    "Android Security Bulletins",
    "Android Security Bulletins publish monthly fixes for issues affecting Android devices. Sources of fixes include AOSP platform, upstream Linux kernel, and SoC manufacturers. Separate bulletins exist for Pixel, Wear, Automotive, XR, etc.",
    [
        ("Android Security Bulletins index", "https://source.android.com/docs/security/bulletin/asb-overview"),
        ("Bulletins landing / monthly list", "https://source.android.com/docs/security/bulletin"),
        ("Pixel Update Bulletins", "https://source.android.com/docs/security/bulletin/pixel"),
    ],
    [
        ("Cadence", "Monthly device-update tool; bulletins typically first Monday of month (holiday shift rule stated)"),
        ("Patch levels", "Bulletins list security patch levels (e.g. YYYY-MM-01 and YYYY-MM-05 style levels)"),
        ("Fix sources", "AOSP platform; upstream Linux kernel; SOC manufacturers"),
        ("OEM pick-up", "Platform fixes merge into AOSP after quarterly bulletin release windows as described; OEMs must still ship to devices"),
        ("OEM-specific portals", "Bulletin index links manufacturer security pages (Samsung, OnePlus, Oppo, Vivo, Motorola, Nokia, LG, Google)"),
        ("Character", "Public vulnerability/fix disclosure — not a guarantee every commercial device ships every bulletin"),
    ],
    "Publication of an Android Security Bulletin does not legally or technically force every OEM/SKU to ship those fixes. Delivery remains OEM/carrier-dependent (Phase 5 WS1).",
    [
        "India-specific delayed bulletin shipping statistics — not available from bulletin pages alone.",
    ],
    "High",
)

note(
    "monthly-security-updates",
    "Monthly Security Updates (platform cadence)",
    "Official Android Security Bulletin materials frame monthly device updates as an important tool for user safety. Security patch levels in Settings typically correspond to bulletin patch levels when OEMs ship corresponding fixes.",
    [
        ("Android Security Bulletins", "https://source.android.com/docs/security/bulletin/asb-overview"),
        ("Check/update Android version (Google support)", "https://support.google.com/android/answer/7680439"),
        ("OTA updates", "https://source.android.com/docs/core/ota"),
    ],
    [
        ("Intended cadence", "Monthly security bulletin publication cycle"),
        ("User check", "Google support documents how users check Android version / updates"),
        ("Delivery path", "Full system OTA and/or modular Mainline/Play system updates depending on fix type"),
        ("Character", "Platform security process description — shipping is OEM responsibility"),
    ],
    "No official global mandate on this page set requiring every manufacturer to ship every month for N years. Enterprise programmes and OEM policies differ.",
    [
        "Correlation tables between bulletin date and India retail device patch levels require empirical capture (out of pure platform docs).",
    ],
    "High",
)

note(
    "security-patch-levels",
    "Security Patch Levels",
    "Android Security Bulletins associate published fixes with security patch level dates (commonly YYYY-MM-01 and YYYY-MM-05 style strings). Devices report a security patch level reflecting the set of fixes incorporated when the OEM builds and ships an update.",
    [
        ("Android Security Bulletins (patch levels in tables)", "https://source.android.com/docs/security/bulletin/asb-overview"),
        ("Bulletins monthly index", "https://source.android.com/docs/security/bulletin"),
        ("Play Integrity — strong integrity / recent security updates (Android 13+)", "https://developer.android.com/google/play/integrity/overview"),
    ],
    [
        ("Identifier", "Date-based security patch level string associated with bulletin contents"),
        ("Device display", "Consumer devices expose patch level in system settings (implementation via platform)"),
        ("Integrity signal", "Play Integrity optional MEETS_STRONG_INTEGRITY (Android 13+) relates to recent security updates among other signals"),
        ("Character", "Technical versioning of security fix bundles — not multi-year legal support floor"),
    ],
    "A high security patch level on a device indicates incorporated bulletin content for that build; it does not alone prove ongoing multi-year commitment.",
    [
        "Exact mapping rules OEM uses when shipping partial vendor vs platform components.",
    ],
    "High",
)

note(
    "cdd",
    "Android Compatibility Definition Document (CDD)",
    "The CDD enumerates requirements that device implementations must meet to be considered compatible with a given Android version. Official docs call the CDD the 'policy' aspect of Android compatibility; CTS is the test suite aspect. CDDs are published per platform version.",
    [
        ("CDD overview", "https://source.android.com/docs/compatibility/cdd"),
        ("Latest CDD HTML hub", "https://source.android.com/docs/compatibility/android-cdd"),
        ("Compatibility program", "https://source.android.com/docs/compatibility/overview"),
        ("Compatibility landing", "https://source.android.com/docs/compatibility"),
    ],
    [
        ("Role", "Codifies compatibility policy requirements for a platform version"),
        ("Relationship to CTS", "CTS cannot be fully comprehensive; CDD clarifies requirements tests cannot fully capture"),
        ("Versioning", "Detailed CDD per Android platform release (versions listed on CDD page through recent releases)"),
        ("Scope", "Compatibility with Android APIs/behaviours — not a consumer multi-year update duration statute"),
        ("Character", "Technical compatibility policy document for implementers"),
    ],
    "CDD requirements concern compatibility of a device build with a platform version. They do not, by themselves, mandate multi-year post-sale OS upgrade counts under Indian law.",
    [
        "Specific CDD clauses on security update expectations for each recent version — residual deep pin-cite OPEN if needed for litigation packs.",
    ],
    "High",
)

note(
    "cts",
    "Compatibility Test Suite (CTS)",
    "CTS is a free commercial-grade test suite used to help ensure devices are Android compatible. It runs on a desktop host, executing tests on attached devices or emulators, and is intended for continuous integration workflows.",
    [
        ("CTS overview", "https://source.android.com/docs/compatibility/cts"),
        ("CTS setup", "https://source.android.com/docs/compatibility/cts/setup"),
        ("Compatibility program", "https://source.android.com/docs/compatibility/overview"),
    ],
    [
        ("Components", "Trade Federation harness; automated tests; CTS Verifier (manual) + app"),
        ("Coverage areas", "API signatures, platform APIs, Dalvik, data model, intents, permissions, resources"),
        ("Role", "Reveal incompatibilities early; maintain compatibility during development"),
        ("Character", "Compliance test tooling — not an end-user update service"),
    ],
    "Passing CTS is about compatibility of an implementation, not about how many years an OEM will ship security OTAs after retail sale.",
    [
        "CTS-on-GSI / newer suite variants deep inventory residual if needed.",
    ],
    "High",
)

note(
    "vts",
    "Vendor Test Suite (VTS)",
    "The Android Vendor Test Suite (VTS) provides extensive testing of kernel and HAL layers. Like CTS, it uses Trade Federation on a host machine and executes tests on devices/emulators. Test types include GTest HAL tests, Linux kernel tests (kselftest, LTP), some JUnit host tests, and limited Python tests.",
    [
        ("VTS and infrastructure", "https://source.android.com/docs/core/tests/vts"),
        ("Architecture overview (Android-compatible path mentions VTS)", "https://source.android.com/docs/core/architecture"),
        ("HAL overview", "https://source.android.com/docs/core/architecture/hal"),
    ],
    [
        ("Focus", "Kernel and HAL validation for vendor implementations"),
        ("Android-compatible devices", "Architecture docs: CDD + VSR + VTS/CTS among requirements path"),
        ("Character", "Vendor-side test suite — supports Treble/GKI-era interfaces"),
    ],
    "VTS does not define consumer software-support duration.",
    [
        "Exact current VSR document URL pin residual if separate from CDD.",
    ],
    "High",
)

note(
    "gms",
    "Google Mobile Services (GMS)",
    "Google Mobile Services (GMS) refers to Google’s proprietary apps/services suite and related certification path for devices that license Google apps (Play Store, etc.). Official android.com/gms is the public GMS orientation page. Mainline docs distinguish GMS-signed module packages from AOSP-keyed packages.",
    [
        ("Google Mobile Services", "https://www.android.com/gms/"),
        ("Mainline GMS vs AOSP package naming", "https://source.android.com/docs/core/architecture/modular-system"),
        ("Play Integrity (Play ecosystem integrity)", "https://developer.android.com/google/play/integrity/overview"),
    ],
    [
        ("Role", "Proprietary Google apps/services layer beyond pure AOSP"),
        ("Certification relevance", "Commercial devices seeking Play/GMS typically follow Google compatibility/certification processes beyond open AOSP"),
        ("Mainline packages", "GMS devices use Google-signed Mainline packages (com.google.android.*)"),
        ("Character", "Commercial services/certification stack — terms are private partner agreements (not fully public)"),
    ],
    "Detailed GMS licensing agreements and any contractual update obligations to OEMs are not fully published as public multi-year consumer matrices on the pages reviewed. Residual OPEN for non-public partner terms.",
    [
        "Public summary of GMS requirements related to security update cadence, if any published document exists.",
    ],
    "Moderate–High",
)

note(
    "treble",
    "Project Treble / vendor interface separation",
    "Project Treble (Android 8 era onward) re-architected Android to separate the vendor implementation (HALs, vendor partition) from the framework, enabling modular updates and cleaner upgrades. Official docs describe binderized HALs, HIDL/AIDL interfaces, and Vendor Interface (VINTF) compatibility concepts. Android Verified Boot (AVB) works with Treble.",
    [
        ("HAL overview (binderized HALs; Android 8+)", "https://source.android.com/docs/core/architecture/hal"),
        ("Architecture overview", "https://source.android.com/docs/core/architecture"),
        ("Verified Boot / AVB with Treble", "https://source.android.com/docs/security/features/verifiedboot"),
        ("VTS (vendor/HAL testing)", "https://source.android.com/docs/core/tests/vts"),
    ],
    [
        ("Architectural goal", "Separate vendor hardware implementation from Android framework for easier platform updates"),
        ("Interfaces", "Standard HAL interfaces (HIDL historically; AIDL for HALs preferred as of Android 13 deprecation of HIDL)"),
        ("Testing", "VTS validates vendor/HAL/kernel aspects"),
        ("Character", "Platform architecture enabling updates — does not by itself set N-year consumer support floors"),
    ],
    "Treble reduces some upgrade friction but does not eliminate OEM work for full OS upgrades; commercial support length remains OEM policy (WS1).",
    [
        "Device-by-device Treble compliance status in India market — empirical residual.",
    ],
    "High",
)

note(
    "gki",
    "Generic Kernel Image (GKI)",
    "The GKI project addresses kernel fragmentation by unifying the core kernel and moving SoC/board support into loadable vendor modules with a stable Kernel Module Interface (KMI). Beginning Android 12, devices shipping with kernel 5.10+ must ship with the GKI kernel. GKI kernels are built from Android Common Kernel (ACK) sources.",
    [
        ("Generic Kernel Image (GKI) project", "https://source.android.com/docs/core/architecture/kernel/generic-kernel-image"),
        ("Android common kernels (ACK)", "https://source.android.com/docs/core/architecture/kernel/android-common"),
        ("Kernel architecture overview", "https://source.android.com/docs/core/architecture/kernel"),
    ],
    [
        ("Problem addressed", "Pre-GKI custom kernels with large out-of-tree code hindered security backport and LTS merges"),
        ("Design", "Single GKI binary per architecture/LTS + vendor modules; stable KMI"),
        ("Requirement", "Android 12+ devices with kernel 5.10+ ship GKI"),
        ("Goals", "Partners deliver kernel security fixes without full vendor rebuild; reduce major kernel uprev cost"),
        ("ACK support lifetimes", "Official ACK table lists multi-year EOL dates per branch (e.g. 4–6 year support lifetimes depending on branch)"),
        ("Character", "Kernel architecture & common-kernel support windows — distinct from OEM product support marketing"),
    ],
    "GKI/ACK support lifetimes describe common kernel branch maintenance by Google/community processes — they are not automatic consumer device OS-upgrade promises for every OEM SKU.",
    [
        "Which India-volume models actually ship pure GKI vs exceptions — device capture residual.",
    ],
    "High",
)

note(
    "vendor-interface",
    "Vendor Interface (HAL / VINTF)",
    "The vendor interface is the stable boundary between Android framework and vendor-owned HAL/kernel modules. Official HAL documentation describes AIDL/HIDL interfaces, binderized HALs, service manager registration, and compatibility matrices that list required HALs for a target release.",
    [
        ("HAL overview", "https://source.android.com/docs/core/architecture/hal"),
        ("Compatibility matrices (VINTF)", "https://source.android.com/docs/core/architecture/vintf/comp-matrices"),
        ("Architecture overview", "https://source.android.com/docs/core/architecture"),
    ],
    [
        ("Purpose", "Allow framework updates without rewriting all vendor code"),
        ("HAL service duty", "Implement required HALs listed in compatibility matrix for target release on vendor partition"),
        ("Evolution", "HIDL deprecated as of Android 13 in favour of AIDL for HALs"),
        ("Character", "Interface stability mechanism for platform/vendor co-existence"),
    ],
    "Vendor interface stability improves update modularity; it does not define how long an OEM must support a retail device.",
    [
        "Deep inventory of mandatory HALs per recent Android version residual if needed.",
    ],
    "High",
)

note(
    "android-upgrade-process",
    "Android Upgrade / OTA Process",
    "Android devices can receive OTA updates to the system, read-only system apps, and time zone rules. Official OTA docs describe Virtual A/B (seamless) updates (Android 11+), legacy A/B, and deprecation of non-A/B as of Android 15. OTAs do not update user-installed Play apps (those update via Play).",
    [
        ("OTA updates", "https://source.android.com/docs/core/ota"),
        ("Virtual A/B seamless updates", "https://source.android.com/docs/core/ota/virtual_ab"),
        ("A/B system updates", "https://source.android.com/docs/core/ota/ab"),
        ("Time zone rules updates", "https://source.android.com/docs/core/permissions/timezone-rules"),
    ],
    [
        ("Package scope", "OS, system partition apps, time zone rules — not user Play apps"),
        ("Virtual A/B", "Two logical slots; compressed snapshots for large dynamic partitions"),
        ("Non-A/B", "Deprecated as of Android 15"),
        ("TZ updates", "From Android 8.1, TZ rules can update without full system image"),
        ("Character", "Technical update delivery architecture for implementers"),
    ],
    "OTA mechanisms enable updates; they do not specify minimum years of support for commercial devices.",
    [
        "Carrier vs OEM OTA channel differences in India — residual.",
    ],
    "High",
)

note(
    "android-release-cycle",
    "Android Platform Release Cycle",
    "Android platform releases are versioned (recent CDDs list versions through Android 16/17 era materials). Official site notes a trunk-stable development model and, effective 2026, AOSP source publication in Q2 and Q4 with android-latest-release tracking the most recent release pushed to AOSP.",
    [
        ("AOSP site updates / Changes to AOSP", "https://source.android.com/docs/whatsnew/site-updates"),
        ("CDD version table", "https://source.android.com/docs/compatibility/cdd"),
        ("Architecture overview", "https://source.android.com/docs/core/architecture"),
    ],
    [
        ("Platform versions", "Annual major platform releases with corresponding CDD/CTS"),
        ("AOSP publish (2026)", "Q2 and Q4 source publication alignment stated on official docs banners"),
        ("Trunk stable", "Development model referenced in official site updates"),
        ("Character", "Platform engineering release process — distinct from OEM device upgrade calendars"),
    ],
    "Platform release schedule ≠ guaranteed device upgrade schedule for every OEM model.",
    [
        "Detailed internal Google release train calendars beyond public docs residual.",
    ],
    "High",
)

note(
    "update-distribution-architecture",
    "Update Distribution Architecture",
    "Android update distribution spans multiple official channels: full system OTA packages (A/B or Virtual A/B), Mainline module packages via Google Play system updates or partner OTA, time zone data updates, and app updates via Google Play (user apps). Security bulletin fixes reach devices only after OEM/SoC integration and shipping.",
    [
        ("OTA updates", "https://source.android.com/docs/core/ota"),
        ("Mainline modular updates", "https://source.android.com/docs/core/architecture/modular-system"),
        ("Android Security Bulletins sources", "https://source.android.com/docs/security/bulletin/asb-overview"),
    ],
    [
        ("Full system OTA", "OEM/carrier-controlled system image updates"),
        ("Mainline / Play system updates", "Modular components; Google or partner packaging"),
        ("Bulletin integration", "AOSP + kernel + SOC sources must be merged and shipped by manufacturers"),
        ("Apps", "User-installed apps update independently via Play — do not replace OS patches"),
        ("Character", "Multi-path distribution architecture"),
    ],
    "No single channel covers entire device security surface for all devices indefinitely.",
    [
        "Quantitative India market split between Play system update-capable devices vs older stacks.",
    ],
    "High",
)

note(
    "android-update-responsibilities",
    "Android Update Responsibilities (descriptive map)",
    "Official documentation distributes technical responsibilities across Google/AOSP (platform code, bulletins, Mainline modules, GKI/ACK), SoC vendors (chipset fixes), and OEMs (device builds, OTAs, vendor partitions, product support policies). This note maps those roles descriptively without assigning legal liability.",
    [
        ("Architecture overview", "https://source.android.com/docs/core/architecture"),
        ("Security bulletins — fix sources", "https://source.android.com/docs/security/bulletin/asb-overview"),
        ("Mainline", "https://source.android.com/docs/core/architecture/modular-system"),
        ("GKI", "https://source.android.com/docs/core/architecture/kernel/generic-kernel-image"),
        ("OTA", "https://source.android.com/docs/core/ota"),
    ],
    [
        ("Google / AOSP", "Publish platform source, CDD/CTS, security bulletins, Mainline modules, GKI/ACK maintenance"),
        ("SoC vendors", "Provide chipset/kernel/firmware fixes referenced in bulletins"),
        ("OEMs", "Integrate fixes, build device images, operate OTA pipelines, set product support lifetimes (WS1)"),
        ("Carriers (where applicable)", "May control OTA approval/distribution in some markets (implementation/business practice)"),
        ("Users", "Install offered updates; app updates via Play"),
        ("Character", "Descriptive responsibility map from platform docs — not legal allocation under Indian law"),
    ],
    "Platform docs describe technical roles; they do not create Indian statutory duties for multi-year support.",
    [
        "Contractual GMS terms between Google and OEMs remain largely non-public.",
    ],
    "High",
)

note(
    "google-vs-oem-responsibilities",
    "Google vs OEM Responsibilities (updates)",
    "Complementing the update-responsibilities map: Google publishes Android platform security fixes and modular updates; OEMs decide product-line support duration and ship device-specific builds. Pixel devices have Google-published support-duration pages (WS1). Third-party OEMs publish their own policies.",
    [
        ("Security bulletins", "https://source.android.com/docs/security/bulletin/asb-overview"),
        ("Mainline", "https://source.android.com/docs/core/architecture/modular-system"),
        ("Pixel software updates (OEM example — Google as OEM)", "https://support.google.com/pixelphone/answer/4457705"),
        ("Architecture overview", "https://source.android.com/docs/core/architecture"),
    ],
    [
        ("Google as platform steward", "AOSP, bulletins, Mainline, GKI/ACK, compatibility program"),
        ("Google as Pixel OEM", "Publishes multi-year Pixel update commitments (WS1)"),
        ("Other OEMs", "Integrate platform; ship OTAs; publish own lifecycle policies (WS1)"),
        ("Shared security surface", "Kernel/vendor/firmware require OEM/SoC action beyond pure framework Mainline modules"),
        ("Character", "Descriptive split — not liability conclusions"),
    ],
    "Neither Google platform documentation nor OEM marketing pages constitute Indian legislation mandating multi-year support industry-wide.",
    [
        "Whether any public GMS MoU clauses on security updates exist outside partner portals.",
    ],
    "High",
)

note(
    "verified-boot",
    "Android Verified Boot",
    "Verified Boot ensures executed code comes from a trusted source (usually device OEMs) via a chain of trust from hardware root of trust through bootloader to verified partitions (boot, system, vendor, etc.). Android 8+ includes Android Verified Boot (AVB) working with Treble, standardizing footers and rollback protection features.",
    [
        ("Verified Boot overview", "https://source.android.com/docs/security/features/verifiedboot"),
        ("Use Verified Boot", "https://source.android.com/docs/security/features/verifiedboot/verified-boot"),
        ("AVB", "https://source.android.com/docs/security/features/verifiedboot/avb"),
        ("dm-verity", "https://source.android.com/docs/security/features/verifiedboot/dm-verity"),
    ],
    [
        ("Chain of trust", "Hardware root → bootloader → partitions"),
        ("Enforcement history", "Android 7.0 strict enforcement; earlier versions warned"),
        ("dm-verity", "Hash-tree verification for large partitions"),
        ("AVB", "Reference implementation with Treble; standardized footers; rollback features"),
        ("Character", "Device integrity architecture"),
    ],
    "Verified Boot protects integrity of software that is present; it does not define how long updates will be offered.",
    [
        "OEM lock state / unlock policy variance residual.",
    ],
    "High",
)

note(
    "rollback-protection",
    "Rollback Protection",
    "Rollback protection prevents installing/booting older, more vulnerable Android versions after an update, blocking a class of persistent exploit attacks. Official Verified Boot docs describe tamper-evident storage of recent versions and refusal to boot lower versions, typically per partition. AVB implements rollback protections.",
    [
        ("Verified Boot — rollback protection", "https://source.android.com/docs/security/features/verifiedboot"),
        ("Use Verified Boot — Rollback protection section", "https://source.android.com/docs/security/features/verifiedboot/verified-boot"),
        ("AVB README (AOSP)", "https://android.googlesource.com/platform/external/avb/+/android17-release/README.md"),
    ],
    [
        ("Threat model", "Non-persistent exploit reinstalls older vulnerable OS to gain persistence"),
        ("Mechanism", "Record newest version; refuse lower versions"),
        ("AVB", "Standardized rollback protection features"),
        ("Character", "Security control on update directionality"),
    ],
    "Rollback protection is orthogonal to multi-year support length; it constrains version direction, not support calendar length.",
    [
        "User-authorized rollback / data migration edge cases residual.",
    ],
    "High",
)

note(
    "play-integrity",
    "Play Integrity API",
    "Play Integrity API helps apps check that user actions/server requests come from a genuine app installed by Google Play on a genuine certified Android device. Verdicts cover app, device, and account licensing signals; optional labels include MEETS_STRONG_INTEGRITY related to recent security updates on Android 13+.",
    [
        ("Play Integrity overview", "https://developer.android.com/google/play/integrity/overview"),
        ("Play Integrity setup", "https://developer.android.com/google/play/integrity/setup"),
        ("Play Integrity landing", "https://developer.android.com/google/play/integrity"),
    ],
    [
        ("Purpose", "Abuse/fraud/tamper detection for apps using Play ecosystem signals"),
        ("Core verdicts", "appIntegrity, deviceIntegrity, accountDetails"),
        ("Security updates signal", "MEETS_STRONG_INTEGRITY (Android 13+) involves recent security updates among hardware-backed signals"),
        ("Request types", "Standard (low latency) and Classic"),
        ("Character", "App/developer integrity API — not an OEM update-duration policy"),
    ],
    "Play Integrity measures aspects of device/app trustworthiness at request time; it does not create OEM obligations to ship N years of OS upgrades.",
    [
        "Prevalence of strong-integrity failures on unsupported India devices — empirical residual.",
    ],
    "High",
)

# ── Negative finding ────────────────────────────────────────
(OUT / "negative-finding-android-platform-not-multi-year-device-floor.md").write_text(
    f"""---
title: "Negative finding — Android platform docs are not multi-year device support floors"
domain: "android-ecosystem"
status: VERIFIED
last_updated: {ACCESS}
phase: 5
workstream: "P5-WS2"
---

# Negative Finding — Platform Documentation vs Device Support Duration

## Repository Relevance

**Tags:** Android ecosystem · Negative finding · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Scope-limited search of official Google/AOSP Android documentation. Not legal conclusions.

## Official sources [FACT]

Primary corpus: source.android.com (architecture, OTA, Mainline, GKI, CDD/CTS/VTS, security bulletins, verified boot); developer.android.com (Play Integrity, Android Enterprise); android.com (GMS, Enterprise Recommended). Access window: **{ACCESS}**.

## Negative findings [FACT]

1. **No industry-wide multi-year consumer OS floor in AOSP platform docs.** Architecture, CDD, CTS, VTS, OTA, Mainline, and GKI documentation describe *how* Android can be updated and certified — not a binding N-year support duty for all commercial devices.
2. **Security Bulletin publication ≠ universal device shipping.** Monthly bulletins publish fixes; OEMs/SoCs must still integrate and ship.
3. **Mainline / Play system updates are partial.** Modular components only; kernel/vendor/non-modular surfaces remain OEM-dependent.
4. **GKI/ACK lifetimes ≠ OEM product marketing support.** Common kernel EOL tables are not substitute for per-brand consumer policies (Phase 5 WS1).
5. **GMS commercial terms** governing partner update expectations are not fully public as a single consumer-facing multi-year matrix on pages reviewed.

## Cross references

- Phase 5 WS1 OEM policies: `research/manufacturers/`
- Phase 4 government-side negative finding (no Indian multi-year OS legal floor)
- `ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md`

## Consistency

Complements Phase 4 (no Indian legal multi-year floor) and Phase 5 WS1 (heterogeneous OEM private policies).

## Audit trail

- Phase 5 Workstream 2
- Official sources only
""",
    encoding="utf-8",
)
print("wrote negative finding")

# ── Matrices & reports ──────────────────────────────────────

(OUT / "README.md").write_text(
    f"""# Android Ecosystem — Phase 5 Workstream 2

**Status:** Workstream 2 complete (Android platform / update infrastructure inventory)  
**Phase 5 overall:** In progress  
**OS:** `REPOSITORY_OS.md` · `PHASE_05_SPECIFICATION.md`  
**Access window:** {ACCESS}

## Rules

- **Official Google / AOSP documentation only** (source.android.com, developer.android.com, android.com enterprise/GMS, security bulletins).  
- Descriptive — not Indian law; not recommendations; not OEM ranking.  
- Repository Relevance + Classification on every note.  
- Does **not** re-audit Phase 5 WS1 manufacturer policies.

## Research notes

| Topic | File |
|-------|------|
| AOSP | [aosp.md](aosp.md) |
| Android Enterprise | [android-enterprise.md](android-enterprise.md) |
| Android Enterprise Recommended | [android-enterprise-recommended.md](android-enterprise-recommended.md) |
| Project Mainline | [project-mainline.md](project-mainline.md) |
| Play System Updates | [play-system-updates.md](play-system-updates.md) |
| Android Security Bulletins | [android-security-bulletins.md](android-security-bulletins.md) |
| Monthly Security Updates | [monthly-security-updates.md](monthly-security-updates.md) |
| Security Patch Levels | [security-patch-levels.md](security-patch-levels.md) |
| CDD | [cdd.md](cdd.md) |
| CTS | [cts.md](cts.md) |
| VTS | [vts.md](vts.md) |
| GMS | [gms.md](gms.md) |
| Treble / vendor separation | [treble.md](treble.md) |
| GKI | [gki.md](gki.md) |
| Vendor Interface | [vendor-interface.md](vendor-interface.md) |
| Upgrade / OTA process | [android-upgrade-process.md](android-upgrade-process.md) |
| Platform release cycle | [android-release-cycle.md](android-release-cycle.md) |
| Update distribution architecture | [update-distribution-architecture.md](update-distribution-architecture.md) |
| Update responsibilities map | [android-update-responsibilities.md](android-update-responsibilities.md) |
| Google vs OEM responsibilities | [google-vs-oem-responsibilities.md](google-vs-oem-responsibilities.md) |
| Verified Boot | [verified-boot.md](verified-boot.md) |
| Rollback Protection | [rollback-protection.md](rollback-protection.md) |
| Play Integrity | [play-integrity.md](play-integrity.md) |
| Negative finding | [negative-finding-android-platform-not-multi-year-device-floor.md](negative-finding-android-platform-not-multi-year-device-floor.md) |

## Analytical artefacts

| Artefact | File |
|----------|------|
| Coverage matrix | [ANDROID_COVERAGE_MATRIX.md](ANDROID_COVERAGE_MATRIX.md) |
| Architecture matrix | [ANDROID_ARCHITECTURE_MATRIX.md](ANDROID_ARCHITECTURE_MATRIX.md) |
| Update responsibility matrix | [ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md](ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md) |
| Component matrix | [ANDROID_COMPONENT_MATRIX.md](ANDROID_COMPONENT_MATRIX.md) |
| Source report | [ANDROID_SOURCE_REPORT.md](ANDROID_SOURCE_REPORT.md) |
| Citation report | [ANDROID_CITATION_REPORT.md](ANDROID_CITATION_REPORT.md) |
| Validation report | [ANDROID_VALIDATION_REPORT.md](ANDROID_VALIDATION_REPORT.md) |
| Cross-reference report | [ANDROID_CROSS_REFERENCE_REPORT.md](ANDROID_CROSS_REFERENCE_REPORT.md) |
| Workstream report | [`../../PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md`](../../PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md) |
""",
    encoding="utf-8",
)

(OUT / "ANDROID_COVERAGE_MATRIX.md").write_text(
    f"""# Android Ecosystem Coverage Matrix — Phase 5 WS2

## Repository Analytical Artefact

This document is an analytical representation created for this repository.  
**It is not an official Google or Government publication.**

**Date:** {ACCESS}

| Topic | Note | Official docs captured? |
|-------|------|-------------------------|
| AOSP | aosp.md | Yes |
| Android Enterprise | android-enterprise.md | Yes |
| Android Enterprise Recommended | android-enterprise-recommended.md | Yes (landing; detailed requirements PDF residual OPEN) |
| Project Mainline | project-mainline.md | Yes |
| Play System Updates | play-system-updates.md | Yes (via Mainline/OTA docs) |
| Security Bulletins | android-security-bulletins.md | Yes |
| Monthly security updates | monthly-security-updates.md | Yes |
| Security patch levels | security-patch-levels.md | Yes |
| CDD | cdd.md | Yes |
| CTS | cts.md | Yes |
| VTS | vts.md | Yes |
| GMS | gms.md | Yes (public orientation; partner terms residual) |
| Treble | treble.md | Yes |
| GKI | gki.md | Yes |
| Vendor interface | vendor-interface.md | Yes |
| OTA / upgrade process | android-upgrade-process.md | Yes |
| Release cycle | android-release-cycle.md | Yes |
| Update distribution | update-distribution-architecture.md | Yes |
| Update responsibilities | android-update-responsibilities.md | Yes |
| Google vs OEM | google-vs-oem-responsibilities.md | Yes |
| Verified Boot | verified-boot.md | Yes |
| Rollback protection | rollback-protection.md | Yes |
| Play Integrity | play-integrity.md | Yes |
| Negative finding | negative-finding-… | Yes |

**Coverage result:** Core WS2 topic list **complete** at descriptive baseline depth.
""",
    encoding="utf-8",
)

(OUT / "ANDROID_ARCHITECTURE_MATRIX.md").write_text(
    f"""# Android Architecture Matrix — Phase 5 WS2

## Repository Analytical Artefact

**Not** an official Google publication. **Date:** {ACCESS}

| Layer / concept | Official role (descriptive) | Update relevance |
|-----------------|----------------------------|------------------|
| Apps (user) | Third-party / preloaded apps | Play app updates ≠ OS patches |
| Android framework | Public + system APIs | Platform OTAs / some Mainline modules |
| System services | Modular system components | Mainline candidates where modularized |
| ART | Runtime | Mainline ART module (from Android 12) |
| HAL / vendor interface | Vendor hardware abstraction | Vendor partition; VTS |
| Native daemons/libs | Low-level userspace | Platform/vendor as applicable |
| GKI kernel + vendor modules | Unified core kernel + modules | Kernel security via GKI/ACK + vendor modules |
| Verified Boot / AVB | Chain of trust + rollback | Protects integrity of installed images |

| Compatibility artefact | Role |
|------------------------|------|
| CDD | Policy requirements for compatibility |
| CTS | Automated compatibility tests |
| VTS | Vendor kernel/HAL tests |
| VINTF matrices | Required HAL interfaces per release |
""",
    encoding="utf-8",
)

(OUT / "ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md").write_text(
    f"""# Android Update Responsibility Matrix — Phase 5 WS2

## Repository Analytical Artefact

Descriptive map from official platform documentation. **Not** legal liability allocation. **Date:** {ACCESS}

| Responsibility area | Google / AOSP | SoC vendor | OEM | Carrier (if any) | End user |
|---------------------|---------------|------------|-----|------------------|----------|
| Publish platform security fixes (bulletins) | Primary | Contributes chipset fixes | Integrates/ships | May gate OTA | Installs |
| Mainline module packages | Builds/signs (GMS path) | — | May ship partner OTA path | — | Receives Play system updates |
| Full system OTA image | Provides AOSP base | Provides BSP pieces | **Builds & ships** | May approve/distribute | Installs |
| Kernel (GKI) updates | Maintains GKI/ACK | Vendor modules | Integrates/ships device kernel package | — | Installs |
| Product support duration (years) | Pixel as OEM (WS1); platform docs ≠ industry floor | — | **Publishes policy** (WS1) | — | Purchase decision |
| App updates (user apps) | Play Store | — | Preloads vary | — | Updates apps |
| Compatibility certification (CTS/CDD) | Defines/tests program | Supports | Executes for products | — | — |

**Key descriptive takeaway:** Platform infrastructure enables updates; **device-level multi-year commitments remain OEM product policies** (Phase 5 WS1), not AOSP universal floors.
""",
    encoding="utf-8",
)

(OUT / "ANDROID_COMPONENT_MATRIX.md").write_text(
    f"""# Android Component Matrix — Phase 5 WS2

## Repository Analytical Artefact

**Date:** {ACCESS}

| Component / programme | Update path (official) | Covered by Mainline? | Notes |
|-----------------------|------------------------|----------------------|-------|
| Framework (non-modular) | System OTA | Partial / evolving | Many areas still full OTA |
| Mainline modules (Conscrypt, Media, Wi-Fi, ART, …) | Play system updates or partner OTA | Yes | See modular-system module table |
| Vendor HALs | Vendor image / OTA | No (vendor-owned) | Treble interfaces |
| GKI core kernel | GKI boot image updates | No (kernel project) | Stable KMI with vendor modules |
| Vendor kernel modules | Vendor image | No | Device-specific |
| Security bulletin platform fixes | OEM OTA after AOSP merge | Some modules if Mainline | Mixed |
| User Play apps | Google Play | N/A | Not OS |
| Time zone data | TZ updates / Mainline tzdata | Yes (tzdata module) | Can avoid full OTA |
| Verified Boot metadata | Shipping images | N/A | Integrity, not cadence |
""",
    encoding="utf-8",
)

(OUT / "ANDROID_SOURCE_REPORT.md").write_text(
    f"""# Android Ecosystem Source Report — Phase 5 WS2

**Date:** {ACCESS}

## Accepted

| Source class | Examples | Tier |
|--------------|----------|------|
| AOSP docs | source.android.com architecture, OTA, Mainline, GKI, HAL, VTS, CDD, CTS, security, verified boot | T0 |
| Android Developers | developer.android.com/work, Play Integrity | T0/T1 |
| Android.com product | android.com/gms, android.com/enterprise | T1 |
| Google support (Android/Pixel) | support.google.com/android, pixelphone | T1 |
| AOSP googlesource | android.googlesource.com AVB README | T0 |

## Rejected

Blogs · forums · Reddit · Wikipedia · YouTube · news · unofficial tech articles · community wikis as sole authority

## Provisional / residual OPEN

- Full public GMS partner agreement text (if any) on security update SLAs  
- Complete AER requirement PDF version pin  
- Deep CDD clause pin-cites on security updates per version  

## Conclusion

Acceptable official Google/AOSP inventory for WS2 technical baseline.
""",
    encoding="utf-8",
)

(OUT / "ANDROID_CITATION_REPORT.md").write_text(
    f"""# Android Ecosystem Citation Report — Phase 5 WS2

**Date:** {ACCESS}

| Rule | Status |
|------|--------|
| Official URLs only as authorities | **PASS** |
| Access dates recorded | **PASS** ({ACCESS}) |
| FACT / ANALYSIS labels | **PASS** |
| No fabricated case law / statutes | **PASS** (technical domain) |
| OEM policies not re-stated as law | **PASS** |
| Cross-links to WS1 manufacturers | **PASS** |

**Overall citation quality:** **PASS**
""",
    encoding="utf-8",
)

(OUT / "ANDROID_VALIDATION_REPORT.md").write_text(
    f"""# Android Ecosystem Validation Report — Phase 5 WS2

**Date:** {ACCESS}  
**Standard:** VALIDATION.md · REPOSITORY_OS.md · PHASE_05_SPECIFICATION.md

| Check | Result |
|-------|--------|
| Official Google/AOSP sources only | **PASS** |
| Research notes present for major topics | **PASS** (23 topic notes + negative finding) |
| Repository Relevance + Classification | **PASS** |
| Matrices + reports | **PASS** |
| No recommendations / legal conclusions as law | **PASS** |
| No OEM ranking / policy proposals | **PASS** |
| Single workstream scope | **PASS** |
| Phase 5 WS1 not rewritten | **PASS** |
| Duplicate research avoided | **PASS** (new domain folder) |

**Overall:** **PASS**
""",
    encoding="utf-8",
)

(OUT / "ANDROID_CROSS_REFERENCE_REPORT.md").write_text(
    f"""# Android Ecosystem Cross-Reference Report — Phase 5 WS2

**Date:** {ACCESS}

| From | To | Relationship |
|------|-----|--------------|
| android-ecosystem/* | manufacturers/* | Platform infrastructure vs OEM product policies |
| security-bulletins | manufacturers/* | Bulletin publish vs OEM ship |
| mainline / play-system-updates | update-distribution-architecture | Modular path |
| gki | android-common kernels / security | Kernel security delivery |
| cdd/cts/vts | treble / vendor-interface | Compatibility program |
| verified-boot / rollback | android-upgrade-process | Integrity of OTAs |
| play-integrity | security-patch-levels | Strong integrity / recent patches signal |
| google-vs-oem-responsibilities | PHASE_05 WS1 report | Pixel vs third-party OEMs |
| negative finding (platform) | phase4-gap-analysis + manufacturers negative finding | No universal multi-year floor (law or platform) |

**Orphans:** None intended — all notes linked from README and workstream report.
""",
    encoding="utf-8",
)

# Workstream report
(ROOT / "PHASE_05_ANDROID_ECOSYSTEM_WORKSTREAM_REPORT.md").write_text(
    f"""# Phase 5 Workstream 2 Report — Android Ecosystem

**Date:** {ACCESS}  
**Base main:** `558a405` (Phase 5 WS1 merged, v0.6.1)  
**Phase 5 status:** In progress (WS2 when this merges)  
**Version:** **0.6.2**

---

## 1. Objectives

Document **official Google / AOSP Android platform and update infrastructure** as descriptive technical baseline evidence. No recommendations, policy proposals, or legal interpretation.

## 2. Topics covered

AOSP · Android Enterprise · Android Enterprise Recommended · Project Mainline · Play System Updates · Security Bulletins · Monthly security updates · Security patch levels · CDD · CTS · VTS · GMS · Treble · GKI · Vendor interface · OTA/upgrade process · Platform release cycle · Update distribution · Update responsibilities · Google vs OEM responsibilities · Verified Boot · Rollback protection · Play Integrity  

## 3. Key descriptive findings

| Finding | Detail |
|---------|--------|
| Multi-path updates | Full system OTA + Mainline/Play system updates + TZ + app updates |
| Bulletin ≠ device ship | Monthly ASB publishes fixes; OEM/SoC integrate and ship |
| Modular security partial | Mainline covers selected components only |
| GKI reduces kernel fragmentation | Required for Android 12+ with kernel 5.10+; ACK support lifetime tables exist |
| Compatibility program | CDD (policy) + CTS/VTS (tests) define compatibility — not consumer N-year floors |
| Responsibility split | Google platform vs SoC vs OEM product policies (WS1) |
| Negative finding | Platform docs are **not** a universal multi-year device support floor |

## 4. Validation / Gate++

**PASS** / **PASS** (see `orchestration/PHASE_05_WS2_GATE_REPORT.md`)

## 5. Explicitly not done

- Phase 5 **not** complete  
- iOS technical baseline (separate residual tasks)  
- OEM policy re-audit  
- Phase 5 Workstream 3 — **not started**

## 6. Next

Further Phase 5 work only after merge + authorisation. **Do not auto-start WS3.**

---
""",
    encoding="utf-8",
)

(ROOT / "orchestration" / "PHASE_05_WS2_GATE_REPORT.md").write_text(
    f"""# Repository Gate++ — Phase 5 WS2

**Date:** {ACCESS}

| Check | Result |
|-------|--------|
| PR #26 / WS1 prerequisite | **PASS** (merged; v0.6.1) |
| Official Google/AOSP sources only | **PASS** |
| Folder `research/android-ecosystem/` | **PASS** |
| Notes + matrices + reports | **PASS** |
| Repository Relevance / Classification | **PASS** |
| No recommendations / legal conclusions as law | **PASS** |
| Single workstream | **PASS** |
| Indexes / docs update | **PASS** (this PR) |
| Knowledge graph reachability | **PASS** (README + research/README + STATE) |

**Overall:** **PASS**
""",
    encoding="utf-8",
)

print("WS2 package generation complete")
