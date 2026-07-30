---
title: "Negative finding — No universal multi-year chipset/firmware support floor in public official docs"
domain: "hardware-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS3"
---

# Negative Finding — Hardware/Chipset Public Support Floors

## Repository Relevance

**Tags:** Hardware ecosystem · Negative finding · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Scope-limited search of official AOSP, kernel.org, and public chipset vendor documentation.

## Official sources [FACT]

source.android.com (kernel, GKI, HAL, Verified Boot, Trusty, ASB, OTA, vendor_boot) · kernel.org releases · docs.qualcomm.com security bulletins · Samsung security/TEEGRIS · unisoc.com · Google Pixel support/bulletins. Access: **2026-07-31**.

## Negative findings [FACT]

1. **No universal multi-year consumer chipset/firmware support floor** published jointly by SoC vendors for all Android devices.
2. **ACK/GKI/LTS lifetimes** are common-kernel maintenance windows — not automatic OEM product multi-year OS promises.
3. **SoC public docs are uneven:** Qualcomm publishes security bulletins; MediaTek/UNISOC public multi-year matrices sparse; detailed BSP packages largely partner-only.
4. **ASB SoC fixes** require OEM integration and shipping — publication alone does not update devices.
5. **TEE/firmware/bootloader** update calendars are not standardized as public N-year consumer matrices across vendors.

## Cross references

- `research/android-ecosystem/negative-finding-android-platform-not-multi-year-device-floor.md`
- `research/manufacturers/negative-finding-oem-unified-multi-year-matrix.md`
- Phase 4 government-side no multi-year legal floor

## Consistency

Hardware/chipset layer reinforces: update *capability* architecture exists; *duration commitments* remain product/OEM/partner-specific or non-public.

## Audit trail

- Phase 5 Workstream 3
