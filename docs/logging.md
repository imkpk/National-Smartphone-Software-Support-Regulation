# Logging Conventions

## Location

`logs/` — progress notes, session diaries, validation incident logs.

## Rules

- Prefer Markdown: `logs/YYYY-MM-DD_topic.md`  
- Do not commit secrets, tokens, or sealed documents  
- Large binary logs stay gitignored if added later  
- Keep entries concise: goal, files touched, next step  

## Required at phase boundaries

A short completion note when a phase exits (see Phase 1 note).

---
*Phase 1*
