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
| G4 — code/test baseline | PASS | local 6/6 tests + GitHub Actions CI #172 fully green |
| G5 — v1 compatibility preserved | PASS | no v1 contract replacement |
| G6 — traceability rules documented | PASS | DATA_SOURCES + REAL_DATA_REBOOT + evidence |
| G7 — official raw SMP/SCM download reproducible | **FAIL / BLOCKED** | ANATEL CSV host security/WAF block in this environment |
| G8 — production raw hash/schema captured | **BLOCKED by G7** | no official raw bytes available here |

## CI evidence

GitHub Actions run #172 completed successfully across Python, web and Cloudflare-build jobs, including Ruff, pytest, npm audit, frontend tests/build, bundle budget, Wrangler deploy dry-run and static smoke tests.

Validated commit: `c3782afdb5527b3bf7aa8d3537def93526164151`.

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


---

## Re-homologation R0 — mitigation round

### Result

**NO-GO remains, now with internal mitigation fully GREEN.**

After the first homologation, a governed raw-capture path was added:

- `src/telecom_pulse/raw_capture.py`;
- `scripts/capture_official_raw.py`;
- `tests/test_raw_capture.py`;
- `docs/RAW_CAPTURE_RUNBOOK.md`.

The capture path:
- accepts only HTTPS on the official ANATEL host;
- rejects zero-byte responses;
- detects and rejects the ANATEL WAF/block HTML page;
- preserves raw bytes unchanged;
- records exact source URL, UTC retrieval time, byte size, content type and SHA-256.

### Validation

GitHub Actions CI run **#185** completed successfully:

- Python / Ruff: PASS;
- pytest: PASS;
- v1 pipeline regression: PASS;
- web audit/tests/build/bundle budget: PASS;
- Cloudflare build: PASS;
- Wrangler deploy dry-run: PASS;
- static smoke test: PASS.

CI: https://github.com/MSsanto/TelecomPulse-Analytics/actions/runs/35799086000

### External source check

The official ANATEL open-data documentation continues to identify SMP/SCM datasets as monthly official access datasets, with CSV distribution and geographic consolidations. Current SCM CSV URLs indexed by search still return an ANATEL security/WAF block page from this execution environment.

Therefore:

- internal ingestion guardrail: **PASS**;
- reproducible official raw capture in this environment: **FAIL / BLOCKED**;
- Sprint R0: **NO-GO**;
- Sprint R1 production ingestion: **NOT AUTHORIZED BY GOVERNANCE**.

No merge and no deploy are authorized by this re-homologation.
