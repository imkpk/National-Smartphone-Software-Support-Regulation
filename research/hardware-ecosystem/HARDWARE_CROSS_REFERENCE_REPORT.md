# Hardware Ecosystem Cross-Reference Report — Phase 5 WS3

**Date:** 2026-07-31

| From | To | Relationship |
|------|-----|--------------|
| linux-kernel-lts | android-common-kernel | Upstream LTS → ACK |
| android-common-kernel | generic-kernel-image | ACK 5.10+ as GKI |
| generic-kernel-image | kernel-module-interface | Stable KMI |
| vendor-boot | generic-kernel-image | GKI boot packaging |
| board-support-package | HAL / vendor modules | Vendor software |
| firmware-lifecycle | vendor-security-patches | SoC fix pipeline |
| qualcomm/mediatek/tensor/exynos/unisoc | firmware + GKI | SoC roles |
| verified-boot / tee / bootloader | firmware-lifecycle | Trust chain |
| hardware-ecosystem/* | android-ecosystem/* | Platform vs hardware layers |
| hardware-ecosystem/* | manufacturers/* | Hardware capability vs OEM policies |
| negative finding | WS1/WS2 negative findings | No universal multi-year floor |

**Orphans:** None intended.
