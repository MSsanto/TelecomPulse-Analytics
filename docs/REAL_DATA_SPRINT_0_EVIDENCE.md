# TelecomPulse v2 — Sprint R0 Evidence

## Scope

Final evidence package for Sprint R0 — Sources, contract and territory.

Branch: `feat/real-data-reboot-sprint0`

The Sprint R0 objective is to prove that the Real Data Reboot has a defensible source strategy, canonical geography, versioned contract and an auditable path to real-data ingestion before dashboard implementation.

## Normative baseline

Governance order followed:

`Normas → Baseline → Validação → Evidências → Documentação → Implementação → Revalidação → Review`

No deploy or publication was performed.

## Official source validation

### ANATEL — access datasets

Validated from official ANATEL documentation:

- SMP and SCM access collections are official regulatory datasets;
- CSV is an official distribution/collection format;
- the open-data catalog documents historical coverage and geographic aggregations including UF and Region;
- ANATEL may correct historical files retroactively.

The metadata/catalog is accessible from this execution environment.

### Raw-file access limitation

The ANATEL file host used for direct CSV distribution returned a security/WAF block to automated requests from this execution environment.

Consequences:

- official source existence: **validated**;
- official metadata/schema documentation: **validated**;
- direct raw-byte download from this environment: **not validated**;
- SHA-256 of an official raw SMP/SCM file: **not available**;
- production ingestion is therefore **not claimed** in Sprint R0.

This is an external access limitation, not evidence that the datasets are unavailable publicly.

### IBGE

Validated from official IBGE documentation:

- 2026 population estimates use 1 July 2026 as reference;
- official UF codes are available;
- Great Region codes are canonical: 1 Norte, 2 Nordeste, 3 Sudeste, 4 Sul, 5 Centro-Oeste.

## Geographic model implemented

File: `src/telecom_pulse/geography.py`

Implemented:
- 5 Great Regions;
- 27 UFs;
- two-digit IBGE UF codes;
- Great Region code and name;
- exact state-to-region membership;
- validation of unknown regions/states;
- exact coverage requirement for additive regional reconciliation;
- rejection of negative additive values.

## Contract implemented

File: `contracts/geography-v2.schema.json`

Contract characteristics:
- contract is specific to state geography;
- Brazil is fixed as country;
- region codes/names are enumerated;
- IBGE Great Region codes are enumerated;
- all 27 UF abbreviations are enumerated;
- all 27 two-digit IBGE UF codes are enumerated;
- unknown additional properties are rejected.

Cross-field semantic consistency (for example SP must belong to Sudeste) is enforced by the Python canonical model/tests; JSON Schema alone is not treated as the source of that relationship.

## Validation snapshot

File: `data/reference/smp_sudeste_2026_07.csv`

Purpose: arithmetic/territorial validation only.

The state-level values are secondary validation data from pages that identify ANATEL as their source. They are explicitly marked `VALIDATION_SECONDARY` and are **not** treated as production raw ANATEL data.

Reference snapshot:

| Geography | SMP accesses — 2026-07 | Evidence tier |
| --- | ---: | --- |
| SP | 86,765,457 | VALIDATION_SECONDARY |
| MG | 27,665,157 | VALIDATION_SECONDARY |
| RJ | 22,093,588 | VALIDATION_SECONDARY |
| ES | 5,014,235 | VALIDATION_SECONDARY |
| Sudeste | 141,538,437 | DERIVED_VALIDATION |
| Brasil | 279,184,156 | PRIMARY_OFFICIAL national reference |

Arithmetic proof:

`86,765,457 + 27,665,157 + 22,093,588 + 5,014,235 = 141,538,437`

This proves the geographic reconciliation mechanism for the Sudeste reference snapshot. It does **not** prove full Brazil = sum(27 UFs) because the official raw file was not downloaded.

## Tests

File: `tests/test_geography_v2.py`

Local execution:
- pytest: **6 passed**;
- Python compileall: **passed**;
- local Ruff: **not executed**, because the Ruff binary is not installed in the local execution runtime used for this validation.

Tests cover:
- exactly 5 regions;
- exactly 27 UFs;
- unique IBGE UF codes;
- canonical SP identity;
- exact Sudeste membership;
- additive Sudeste reconciliation;
- rejection of incomplete regional coverage;
- rejection of cross-region state contamination.

GitHub Actions CI run **#172** for PR #10 completed successfully on commit `c3782afdb5527b3bf7aa8d3537def93526164151`.

Validated in CI:
- `ruff check src tests`: PASS;
- full `pytest -q`: PASS;
- legacy v1 pipeline/presentation generation: PASS;
- frontend npm audit high/critical gate: PASS;
- frontend tests/build/bundle budget: PASS;
- Cloudflare production deploy dry-run: PASS;
- local static smoke test: PASS.

CI URL: https://github.com/MSsanto/TelecomPulse-Analytics/actions/runs/35798324643

## Regression scope

The Real Data Reboot does not replace or mutate:
- `dashboard-v1.schema.json`;
- the v1 synthetic incident model;
- the current v1 frontend runtime contract.

The new geographic model is additive and isolated.

## Security/privacy

- no credentials or tokens introduced;
- no personal data introduced;
- no private operational data introduced;
- reference data is public-market information;
- no deploy performed.

## Open blocker

**R0-B01 — Reproducible official raw download**

The current Sprint R0 gate requires a reproducible primary-source download. That proof is not available from this execution environment because the ANATEL CSV host blocks automated retrieval.

To close:
1. download one current official SMP CSV and one SCM CSV from an environment accepted by the ANATEL host;
2. preserve the raw bytes unchanged;
3. record source URL, retrieval timestamp, byte size and SHA-256;
4. inspect actual headers/dtypes;
5. run a minimal parser;
6. re-run territorial reconciliation against the primary raw sample.

Until R0-B01 is closed, the project must not label the reference snapshot as production ANATEL ingestion.
