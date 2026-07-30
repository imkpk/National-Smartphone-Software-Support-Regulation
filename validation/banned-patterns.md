# Banned Patterns (Hallucination Red Flags)

**Phase:** 1  
**Use:** Manual review and future linters  

## Automatic fail (BLOCKER)

| Pattern | Why |
|---------|-----|
| Case name with no reporter/neutral citation marked VERIFIED | Fabrication risk |
| “Section ___ of [Act]” without verifying Act text | Mis-citation risk |
| “Supreme Court held that India requires N years of OS updates” | No such known holding; do not invent |
| Fake Gazette / notification numbers | Fabrication |
| Exact fraud/e-waste percentages without publisher study | False precision |
| Quotation marks around judicial language without pin-cite | Misquotation risk |
| Treating EU regulations as binding Indian law | Category error |
| Wikipedia / random blog as sole LAW source | Tier failure |

## Major warnings

| Pattern | Action |
|---------|--------|
| “It is well settled that…” without case cite | Demand authority or delete |
| Brand-wide OEM support years without series scope | Narrow claim |
| Soft law described as “the Act requires” | Relabel |
| Pin-paragraph numbers not checked in full text | Mark PROVISIONAL |

## Safe practices

- Prefer “According to [source]…”  
- Use OPEN when unknown  
- Record negative findings with search log  
