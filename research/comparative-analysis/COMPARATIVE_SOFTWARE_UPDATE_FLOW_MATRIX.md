# Software Update Flow Matrix — Phase 5 WS4

## Repository Analytical Artefact

**Date:** 2026-07-31

| Path | Content | Evidence | Replaces full OS security? |
|------|---------|----------|----------------------------|
| Full system OTA | OS + system apps + TZ (WS2) | android-upgrade-process, OTA | Primary for non-modular surface |
| Virtual A/B | Seamless slots | WS2 OTA | Mechanism only |
| Mainline / Play system updates | Selected modules | WS2 Mainline | Partial only |
| GKI boot image | Core kernel | WS2/WS3 GKI | Kernel core only |
| Vendor / vendor_boot | Modules, DTB, vendor bits | WS3 vendor-boot | Vendor surface |
| Firmware OTA | Modem, TEE, bootloader, … | WS3 firmware | Firmware surface |
| Play app updates | User apps | WS2 | **No** — not OS patches |

**Source:** WS2 distribution + WS3 firmware architecture.
