# TelecomPulse v2 — Official Raw Capture Runbook

## Purpose

Close Sprint R0 blocker `R0-B01` while preserving the real requirement: **official provenance + immutable raw + traceability + validation**.

The transport mechanism is not itself a quality criterion. Two acquisition paths are accepted:

1. **automatic HTTPS capture** from the official ANATEL host;
2. **governed manual registration** of a file downloaded from the official ANATEL URL in a browser.

Both produce the same provenance requirements.

## Path A — automatic capture

```bash
python scripts/capture_official_raw.py \
  --service SMP \
  --url "<official-anatel-smp-csv-url>" \
  --output data/raw/v2/anatel/smp/<filename>.csv
```

Equivalent for SCM.

This path:
- accepts only HTTPS URLs from `anatel.gov.br`;
- rejects zero bytes;
- rejects known ANATEL WAF/block pages;
- refuses overwrite;
- writes SHA-256 and provenance metadata.

## Path B — governed manual registration

Download the file in a browser directly from the official ANATEL URL, without editing or opening/saving it in another application.

Then register it:

```bash
python scripts/register_official_raw.py \
  --service SMP \
  --file "<path-to-browser-download.csv>" \
  --source-url "<exact-official-anatel-url>" \
  --output data/raw/v2/anatel/smp/<filename>.csv
```

Optional when the browser download time is known:

```bash
  --retrieved-at "2026-09-22T20:00:00-03:00"
```

The registration:
- validates that the provenance URL is HTTPS and official ANATEL;
- rejects empty files;
- rejects a saved WAF/block HTML page;
- refuses overwrite of an existing raw;
- copies byte-for-byte;
- verifies the copied bytes;
- computes SHA-256;
- records original filename and `acquisition_method=manual_governed`.

## Success artifacts

For each raw:

```text
<filename>.csv
<filename>.csv.metadata.json
```

Metadata contains:
- service;
- exact source URL;
- retrieval/registration timestamp;
- byte size;
- SHA-256;
- response content type when available;
- governed raw path;
- acquisition method;
- original filename.

## Git policy

Official raw bytes are intentionally ignored under `data/raw/v2/anatel/` to avoid repository bloat and accidental mutation through Git workflows.

The raw remains local or in an approved artifact store. Metadata/manifests may be versioned as evidence.

## Sprint R0 GO criterion

R0 no longer requires that Python itself performs the HTTP transaction.

R0 requires, for both SMP and SCM:

1. file obtained from an official ANATEL URL by an accepted acquisition path;
2. exact source URL recorded;
3. raw bytes preserved unchanged;
4. SHA-256 recorded;
5. actual file headers/delimiter/encoding inspected;
6. service, period, geography and operator fields identified;
7. primary-source territorial reconciliation executed;
8. full validator suite green.

This changes the **transport implementation**, not the integrity standard.

## Post-capture mandatory gate

After accepted SMP + SCM raws exist:

1. inspect actual headers and delimiter;
2. document encoding;
3. identify period/geography/operator fields;
4. build aliases while preserving source names;
5. reconcile at least one state → region → Brazil path from primary data;
6. run Ruff + pytest + v1 regression;
7. update `REAL_DATA_SPRINT_0_HOMOLOGATION.md` to GO only if all checks pass.
