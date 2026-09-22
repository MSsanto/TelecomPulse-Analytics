# TelecomPulse v2 — Sprint R0 Final Homologation

## Verdict

**NO-GO — one external blocking criterion remains.**

Date: 2026-09-22  
Branch: `feat/real-data-reboot-sprint0`

This is a final gate result, not an unfinished review. The Sprint R0 package was taken through architecture, implementation, tests, review and evidence collection. The only blocking criterion is explicitly identified below.

## Gate matrix

| Gate | Result | Evidence |
| --- | --- | --- |
| G0 — official sources identified | PASS | ANATEL + IBGE official documentation/catalog |
| G1 — canonical territory identity | PASS | 5 regions, 27 UFs, IBGE codes |
| G2 — additive reconciliation mechanism | PASS | Sudeste reference snapshot + tests |
| G3 — geography contract versioned | PASS | `geography-v2.schema.json` |
| G4 — code/test baseline | PASS with CI confirmation required for Ruff | 6 local pytest tests + compileall |
| G5 — v1 compatibility preserved | PASS | no v1 contract replacement |
| G6 — traceability rules documented | PASS | DATA_SOURCES + REAL_DATA_REBOOT + evidence |
| G7 — official raw SMP/SCM download reproducible | **FAIL / BLOCKED** | ANATEL CSV host security/WAF block in this environment |
| G8 — production raw hash/schema captured | **BLOCKED by G7** | no official raw bytes available here |

## Why this is NO-GO

The Sprint R0 plan defines a reproducible primary-source download as part of its GO criteria. Changing that requirement after encountering the host block would weaken the gate after the fact.

Metadata accessibility and secondary validation are not substitutes for raw primary-source ingestion.

## What is approved

The following work is approved for merge only as Sprint R0 groundwork:
- source catalog and trust hierarchy;
- v2 reboot architecture;
- canonical geographic dimension;
- strict geography schema;
- territorial reconciliation logic;
- unit tests;
- validation-only reference snapshot;
- sprint/backlog governance.

Approval of this groundwork does **not** authorize the UI to present the validation snapshot as official production data.

## Exact condition to flip to GO

R0 becomes **GO** when all items below are recorded:

- official current SMP raw file retrieved;
- official current SCM raw file retrieved;
- source URLs recorded;
- retrieval timestamps recorded;
- SHA-256 recorded;
- headers/schema inspected;
- at least one primary-source territorial reconciliation executed;
- full validator suite green.

No new product decision is required to close this gate.
