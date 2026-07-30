# Platform Dependency Matrix — Phase 5 WS4

## Repository Analytical Artefact

**Date:** 2026-07-31

| Dependent layer | Depends on | Failure mode if upstream stops | Evidence |
|-----------------|------------|--------------------------------|----------|
| OEM security OTA | ASB + SoC + kernel fixes | Cannot ship unpublished fixes | WS2/WS3 |
| GKI updates without vendor rebuild | Stable KMI | KMI break → module rebuild | WS3 KMI |
| Mainline modules | Device eligibility / GMS path | Modules not delivered | WS2 |
| Vendor HALs | Treble/VINTF interfaces | Upgrade friction | WS2 Treble/HAL |
| Verified Boot trust | OEM signing + hardware root | Tampered images rejected | WS2/WS3 AVB |
| Product multi-year claim | OEM decision + ability to integrate | Claim ≠ capability if chain breaks | WS1 + WS2/WS3 |
| Consumer device security over time | All of the above | Layered residual risk | Synthesis |

**Descriptive takeaway:** Long-term device updates are a **dependency chain**, not a single actor’s document.
