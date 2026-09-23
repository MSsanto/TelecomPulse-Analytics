# TelecomPulse Analytics — AI Memory Layer

## Purpose

Adopt the architectural pattern from **akitaonrails/ai-memory** for durable project memory and agent handoff without allowing memory to become a substitute for primary evidence.

The memory layer exists to preserve:
- validated architecture decisions;
- source identities and provenance rules;
- accepted metric definitions;
- known operator aliases after validation;
- known failures and their diagnosed causes;
- sprint/gate outcomes;
- open questions;
- handoffs between agents/work sessions.

## Core invariant

```text
Markdown/Git = canonical project memory
Index/search = derived convenience
Primary data/evidence = external source of truth
```

Memory can explain what the project previously decided.
Memory cannot prove that a current external fact is still true.

## Position in TelecomPulse architecture

```text
User Goal
   ↓
Ruflo-style Coordinator
   ↓
AI Memory recall / prior handoff
   ↓
SKILLS_ORCHESTRATOR
   ↓
Specialist workers
   ↓
Validation / evidence
   ↓
Golden Rule / Gate
   ↓
Memory promotion of validated outcomes
```

## Memory tiers

### CANONICAL
Durable, validated knowledge.

Examples:
- architecture decisions;
- metric definitions;
- accepted source URLs;
- canonical geography mappings;
- approved data contracts;
- homologation results.

Requirements:
- evidence/reference;
- date;
- owner or originating gate;
- status = validated.

### PROCEDURAL
Repeatable workflows and runbooks.

Examples:
- raw capture;
- raw registration;
- ZIP inspection;
- validation sequence;
- release/homologation runbooks.

### GOTCHAS
Known failure modes with evidence.

Examples:
- ANATEL WAF blocks automated raw downloads in some environments;
- HTML block pages must never be parsed as CSV;
- non-additive indicators must not be averaged without methodology.

### EPISODIC
Session/sprint observations.

Examples:
- temporary experiments;
- intermediate findings;
- failed approaches;
- local diagnostics.

Episodic content must not automatically become canonical.

### HANDOFF
Explicit next-agent/work-session baton.

A handoff must contain:
- current objective;
- completed work;
- evidence produced;
- blockers;
- exact next action;
- stop/gate condition.

## Promotion policy

```text
Observation
   ↓
Episodic memory
   ↓
Validation
   ↓
Evidence
   ↓
Gate PASS
   ↓
Canonical memory
```

No automatic promotion from chat/session observation directly into canonical memory.

## Contradiction policy

When new evidence contradicts memory:

1. do not silently overwrite;
2. mark the previous item as superseded or disputed;
3. preserve original evidence/date;
4. record the new evidence;
5. re-run the applicable gate;
6. promote only after validation.

Current instructions and current repository state always outrank remembered instructions.

## Memory page structure

Recommended repository-native structure:

```text
docs/memory/
├── decisions/
├── procedures/
├── gotchas/
├── handoffs/
├── gates/
└── index.md
```

Each canonical page should include:

```yaml
---
status: validated
kind: decision|procedure|gotcha|gate|handoff
validated_at: YYYY-MM-DD
evidence:
  - path-or-url
supersedes: null
---
```

## Privacy and security

Do not persist:
- secrets/tokens/passwords;
- private credentials;
- unnecessary personal data;
- transient raw payloads containing sensitive information;
- unredacted tool output that may contain secrets.

Sanitize before persistence.

## Relationship with ai-memory runtime

The upstream project provides:
- lifecycle hooks;
- cross-agent handoffs;
- markdown/git-backed wiki;
- derived SQLite/FTS index;
- optional vectors;
- audit history;
- multi-agent/multi-machine continuity.

TelecomPulse adopts these architectural ideas immediately.

The actual ai-memory runtime is not installed automatically because:
- native Windows support is experimental upstream;
- WSL2 is the supported Windows path;
- runtime installation would introduce local services/hooks/configuration;
- those changes require separate inspection and security validation.

A future runtime installation must happen in a dedicated branch and pass:
- configuration diff review;
- secret/privacy review;
- hook-scope review;
- startup/shutdown test;
- handoff test;
- recall test;
- rollback/uninstall test.

## R0 memory state

Canonical facts currently safe to retain:
- ANATEL and IBGE are the primary public-data families;
- R0 requires official SMP + SCM raw artifacts with provenance/hash/schema;
- canonical ANATEL raw ZIP URLs are documented in DATA_SOURCES;
- automatic and governed manual acquisition are accepted;
- geography model has 5 regions and 27 UFs;
- CI validations are required before gate decisions.

Current blocker/open handoff:
- obtain official SMP and SCM raw ZIP bytes;
- register provenance/hash;
- inspect real schema;
- derive operator aliases;
- execute primary-source territorial reconciliation;
- re-homologate R0.
