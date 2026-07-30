# Kernel Lifecycle Matrix — Phase 5 WS3

## Repository Analytical Artefact

**Date:** 2026-07-31

| Stage | Actor | Artifact | Official reference |
|-------|-------|----------|--------------------|
| Upstream mainline | kernel.org / Linus | Mainline releases | kernel.org |
| LTS selection | kernel.org stable team | Longterm branches | kernel.org releases |
| ACK branch | Android kernel team | androidXX-Y.Z | source.android.com android-common |
| GKI build | Google | Certified boot.img | GKI project |
| Vendor modules | SoC/OEM | .ko modules | GKI / vendor_boot |
| Device ship | OEM | Product kernel package | OEM OTA |
| EOL | Google (ACK table) | Branch EOL date | android-common support table |

| ACK example (from AOSP table) | Support lifetime (years) | EOL (AOSP table) |
|------------------------------|--------------------------|------------------|
| android12-5.10 | 6 | 2027-07-01 |
| android14-6.1 | 6 | 2029-07-01 |
| android15-6.6 | 4 | 2028-07-01 |
| android16-6.12 | 4 | 2029-07-01 |
| android17-6.18 | 4 | 2030-07-01 |

*Values as published on Android common kernels page at access date; re-verify on re-use.*
