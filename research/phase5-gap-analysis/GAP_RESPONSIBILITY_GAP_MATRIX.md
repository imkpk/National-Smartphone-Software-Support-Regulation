# Responsibility Gap Matrix — Phase 5 WS5

## Repository Relevance

Describes responsibility **splits and absences** from WS1–WS4. **Date:** 2026-07-31

## Classification

**ANALYSIS** — Not legal liability assignment.

## Evidence sources

WS2 ANDROID_UPDATE_RESPONSIBILITY_MATRIX · WS3 FIRMWARE_RESPONSIBILITY_MATRIX · WS4 responsibility-matrix

## Cross references

`responsibility-gaps.md` · `GAP_MATRIX.md`

## Negative findings

No single industry-wide multi-year owner (R-G1).

| Function | Who is described as acting | Public multi-year duration owner? | Gap note |
|----------|----------------------------|-----------------------------------|----------|
| ASB platform fix content | Google/AOSP | No (publication cadence, not device years) | A-G2 |
| Kernel LTS/ACK/GKI | Google kernel + upstream | ACK branch EOL tables exist; not product years | H-G2 |
| SoC firmware fixes | SoC vendors | Rarely as open consumer multi-year matrix | H-G1/H-G3 |
| Device OTA ship | OEM | Where OEM publishes product policy (WS1) | M-G2 residual |
| Mainline modules | Google (+ OEM eligibility) | Partial surface only | A-G3 |
| Industry-wide floor | — | **Not identified** | R-G1 / U-G1 |
| Post-OEM EOL security | Not established as single rule | Residual OPEN | R-G5 |
