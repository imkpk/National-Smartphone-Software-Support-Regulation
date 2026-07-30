# Android Update Responsibility Matrix — Phase 5 WS2

## Repository Analytical Artefact

Descriptive map from official platform documentation. **Not** legal liability allocation. **Date:** 2026-07-31

| Responsibility area | Google / AOSP | SoC vendor | OEM | Carrier (if any) | End user |
|---------------------|---------------|------------|-----|------------------|----------|
| Publish platform security fixes (bulletins) | Primary | Contributes chipset fixes | Integrates/ships | May gate OTA | Installs |
| Mainline module packages | Builds/signs (GMS path) | — | May ship partner OTA path | — | Receives Play system updates |
| Full system OTA image | Provides AOSP base | Provides BSP pieces | **Builds & ships** | May approve/distribute | Installs |
| Kernel (GKI) updates | Maintains GKI/ACK | Vendor modules | Integrates/ships device kernel package | — | Installs |
| Product support duration (years) | Pixel as OEM (WS1); platform docs ≠ industry floor | — | **Publishes policy** (WS1) | — | Purchase decision |
| App updates (user apps) | Play Store | — | Preloads vary | — | Updates apps |
| Compatibility certification (CTS/CDD) | Defines/tests program | Supports | Executes for products | — | — |

**Key descriptive takeaway:** Platform infrastructure enables updates; **device-level multi-year commitments remain OEM product policies** (Phase 5 WS1), not AOSP universal floors.
