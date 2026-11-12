# RWCAI ♾️13 — Real World Cross-AI Collaboration Pipeline

**Document type:** Collaboration pipeline specification  
**Version:** 1.1.0  
**Status:** DOCUMENTED / OPERATIONAL INTEGRATION NOT VERIFIED  
**Governing protocol:** [ASIP ♾️13](ASIP-13.md)  
**Parent ecosystem:** AMRHZ

## 1. Name and purpose

**RWCAI** means **Real World Cross-AI Collaboration Pipeline**.

The name combines:
- **RWC** — Real World Cross
- **AI** — Artificial Intelligence

RWCAI is an initiative under the AMRHZ Shared Intelligence Protocol (ASIP ♾️13). It describes a real, evidence-backed workflow in which independent AI systems contribute to the same task through inspectable work products, review, correction, and human decisions.

The pipeline is intended to improve collaboration quality and continuity. It does not imply that participating AI products share a runtime, private memory, credentials, or a direct network connection.

## 2. What qualifies as real collaboration

A collaboration event must include at least:

1. A defined task and expected output.
2. A named participant and its assigned contribution.
3. An actual output or artifact from that participant.
4. A traceable handoff to another participant or the human owner.
5. A review, comparison, or correction step.
6. A recorded outcome and evidence reference.

Manual transfer of outputs between AI applications can qualify as a real collaboration workflow when the handoff and artifacts are recorded. It must be labelled **manual**. It must not be described as API integration, automatic dispatch, shared memory, or autonomous coordination.

## 3. Pipeline

~~~text
HUMAN INTENT
    |
    v
TASK DEFINITION + SCOPE
    |
    v
AUDIT SOURCE STATE
    |
    v
ASSIGN INDEPENDENT AI CONTRIBUTIONS
    |
    v
EXECUTE TASKS IN EACH REAL ENVIRONMENT
    |
    v
EXCHANGE VERSIONED ARTIFACTS + ATTRIBUTED CONTEXT
    |
    v
INDEPENDENT REVIEW / CHALLENGE
    |
    v
CORRECTION + RECONCILIATION
    |
    v
HUMAN ACCEPTANCE
    |
    v
VERIFY + CHECKPOINT
~~~

## 4. Collaboration modes

| Mode | Description | Evidence required |
|---|---|---|
| MANUAL | Human transfers prompts and outputs between separate AI services | Task record, source/output capture, handoff record |
| TOOL-ASSISTED | An AI uses an authorized connector or tool to access a second system or repository | Tool result, target identity, action scope, timestamp, result |
| API-INTEGRATED | Services exchange data through configured APIs | Endpoint/config reference without secrets, request/response logs, authentication and authorization evidence |
| AUTOMATED | A controlled orchestrator dispatches tasks and collects results | Execution trace, job IDs, policy decisions, failure handling, audit log |

Do not promote a workflow to a higher integration mode without evidence for that mode.

## 5. Task record

Each collaboration task should record:

- task_id
- task title and objective
- requester / human authority
- scope and prohibited actions
- participating AI systems and assigned roles
- collaboration mode
- source artifacts and immutable revisions
- expected deliverables
- actual outputs and their artifact IDs
- handoff and review records
- corrections and decisions
- verification results
- final status and next checkpoint

Use the artifact metadata schema and evidence model linked from [the artifact registry](../artifacts/README.md), and the [RWCAI task-record template](../templates/RWCAI-task-record.md).

## 6. Review and disagreement handling

- Each participant should state assumptions, evidence, uncertainty, and limitations.
- Independent review must not be reduced to copying another participant's conclusion.
- Conflicting outputs are recorded and compared against source evidence.
- The human owner resolves decisions that affect project direction or authorization.
- A correction must preserve the original finding or record the reason it was superseded.

## 7. Completion criteria

A task is **VERIFIED** only when its acceptance criteria are met and supporting evidence is available.

A task is **PARTIAL** when useful work exists but one or more acceptance criteria remain incomplete.

A task is **BLOCKED** when a concrete dependency, permission, or environment prevents progress.

A task is not complete merely because:
- an AI generated a plan;
- a message was sent without a confirmed response;
- a UI displays “connected”;
- a file name or documentation describes a feature;
- a model or service is accessible but inference or execution was not tested.

## 8. Current implementation status

The protocol and workflow are documented in this repository.

The available evidence supports that the collaboration process has been discussed and carried out through human-mediated exchanges in ChatGPT conversations. This repository does not yet contain a complete task ledger, machine-readable exchange log, verified cross-provider API integration, or automated dispatcher for RWCAI.

Therefore the honest status is:

**DOCUMENTED / MANUAL WORKFLOW DESCRIBED / AUTOMATED INTEGRATION NOT VERIFIED**

This status is intentionally conservative. It can be updated when versioned task records, tool traces, or integration tests are added.

## 9. Initial implementation roadmap

1. Create a task-record template using the artifact schema.
2. Record one end-to-end manual collaboration task with source and output references.
3. Add independent review and correction evidence.
4. Define acceptance criteria and verify the resulting artifact.
5. Evaluate whether tool-assisted or API-integrated exchange is justified.
6. Implement automation only after authorization, threat review, and a testable design.

## 10. Multi-AI context contribution and handoff

Participating AI systems may voluntarily contribute relevant context from their actual collaboration with AMRHZ when that context is available to them and permitted to be shared. Examples include task summaries, prior outputs, technical findings, owner-confirmed decisions, unresolved questions, and lessons learned.

This exchange is an explicit handoff of selected information. It is not automatic synchronization of private memories, conversations, accounts, or internal AI state.

Each context handoff should record, where available:

- contributing AI system/service;
- source conversation, artifact, task ID, or repository revision;
- date or time period;
- purpose and relevance to the current task;
- whether the contribution is a direct extract, summary, interpretation, or recommendation;
- verification and owner-confirmation status;
- uncertainty, omissions, and known limitations;
- applicable privacy, consent, and handling restrictions.

### 10.1 Handling rules

1. Preserve the original source and attribute each contribution.
2. Keep AI interpretation distinct from owner-stated information and verified facts.
3. Do not invent source metadata when it is unavailable.
4. Do not include secrets, credentials, or unrelated personal information.
5. Do not infer that one AI can access another AI's hidden memory.
6. Record disagreements and retain competing source references until reconciled.
7. Ask the human owner to clarify material conflicts or approve promotion into canonical context.
8. Treat context as input to a task, never as authorization for a consequential action.

### 10.2 Context status

Use the existing labels OWNER-STATED, SOURCE-FACT, AI-INTERPRETATION, OWNER-CONFIRMED, VERIFIED-STATE, ASSUMPTION, UNRESOLVED, and SUPERSEDED as defined by the Intent Clarification Layer.

A context handoff is not itself proof that the underlying claim is true. Verification remains tied to the specific claim and its evidence.

## 11. Governance

RWCAI operates under ASIP ♾️13. Human authority remains final for task scope, approvals, and acceptance. AI participants may analyze, propose, execute authorized work, and review evidence within their granted permissions.

---

**Principle:** Independent intelligence. Shared evidence. Attributed context. No false connection. Human-governed execution.
