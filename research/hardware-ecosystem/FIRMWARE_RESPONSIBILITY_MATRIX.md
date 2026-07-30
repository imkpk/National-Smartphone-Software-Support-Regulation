# Firmware Responsibility Matrix — Phase 5 WS3

## Repository Analytical Artefact

Descriptive only — **not** legal liability. **Date:** 2026-07-31

| Component | Typically developed by | Public fix channel | Ships to device via |
|-----------|------------------------|--------------------|---------------------|
| GKI core kernel | Google (ACK) | GKI builds / LTS merges | OEM (boot image) |
| Vendor kernel modules | SoC / OEM | Partner + OEM builds | vendor_boot / vendor |
| Platform framework | Google AOSP | ASB / AOSP | System OTA |
| SoC proprietary firmware | SoC vendor | SoC bulletins/partner | OEM OTA |
| Bootloader | SoC / OEM | OEM/service | OEM OTA / factory |
| TEE | Google Trusty or vendor TEE | Vendor/OEM | OEM OTA |
| Modem/baseband | SoC | SoC + OEM | OEM OTA |
| Product support years | Device OEM | OEM policy pages (WS1) | Marketing / support policy |

**Key descriptive takeaway:** Long-term device security depends on **coordination** across kernel, SoC firmware, and OEM OTA — no single public party publishes a universal multi-year floor for all layers.
