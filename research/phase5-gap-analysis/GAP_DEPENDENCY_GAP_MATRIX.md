# Dependency Gap Matrix — Phase 5 WS5

## Repository Relevance

Describes dependency-chain gaps that can interrupt device updates. **Date:** 2026-07-31

## Classification

**ANALYSIS**

## Evidence sources

WS4 COMPARATIVE_PLATFORM_DEPENDENCY_MATRIX · WS2/WS3 architecture notes

## Cross references

`hardware-gaps.md` · `android-platform-gaps.md` · `responsibility-gaps.md`

## Negative findings

Chain fragility is descriptive, not predictive of future OEM behaviour.

| Dependent layer | Depends on | Documented failure / stop mode in evidence | Gap ID |
|-----------------|------------|--------------------------------------------|--------|
| OEM security OTA | ASB + SoC + kernel fixes | Cannot ship unpublished fixes | A-G2 / H-G5 |
| GKI without vendor rebuild | Stable KMI | KMI break → module rebuild | H-G7 |
| Mainline delivery | Device eligibility / GMS path | Modules not delivered | A-G3 |
| Vendor HALs | Treble/VINTF | Upgrade friction if interfaces break | WS2 Treble |
| Product multi-year claim | OEM ability to integrate full chain | Claim ≠ capability if chain breaks | WS4 dependency |
| Consumer long-term security | All of the above | Layered residual risk (descriptive) | U-G1 |
