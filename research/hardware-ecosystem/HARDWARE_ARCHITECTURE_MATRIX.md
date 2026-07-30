# Hardware Architecture Matrix — Phase 5 WS3

## Repository Analytical Artefact

**Date:** 2026-07-31

| Layer | Components | Primary maintainers (descriptive) | Update path |
|-------|------------|-------------------------------------|-------------|
| Hardware root of trust | Fuses, ROM | SoC / OEM | Rare; factory |
| Bootloader | ABL/LK/etc. | OEM / SoC | OEM OTA / service |
| GKI kernel | Generic core | Google ACK/GKI | GKI boot image when KMI allows |
| Vendor modules | SoC/board drivers | SoC / OEM | vendor_boot / vendor image |
| Vendor HALs | Camera, audio, … | SoC / OEM | Vendor partition OTA |
| Firmware (modem, DSP, …) | Closed blobs | SoC (+ OEM) | OEM OTA / specialized |
| TEE | Trusty / vendor TEE | Google or vendor | Vendor/OEM controlled |
| Framework / system | Android OS | Google AOSP + OEM | System OTA / Mainline |

| Interface | Role |
|-----------|------|
| KMI | GKI ↔ vendor modules |
| HAL / VINTF | Framework ↔ vendor HAL |
| AVB | Signed verified images |
