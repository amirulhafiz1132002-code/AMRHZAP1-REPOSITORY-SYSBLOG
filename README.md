# AMRHZ / AP1 — SYSBLOG

> Development history, architecture, experiments, evidence, decisions, and documentation for the AMRHZ/AP1 ecosystem.

## Project Identity

**AMRHZ/AP1** is a human-led AI systems research and development ecosystem.

Core principles:

- **REAL STATE > UI SIMULATION**
- **EVIDENCE > CLAIM**
- **HUMAN INTENTION > AI ASSUMPTION**
- No fake READY/status, invented activity/data, hidden execution, or untraceable system state.
- GitHub is the source of truth for code, documentation, architecture, decisions, and history.

## Development Cycle

`INSPECT → UNDERSTAND → PROPOSE → HUMAN APPROVAL → IMPLEMENT → TEST → VERIFY → DOCUMENT → CHECKPOINT`

Planning is not execution. Changes are made only after human approval and are verified against real evidence.

## Ecosystem

### AMRHZ Website
Public identity and development layer.

Repository: `AMRHZ-Website`

Current direction includes the Development Hub, development tracking, changelog, architecture references, and Cloudflare-compatible deployment.

### AP1-WEB-Console
Interactive AP1 workspace direction.

Explored concepts include SEARCH → DECIDE → ANSWER → EVALUATE, operating modes, agents, memory controls, task management, and identity. Explored concepts are not automatically treated as implemented features.

### AMRHZ-AI-13
Executable AI experimentation layer.

Known components include `run.py` and `api/api_server.py`.

### Cloudflare Worker
Current Worker direction includes:

- `/`
- `/health`
- `/ping`
- `/version`
- `/status`
- `/capabilities`

### NATAN AI
Planned visual workspace direction:

- Image Generator
- Location Estimator
- Photo Editor / image tools

Provider verification and server-side image-generation paths have been explored. Real provider state must remain distinguishable from UI simulation.

### Device Lab
A secondary Android tablet is being used as a lab node alongside the main phone.

Verified tablet state at this checkpoint:

- Model reported: `ipad5pro`
- Android: 11
- Hardware evidence: MediaTek `MT6753`
- Architecture: `aarch64 / ARM64`
- RAM observed: approximately 1.16 GiB
- Swap: approximately 1 GiB
- Wi-Fi IPv4: `192.168.0.28`
- Termux username: `u0_a86`
- OpenSSH: listening on TCP `8022`
- Phone → Tablet SSH: **VERIFIED**

The tablet is treated as a **Secondary Lab Node**, not as a replacement for the main development environment.

## SYSBLOG Purpose

SYSBLOG exists to preserve the deeper story behind the system:

- Development history
- Architecture explainers
- Experiments
- Implementations
- Failures and incidents
- Troubleshooting
- Architecture decisions
- Checkpoints
- Q&A / FAQ
- Diagrams and visual documentation
- Videos and media
- Infrastructure and device-lab records

SYSBLOG should complement, not duplicate, the AMRHZ Website changelog.

### Separation of Responsibilities

| Layer | Responsibility |
|---|---|
| GitHub project repositories | Source code and implementation |
| AMRHZ Website | Public identity and development view |
| SYSBLOG | Deep history, explanations, evidence, experiments, and decisions |

## Evidence Model

Documentation should clearly separate:

1. **STATUS** — what is currently known
2. **EVIDENCE** — what was actually observed or verified
3. **OBSERVATION** — what the evidence shows
4. **DECISION** — what the human chose
5. **NEXT STEP** — what is planned, without treating plans as execution

### Example: Device Lab / SSH

A real troubleshooting sequence is part of the project history.

An incorrect `netstat -Itn` attempt was corrected to:

```bash
netstat --listening --tcp --numeric
```

The resulting state showed SSH listening on port `8022`, followed by a successful Phone → Tablet SSH login.

This is recorded as evidence, not as a claim of capability without verification.

## Protocols & Persistent Knowledge

The versioned protocol and artifact documentation is being maintained under the documentation area:

- [Documentation index](docs/README.md)
- [ASIP ♾️13 — AMRHZ Shared Intelligence Protocol](docs/protocols/ASIP-13.md)
- [RWCAI ♾️13 — Real World Cross-AI Collaboration Pipeline](docs/protocols/RWCAI-13.md)
- [Persistent artifact registry and evidence model](docs/artifacts/README.md)
- [Artifact metadata schema](schemas/artifact.schema.json)
- [Artifact registry manifest](artifact-registry.yaml)

These records define governance and metadata contracts. They do not by themselves establish live AI-to-AI connectivity, automatic dispatch, shared runtime memory, or verified implementation. See each document's status and limitations.

## Proposed SYSBLOG Structure

```text
AMRHZAP1-REPOSITORY-SYSBLOG/
├── README.md
├── 00-index/
│   ├── project-map.md
│   ├── current-state.md
│   └── navigation.md
├── 01-history/
│   ├── timeline.md
│   └── milestones/
├── 02-architecture/
│   ├── amrhz-architecture.md
│   ├── ap1.md
│   ├── system-layers.md
│   └── human-ai-model.md
├── 03-development/
│   ├── experiments/
│   ├── implementations/
│   └── checkpoints/
├── 04-infrastructure/
│   ├── cloudflare/
│   ├── termux/
│   ├── ssh/
│   └── device-lab/
├── 05-explainers/
│   ├── how-it-works/
│   └── concepts/
├── 06-qa/
│   ├── faq/
│   └── questions/
├── 07-visuals/
│   ├── diagrams/
│   └── infographics/
├── 08-media/
│   └── videos/
├── 09-incidents/
│   ├── failures/
│   └── troubleshooting/
└── 10-decisions/
    └── architecture-decisions/
```

This structure is **proposed, not locked** until reviewed and approved.

## Current Development Phase

**RESEARCH / BACKGROUND MAINTENANCE**

Current work may include:

- Technology and capability research
- Evidence observation
- Documentation
- Ideas and architecture maturation
- Checkpoint maintenance
- Device-lab exploration

Large-scale implementation remains paused until the human explicitly reopens development.

## Current Checkpoint

### VERIFIED

- SYSBLOG repository exists.
- Phone → Tablet SSH connectivity has been verified.
- Tablet SSH daemon is listening on port `8022`.
- Hardware evidence identifies the tablet platform as `MT6753`.
- Development principles and evidence-first workflow are established.

### PLANNED

- Build the initial SYSBLOG index.
- Add current-state and project-map documents.
- Record the development timeline.
- Organize architecture explainers and experiments.
- Add incident/troubleshooting records.
- Add future visual and media documentation.

### NOT YET LOCKED

- Final SYSBLOG folder structure
- Full publishing workflow
- Automated documentation generation
- Any future autonomous execution path

## Source of Truth

When documentation conflicts with observed repository or runtime state:

**Repository/runtime evidence wins.**

SYSBLOG records what was known, what was tested, what changed, and what remains uncertain.

---

**AMRHZ/AP1 — Build systems. Verify reality. Document the journey.**
