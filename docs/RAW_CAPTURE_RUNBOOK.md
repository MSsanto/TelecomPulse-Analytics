# TelecomPulse v2 — Official Raw Capture Runbook

## Purpose

Close Sprint R0 blocker `R0-B01` without changing the validation criteria.

The capture command accepts only HTTPS URLs from the official ANATEL host, rejects known WAF/block pages, preserves raw bytes unchanged and writes a sidecar metadata file containing timestamp, byte size and SHA-256.

## Command

```bash
python scripts/capture_official_raw.py \
  --service SMP \
  --url "<official-anatel-smp-csv-url>" \
  --output data/raw/v2/anatel/smp/<filename>.csv
```

```bash
python scripts/capture_official_raw.py \
  --service SCM \
  --url "<official-anatel-scm-csv-url>" \
  --output data/raw/v2/anatel/scm/<filename>.csv
```

## Success artifacts

For each file:

```text
<filename>.csv
<filename>.csv.metadata.json
```

Metadata contains:
- service;
- exact source URL;
- UTC retrieval timestamp;
- byte size;
- SHA-256;
- response content type;
- local raw path.

## Failure behavior

The capture exits non-zero if:
- URL is not HTTPS;
- host is not `anatel.gov.br`;
- network/download fails;
- zero bytes are returned;
- an ANATEL security/WAF block page is returned instead of raw data.

A block page must never be committed or parsed as CSV.

## Post-capture mandatory gate

After successful SMP + SCM capture:

1. inspect actual headers and delimiter;
2. preserve raw bytes unchanged;
3. document encoding;
4. identify period/geography/operator fields;
5. build aliases without destroying original names;
6. reconcile at least one state → region → Brazil path from primary data;
7. run Ruff + pytest + v1 regression;
8. update `REAL_DATA_SPRINT_0_HOMOLOGATION.md` from NO-GO to GO only if all checks pass.
