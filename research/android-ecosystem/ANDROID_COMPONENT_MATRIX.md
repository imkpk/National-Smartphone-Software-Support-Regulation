# Android Component Matrix — Phase 5 WS2

## Repository Analytical Artefact

**Date:** 2026-07-31

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
