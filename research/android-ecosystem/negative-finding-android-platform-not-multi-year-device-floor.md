---
title: "Negative finding — Android platform docs are not multi-year device support floors"
domain: "android-ecosystem"
status: VERIFIED
last_updated: 2026-07-31
phase: 5
workstream: "P5-WS2"
---

# Negative Finding — Platform Documentation vs Device Support Duration

## Repository Relevance

**Tags:** Android ecosystem · Negative finding · Repository Cross Reference

## Classification

**FACT / ANALYSIS** — Scope-limited search of official Google/AOSP Android documentation. Not legal conclusions.

## Official sources [FACT]

Primary corpus: source.android.com (architecture, OTA, Mainline, GKI, CDD/CTS/VTS, security bulletins, verified boot); developer.android.com (Play Integrity, Android Enterprise); android.com (GMS, Enterprise Recommended). Access window: **2026-07-31**.

## Negative findings [FACT]

1. **No industry-wide multi-year consumer OS floor in AOSP platform docs.** Architecture, CDD, CTS, VTS, OTA, Mainline, and GKI documentation describe *how* Android can be updated and certified — not a binding N-year support duty for all commercial devices.
2. **Security Bulletin publication ≠ universal device shipping.** Monthly bulletins publish fixes; OEMs/SoCs must still integrate and ship.
3. **Mainline / Play system updates are partial.** Modular components only; kernel/vendor/non-modular surfaces remain OEM-dependent.
4. **GKI/ACK lifetimes ≠ OEM product marketing support.** Common kernel EOL tables are not substitute for per-brand consumer policies (Phase 5 WS1).
5. **GMS commercial terms** governing partner update expectations are not fully public as a single consumer-facing multi-year matrix on pages reviewed.

## Cross references

- Phase 5 WS1 OEM policies: `research/manufacturers/`
- Phase 4 government-side negative finding (no Indian multi-year OS legal floor)
- `ANDROID_UPDATE_RESPONSIBILITY_MATRIX.md`

## Consistency

Complements Phase 4 (no Indian legal multi-year floor) and Phase 5 WS1 (heterogeneous OEM private policies).

## Audit trail

- Phase 5 Workstream 2
- Official sources only
