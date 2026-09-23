# TelecomPulse Analytics — Ruflo Orchestration Layer

## Purpose

Use the orchestration model from **ruvnet/ruflo** as the coordination layer for complex TelecomPulse work while preserving the project's existing governance gates.

Ruflo-inspired orchestration answers:

- what work can run in parallel;
- which specialist role owns each subtask;
- what evidence must converge before review;
- when the coordinator must stop.

TelecomPulse governance still answers:

- what may advance;
- what constitutes PASS/FAIL;
- what requires explicit authorization;
- when a sprint can be homologated.

## Governing principle

```text
User Goal
   ↓
Ruflo-style Coordinator
   ↓
Task decomposition / dependency graph
   ↓
Specialist workers
   ├── Research / Source Validation
   ├── Data Engineering
   ├── Data Quality
   ├── Analytics / Modeling
   ├── Frontend / UX
   ├── Security / Review
   └── Test / Evidence
   ↓
Evidence convergence
   ↓
TelecomPulse Golden Rule / Gate
   ↓
PASS → next stage
FAIL → diagnose / remediate / revalidate
```

## Relationship with SKILLS_ORCHESTRATOR

The existing SKILLS_ORCHESTRATOR remains the **skill/router policy**.

Ruflo is the **coordination policy**.

```text
Ruflo-style orchestration
        ↓
SKILLS_ORCHESTRATOR
        ↓
most specific skill/tool
        ↓
governed execution
```

Ruflo must not bypass the routing rules, authorization requirements, security constraints, validation requirements or deployment gates already defined by TelecomPulse.

## Default topology

Use a **hierarchical coordinator** for multi-step work.

### Coordinator

Responsibilities:
- classify the goal;
- decompose work;
- identify dependencies;
- assign independent tasks in parallel where safe;
- keep one canonical task state;
- reconcile conflicting findings;
- enforce stop conditions;
- present a single gate decision.

The coordinator must not treat worker completion as proof of correctness.

### Workers

#### SOURCE
Owns:
- official-source discovery;
- provenance;
- source availability;
- period/granularity;
- licensing/open-data notes;
- external-source evidence.

#### DATA
Owns:
- ingestion;
- raw preservation;
- schema inspection;
- normalization;
- hashes/manifests;
- reproducibility.

#### QUALITY
Owns:
- schema checks;
- duplicates;
- missing values;
- reconciliation;
- data-quality rules;
- negative tests.

#### ANALYTICS
Owns:
- metric definitions;
- aggregation logic;
- market share;
- growth;
- territorial comparisons;
- non-additive metric methodology.

#### FRONTEND
Owns:
- presentation contracts;
- routes;
- map UX;
- accessibility;
- loading/empty/error states;
- browser behavior.

#### SECURITY_REVIEW
Owns:
- secrets;
- dependency/security checks;
- unsafe network assumptions;
- provenance spoofing risks;
- final adversarial review.

#### TEST_EVIDENCE
Owns:
- test execution;
- CI evidence;
- regression checks;
- artifact validation;
- final evidence package.

## Swarm-size rule

Use the smallest useful team.

- simple change: 1 worker + coordinator;
- normal feature: 2–3 workers;
- cross-domain feature: 3–5 workers;
- broad audit/homologation: as needed, avoiding duplicate roles.

Do not create agents merely because Ruflo supports them.

## Execution lifecycle

### 1. Goal
Capture the requested result and hard constraints.

### 2. Plan
Build a dependency-aware task graph.

### 3. Baseline
Read normative documentation and collect current test/status evidence.

### 4. Fan-out
Run independent workstreams in parallel only when their outputs do not depend on each other.

### 5. Convergence
Coordinator reconciles worker outputs and contradictions.

### 6. Validation
Run applicable tests, schema checks, reconciliations and security checks.

### 7. Evidence
Record exact commands/results/artifacts/limitations.

### 8. Gate
Apply TelecomPulse acceptance criteria.

### 9. Review
Independent review before merge/release where relevant.

### 10. Stop
Stop at the next mandatory authorization/homologation gate.

## Mandatory stop conditions

Stop and return NO-GO when:

- primary-source provenance is missing;
- a critical validator fails without diagnosis;
- source data and derived totals do not reconcile;
- required evidence cannot be produced;
- security/privacy risk is unresolved;
- a product decision is required and undocumented;
- deploy/publication lacks explicit authorization.

## Memory policy

Ruflo-style memory may retain:

- architecture decisions;
- accepted metric definitions;
- source identities;
- known aliases;
- validated test patterns;
- previously diagnosed failures;
- sprint/gate results.

Do not promote assumptions, temporary workarounds or unverified source values into canonical project memory.

## TelecomPulse R0 mapping

Current R0 orchestration:

```text
Coordinator
├── SOURCE
│   └── ANATEL/IBGE canonical sources
├── DATA
│   └── raw capture / manual registration / ZIP inspection
├── QUALITY
│   └── geography + reconciliation
├── SECURITY_REVIEW
│   └── WAF-page rejection / provenance allowlist / overwrite protection
└── TEST_EVIDENCE
    └── Ruff / pytest / v1 regression / web / Cloudflare dry-run
```

Current mandatory gate remains:

```text
official SMP raw
+ official SCM raw
+ provenance
+ SHA-256
+ real schema inspection
+ operator aliases
+ primary-source reconciliation
= R0 GO
```

## Ruflo runtime

The public Ruflo project supports a full CLI/MCP runtime with swarms, agents, hooks and memory. Its own documentation warns that full initialization writes project configuration such as `.claude/`, `.claude-flow/`, `CLAUDE.md` and helpers.

For TelecomPulse, runtime installation is **not implicit**.

Before enabling the full runtime:
1. create a dedicated branch;
2. inspect generated files;
3. compare against existing governance;
4. reject conflicting instructions;
5. run security/dependency checks;
6. merge only after explicit review.

Until then, this document defines the Ruflo-inspired orchestration policy used by the project.
