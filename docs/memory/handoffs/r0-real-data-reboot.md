---
status: validated
kind: handoff
validated_at: 2026-09-23
evidence:
  - docs/REAL_DATA_SPRINT_0_HOMOLOGATION.md
  - docs/REAL_DATA_SPRINT_0_EVIDENCE.md
  - docs/DATA_SOURCES.md
supersedes: null
---

# Handoff — Real Data Reboot R0

## Objective

Close Sprint R0 with official ANATEL SMP and SCM primary raw evidence.

## Completed

- canonical geography model;
- geography v2 contract;
- governed automatic raw capture;
- governed manual raw registration;
- WAF/block-page rejection;
- SHA-256/provenance manifest support;
- raw ZIP inspector;
- canonical ANATEL raw ZIP URLs identified;
- CI validation green for implemented safeguards.

## Current blocker

The execution environment cannot retrieve the ANATEL raw ZIP bytes directly because the host blocks automated requests.

## Next action

Obtain the official SMP and SCM ZIPs in an accepted environment, then:

1. register source URL and raw bytes;
2. calculate SHA-256;
3. inspect ZIP members/schema;
4. identify real operator/provider fields;
5. map aliases while preserving raw values;
6. execute state → region → Brazil reconciliation from primary data;
7. run full validators;
8. re-homologate R0.

## Mandatory stop condition

Do not start R1 production ingestion or the real dashboard until R0 becomes GO.
