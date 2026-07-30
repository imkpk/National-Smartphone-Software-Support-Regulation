# Phase 5 Workstream 3 Report — Hardware & Chipset Ecosystem

**Date:** 2026-07-31  
**Base main:** `7b25119` (Phase 5 WS2 merged, v0.6.2)  
**Phase 5 status:** In progress (WS3 when this merges)  
**Version:** **0.6.3**

---

## 1. Objectives

Document **hardware, chipset, kernel, and firmware** relationships that enable Android software updates and long-term device support. Descriptive technical baseline only.

## 2. Topics covered

Linux LTS · ACK · GKI · KMI · BSP · vendor_boot · firmware lifecycle · Verified Boot · TEE · bootloader/secure boot · Qualcomm · MediaTek · Tensor · Exynos · UNISOC · vendor security patches  

## 3. Key descriptive findings

| Finding | Detail |
|---------|--------|
| LTS → ACK → GKI chain | Official kernel path from kernel.org to certified GKI |
| KMI stability | Enables independent GKI vs vendor module updates when frozen |
| ACK support tables | Multi-year EOL dates published (4–6 years by branch) |
| SoC role | ASB treats SOC manufacturers as distinct fix source |
| Public chipset matrices uneven | Qualcomm bulletins strong; MediaTek/UNISOC multi-year public matrices sparse |
| Negative finding | No universal multi-year chipset/firmware consumer floor in public official docs |

## 4. Validation / Gate++

**PASS** / **PASS**

## 5. Explicitly not done

- Phase 5 **not** complete  
- Partner-only BSP deep capture  
- Phase 5 Workstream 4 — **not started**

## 6. Next

Further Phase 5 work only after merge + authorisation. **Do not auto-start WS4.**

---
