# Evidence Table Schema

Use Markdown tables or CSV under `evidence/tables/`.

## Required columns (minimum)

| column | description |
|--------|-------------|
| id | Stable row ID |
| claim_or_item | Short description |
| value | Data point |
| source_tier | T0–T4 per VALIDATION.md |
| source | Citation or URL |
| access_date | ISO date |
| status | VERIFIED / SECONDARY / UNVERIFIED |
| notes | Caveats |

## File naming

`evidence/tables/YYYY-MM-DD_short-name.md` or `.csv`
