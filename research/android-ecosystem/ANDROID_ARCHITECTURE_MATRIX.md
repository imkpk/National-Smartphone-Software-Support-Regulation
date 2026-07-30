# Android Architecture Matrix — Phase 5 WS2

## Repository Analytical Artefact

**Not** an official Google publication. **Date:** 2026-07-31

| Layer / concept | Official role (descriptive) | Update relevance |
|-----------------|----------------------------|------------------|
| Apps (user) | Third-party / preloaded apps | Play app updates ≠ OS patches |
| Android framework | Public + system APIs | Platform OTAs / some Mainline modules |
| System services | Modular system components | Mainline candidates where modularized |
| ART | Runtime | Mainline ART module (from Android 12) |
| HAL / vendor interface | Vendor hardware abstraction | Vendor partition; VTS |
| Native daemons/libs | Low-level userspace | Platform/vendor as applicable |
| GKI kernel + vendor modules | Unified core kernel + modules | Kernel security via GKI/ACK + vendor modules |
| Verified Boot / AVB | Chain of trust + rollback | Protects integrity of installed images |

| Compatibility artefact | Role |
|------------------------|------|
| CDD | Policy requirements for compatibility |
| CTS | Automated compatibility tests |
| VTS | Vendor kernel/HAL tests |
| VINTF matrices | Required HAL interfaces per release |
