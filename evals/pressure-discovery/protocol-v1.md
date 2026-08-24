# Pressure Discovery Protocol v1

Status: provisionally frozen methodology  
Target skill: Marketing Practitioner v0.5.1  
Frozen target commit: 4278758a9bd31bde4278f634f58e3dcff3187fea  
Protocol mode: Pressure Discovery  
Implementation status: methodology only; pilot not implemented

---

## 1. Purpose

Pressure Discovery exists to produce realistic failure observations whose causes can be investigated with defensible confidence.

Its purpose is to:

- discover unknown failure families in consequential marketing decisions;
- reject or repair invalid scenarios, oracles, and judgments before blaming the executor;
- distinguish evaluator failure, execution variance, task delivery, activation, routing, local knowledge, handoff, inference, authority, and scope failures;
- preserve negative, inconclusive, and no-action findings;
- identify candidates for later frozen evaluations;
- make shared-architecture reopening exceptionally difficult.

Pressure Discovery is not:

- a benchmark or leaderboard;
- a prompt-volume exercise;
- evidence that Marketing Practitioner wins marketing;
- a handbook-conformance test;
- permission to generate a single aggregate score;
- an architecture-discovery shortcut;
- permission to add a campaign, journey, lifecycle, CRM, GTM, media-planning, market-entry, product-portfolio, or other shared abstraction.

The governing success criterion is:

> The factory can produce realistic failure observations while remaining capable of discovering that the scenario, rubric, judge, execution process, or missing authority — rather than Marketing Practitioner — was the thing that failed.

When causal localization is not supported, the required result is F12 — Unresolved Attribution. Missing mechanism evidence returns F12; it must never be imputed from outcome text or evaluator intuition.

---

## 2. Pressure Discovery and Frozen Evaluation

The protocol distinguishes two modes.

### Mode A — Pressure Discovery

Purpose:

- discover unknown failure families;
- explore difficult real-world decisions;
- mutate and revise scenarios;
- inspect disagreements;
- generate new cases from emerging failures.

Properties:

- scenario population may evolve;
- rubrics may be corrected;
- rejected scenarios are expected;
- there is no headline benchmark score;
- no frozen comparative-performance claim is allowed.

This protocol governs Mode A.

### Mode B — Frozen Evaluation

Purpose:

- measure a specific already-known behavior or failure family.

Properties:

- scenario population frozen;
- prompts and artifacts frozen;
- rubric frozen;
- target commits frozen;
- execution configuration frozen;
- adjudication protocol frozen;
- no cases added after observing results until a new benchmark version.

A Pressure Discovery finding may become a candidate for Mode B only through the promotion rules in this protocol. Mode A results must never be silently reported as Mode B performance.

---

## 3. Independence and Role Separation

Scenario construction begins from externally plausible decision reality, not the Marketing Practitioner handbook.

The required order is:

~~~text
EXTERNAL DECISION TRACE
→ immutable provenance snapshot
→ framework-blind scenario editing
→ framework-blind oracle construction
→ validity and rubric attacks
→ scenario and oracle run-lock
→ framework-leak audit
→ post-lock decision-family and route mapping
→ execution
→ blind behavioral judgment
→ counterfactual attribution
~~~

### Required role separation

- Source curator: sees external source material and the sampling protocol; does not see the repository, route table, eval prompts, or failure taxonomy.
- Scenario editor: turns one decision episode into a user-visible task; does not use handbook or controller vocabulary.
- Oracle author: sees the external dossier and scenario; does not use the handbook as the source of truth.
- Validity attacker: did not author the scenario or oracle.
- Framework-leak auditor: may inspect the repository only after scenario and oracle lock.
- Post-lock mapper: may map the accepted case to zero, one, or several current routes.
- Executor: sees only the user-visible task and the assigned execution condition.
- Blind judge: sees the contract predicates but not condition identity, route expectations, or proposed failure class.
- Attribution investigator: sees operational traces only after behavioral judgment is locked.
- Adjudicator: did not author the scenario, oracle, candidate output, or proposed fix.

An independent subagent is not automatically a clean-room author if it inherited repository or brief context. Access boundaries and author attestations are part of provenance.

### Quarantined scenario seeds

The following may not seed, paraphrase, template, balance, or oracle the ecological pressure population:

- current files under evals;
- SKILL.md;
- routing-index.json;
- handbook and platform modules;
- task-specification guides;
- practitioner cards and quality rubrics;
- Commercial Design research artifacts;
- repository evidence ledgers used as a case-selection inventory.

They may be used only for:

- legacy regression testing;
- contamination canaries;
- post-lock route mapping;
- failure attribution against an existing owner;
- future local regression after a correction.

Current eval repetitions are regression depth, not independent recurrence.

---

## 4. End-to-End Pressure Discovery Architecture

Use two segregated lanes.

### Ecological pressure lane

Cases reconstructed from:

- consented operational artifact bundles;
- practitioner critical incidents;
- primary public decision records or postmortems;
- timestamped multi-artifact public reconstructions.

These cases may support realism, independent recurrence, and future targeted-evaluation promotion.

### Diagnostic injection lane

Cases with planted:

- scenario defects;
- oracle defects;
- activation failures;
- routing failures;
- local-knowledge omissions;
- handoff losses;
- execution variance;
- false architecture-gap appearances.

These cases test the factory itself. They do not count as ecological evidence, independent real-world recurrence, or Marketing Practitioner performance.

### Processing flow

~~~text
SOURCE EPISODE
→ provenance graph
→ decision-time reconstruction
→ user-visible task
→ hidden scenario contract
→ validity gate
→ run-lock
→ post-lock mapping
→ matched execution
→ blind judgment
→ triggered repetition where justified
→ controlled attribution ladder
→ finding ledger
→ recurrence and promotion gates
~~~

No scenario generator may act as its own final validator, judge, or architecture adjudicator.

---

## 5. Scenario Provenance

Every ecological case records:

- provenance root;
- source class;
- organization or episode identifier;
- decision-time cutoff;
- source dates;
- source-lineage graph;
- shared-root relationships among derivative artifacts;
- source-to-scenario transformation log;
- anonymization, redaction, fabrication, and compression;
- author repository-access attestation.

Recommended source classes:

- P1: primary operational dossier;
- P2: practitioner critical incident, preferably corroborated;
- P3: primary public decision, official postmortem, or adjudicated record;
- P4: public multi-artifact reconstruction from timestamped primary materials;
- P5: community thread, review corpus, or anecdotal account used only as a seed pending corroboration;
- S: synthetic diagnostic or mutation, excluded from ecological claims;
- X: current repository material, prohibited as a pressure-population seed.

Two reports about the same event are one provenance root. Twelve derivative notes from two interviews remain two root sources.

At least one accepted clean-room case in the methodology-validation pilot must remain unmapped or multiply mapped after post-lock mapping. A case must not be rewritten merely to make it fit the current architecture.

---

## 6. Scenario Contract

The Scenario Contract is the smallest hidden record sufficient to validate and adjudicate one case.

### Required block 1 — Identity and version

- scenario ID and version;
- oracle/rubric version;
- provenance-root ID;
- contract author and independent validator identities.

### Required block 2 — External provenance

- source class and decision-time cutoff;
- root episode and source-lineage graph;
- raw-source snapshot reference;
- transformation and redaction log;
- framework-access attestation.

### Required block 3 — Exact user-visible package

- exact prompt;
- exact artifacts;
- acting role presented to the executor;
- tools and external evidence available;
- material facts visible to the executor.

Hidden evaluator facts may not silently select a correct world.

### Required block 4 — Decision record

- consequential decision, transformation, claim, or action at stake;
- decision owner and authority;
- objective and material consequence;
- deadline, reversibility, or loss asymmetry only when material.

### Required block 5 — Evidence and state ledger

For each material proposition:

- proposition;
- status: established, reported, inferred, unknown, or conflicted;
- provenance and authority;
- executor visibility;
- fixed or committed versus unresolved status;
- temporal, commercial, audience, or dependency attributes when material.

This block replaces separate universal fields for facts, unknowns, confounders, resolved state, commercial state, time, audience, and authority.

### Required block 6 — Oracle

- primary truth type;
- resolved-state and authority modifiers;
- semantic hard MUST predicates;
- semantic hard MUST-NOT predicates;
- MAY and valid-variation rules;
- pass-sufficiency rule;
- consequential disqualifying errors.

### Required block 7 — Validity docket

- strongest two-world underspecification witness;
- fluent but decision-wrong anchor;
- defensible noncanonical anchor;
- validity disposition;
- validator identities and rationale.

### Conditional fields

- pair ID, mutation, consistency closure, held-constant facts, and expected relation;
- post-lock decision label and decision-structure tags;
- deliberately manipulated difficulty factors;
- route or owner hypothesis, sealed from behavioral judges and used only when routing is under test;
- non-gating communication requirements.

### Rejected universal fields

- business archetype or decision family as a scenario-generation input;
- exact preferred answer;
- universal material routing expectation;
- handbook chapter names in the oracle;
- separate mandatory commercial, time, audience, authority, confounder, and resolved-state sections;
- free-text acceptable-answer space without semantic predicates;
- duplicated failure conditions;
- scalar difficulty.

---

## 7. Truth and Oracle Model

Use three primary truth types.

### T1 — Determinate state or fact

A material fact or boundary is:

- visible;
- derivable from visible evidence; or
- obtainable through explicitly available tools.

Judge factual correctness, source authority, and scope.

If reasonable compatible worlds disagree about the fact, the case is not T1.

### T2 — Bounded decision

One sufficiently specified world permits several defensible actions or recommendations.

Judge:

- hard obligations;
- hard prohibitions;
- evidence and authority constraints;
- claim-action coherence;
- decision consequences.

Do not judge preferred wording or one favored method.

### T3 — Underdetermined decision

Plausible worlds compatible with the visible task require different ultimate choices.

Correct behavior may be:

- preserving uncertainty;
- identifying discriminating evidence;
- providing conditional branches;
- taking a bounded reversible action;
- retaining the baseline.

A T3 answer must do more than say that it depends or request generic research. The proposed evidence or action must be decision-relevant and feasible under the stated constraints.

### R — Resolved-state modifier

An upstream decision is protected unless it is:

- contradictory;
- materially stale;
- unsupported for a required claim;
- infeasible;
- materially insufficient for the requested downstream job.

R is orthogonal to T1/T2/T3.

### A — Authority/dependency modifier

Marketing reasoning should progress as far as it legitimately can, then stop, condition, or escalate at the authoritative boundary.

Acknowledging a dependency does not permit bypassing it. Stopping immediately without completing available marketing work is also not automatically correct.

A is orthogonal to T1/T2/T3.

Examples include T2+R, T3+A, and T2+R+A. No additional truth type is needed.

---

## 8. Predicate-Based Oracle Design

The oracle is a minimal set of semantic predicates over claims, actions, constraints, and cross-case relations.

Mere mention never satisfies a predicate.

Each hard predicate records:

- activation condition from scenario state;
- target: claim, inference, action, artifact, or relation;
- required or forbidden semantic relation;
- material consequence;
- acceptable satisfaction modes;
- external or scenario-stipulated provenance;
- hard or soft status.

Universal hard concerns, where material:

1. state and evidence fidelity;
2. inference license;
3. decision and constraint validity;
4. claim-action coherence;
5. task fulfillment;
6. relation fidelity for paired cases.

Soft quality includes elegance, organization, tone, and preferred analytical method unless the scenario predeclares a material reason to make one hard.

### Required oracle attacks

Every candidate rubric must reject:

- keyword-complete wrong answers;
- disclaimers followed by contradictory actions;
- invalid discriminating checks;
- conditional laundering of unsupported claims;
- authority acknowledged and then bypassed;
- excessive caution that fails to complete the task;
- generic unchanged answers across sensitivity pairs.

Every candidate rubric must accept:

- concise semantic satisfaction;
- a defensible alternative method;
- justified abstention or partial completion;
- a reversible bounded action under uncertainty;
- a noncanonical recommendation inside the acceptable decision space.

Any novel defensible answer that exposes an omitted valid path triggers oracle review before executor failure.

---

## 9. Scenario Validity Gate

The ten validity attacks are grouped into five non-compensatory decisions.

### Reality and materiality

- V1 Realism: plausible actor, chronology, artifacts, feasible actions, constraints, and consequences.
- V2 Decision relevance: consequential open action, claim, inference, or evidence decision.
- V8 Materiality: the tested distinction changes an action, allowed claim, authority boundary, or required evidence.
- V10 Real-world prior: the main burden is marketing judgment, not puzzle-solving, arbitrary recall, or context-window endurance.

### Specification

- V3 Underspecification: construct at least two minimally different plausible worlds compatible with every visible statement.

Disposition:

- overlapping acceptable behavior at the requested level → T1 or T2 may stand;
- different ultimate choices but a useful common policy → deliberate T3;
- hidden-world-specific action required → rewrite or reject.

### Oracle robustness

- V6 False-positive attack: fluent but materially wrong answer must fail.
- V7 False-negative attack: defensible noncanonical answer must pass.

### Independence and leakage

- V4 Answer leakage: wording must not unnecessarily reveal the tested concept.
- V5 Framework shaping: the case and oracle must be reconstructible from external material without Marketing Practitioner terminology.

### Attribution viability

- V9 Attributability: the case supports at least one discriminating counterfactual, or its mechanism confidence is explicitly capped at F12.

### Dispositions

- Accept for discovery: all applicable hard gates pass.
- Rewrite: the originating real decision remains intact and the defect is repairable.
- Reject: artificial decision, hidden-world oracle, framework recall, immaterial distinction, or irreparable ambiguity.
- Run-lock: accepted prompt, artifacts, contract, oracle, and relation become immutable for the execution bundle.

No weighted validity score is permitted.

---

## 10. Sensitivity, Invariance, and Metamorphic Cases

Use a pair when correctness is better expressed as a relation than a standalone answer.

### Sensitivity

A material fact changes, so at least one semantic behavior must change.

Examples:

- approval pending versus granted;
- two root interviews versus twelve independent interviews;
- immature versus fully matured cohort;
- ineligible versus eligible buyer;
- absent versus established response opportunity.

### Invariance

A demonstrated non-causal nuisance changes, so the material decision behavior remains stable.

Safer nuisance examples:

- founder name;
- document formatting;
- unrelated company-history detail;
- unrelated vanity metric.

Platform, country, industry, and demographic nouns are not presumed irrelevant. Their decision path must be neutralized or the invariance claim rejected.

### Minimum coherent intervention

Change one target fact plus only its logical consistency closure.

Permitted collateral changes:

- facts logically entailed by the target change;
- date arithmetic needed for time-state coherence;
- action feasibility directly caused by the target change;
- grammar and entity-reference repairs.

Any collateral fact that can independently explain the expected output difference invalidates the pair.

### Held constant

Unless targeted:

- decision and deliverable;
- actor and authority;
- objective;
- evidence and unknowns;
- resolved state;
- causal structure;
- commercial conditions;
- time horizon;
- tool and external-evidence access;
- output constraints;
- execution configuration.

### Expected relation

Normalize outputs over:

- D: decision or selected action;
- E: evidence interpretation;
- U: uncertainty;
- S: resolved/open state;
- A: authority handling;
- N: next action or discriminating evidence;
- R: observable decision-domain footprint;
- C: communication, secondary to correctness.

Relations may require:

- preserve;
- semantically same;
- change to;
- add;
- drop;
- tighten;
- loosen;
- nonincrease;
- nondecrease;
- permitted variance.

Judge each member independently before revealing the relation. A pair passes only if:

1. both outputs are independently acceptable; and
2. the required relation holds.

Two equally wrong answers cannot pass invariance. Different wording cannot fail invariance.

Pair siblings share lineage and count as one case family, not independent recurrence.

---

## 11. Difficulty, Decision, Archetype, and Composition Coverage

Do not compute a scalar difficulty score.

Record only factors deliberately present or manipulated:

- evidence insufficiency or ambiguity;
- evidence conflict and provenance distance;
- causal identifiability;
- temporal lag, maturity, censoring, or history;
- actor and authority coupling;
- dependency and composition depth;
- decision pressure, reversibility, and opportunity cost;
- mediation and observability;
- source-grounded irrelevant or misleading cues.

Commercial state and platform presence are coverage attributes unless they materially increase one of these factors.

### Optional case-structure descriptors

- clean isolated decision;
- genuine composition;
- source-derived messy case;
- source-derived near miss.

These are construction descriptors, not lifecycle states or scores. No fifth layer is required.

### Post-lock decision-family mapping

Use externally recognizable decision actions:

1. understand or synthesize evidence;
2. select or deprioritize a market, customer group, opportunity, or partner;
3. define or change category, positioning, or value;
4. set or change price, package, terms, eligibility, or commitment;
5. publish, withhold, revise, or adapt a claim or representation;
6. allocate, stop, or reallocate distribution or resources;
7. diagnose performance and choose the next check or action;
8. test, roll out, hold, reverse, or retain an intervention;
9. transfer or localize a prior decision;
10. preserve, revise, or retire organizational learning;
11. proceed, defer, or escalate across an authority boundary.

Handbook routes are a secondary crosswalk only.

### Structurally distinct business contexts

Use archetype diversity only when decision structure changes:

- self-serve digital subscription;
- enterprise or account-based business with distributed authority;
- inventory/returns/fulfillment-constrained commerce;
- capacity-constrained local or professional service;
- two-sided or platform-mediated business;
- regulated or high-substantiation-risk offering.

International and multi-product complexity are modifiers, not mandatory archetypes.

Composition is recorded as the actual dependency edges observed in accepted cases. Do not generate cases merely to fill a predefined composition cell.

---

## 12. Execution Protocol

For comparative Pressure Discovery:

- Condition A: same base model and host scaffold without Marketing Practitioner.
- Condition B: same base model and host scaffold with exact Marketing Practitioner v0.5.1 at the frozen target commit.

The only intended delta is skill availability through the normal activation mechanism.

### Control or record

- provider and exact model deployment/snapshot where exposed;
- reasoning mode and generation configuration;
- temperature, top-p, seed, penalties, output limit, stop and tool-choice policy;
- complete common system/developer scaffold and message order;
- host version, retry, timeout, truncation, and compaction policy;
- exact visible input;
- tools, schemas, permissions, credentials, and resource ceilings;
- locale, timezone, date, and working environment where material;
- external-evidence snapshot;
- fresh-context identifier;
- skill ID/version/tree hash and activation receipt;
- route requests and resource-access outcomes;
- output, tool trace, errors, request ID, and finish state;
- temporal execution block and A/B order.

The baseline must not be able to discover the skill through filesystem or web access. Do not pad the baseline context to mimic skill length.

Every attempt uses a fresh context with no prior case, answer, rubric, judge discussion, retained scratch state, or treatment label.

Counterbalance A→B and B→A across cases and keep paired calls close in time.

Prefer closed-book or frozen-evidence cases. For live retrieval, replay identical evidence before attributing a reasoning difference.

### Repetition

Default screen:

~~~text
A1 / B1
~~~

Trigger repetition when:

- either arm materially fails;
- arms differ on a hard invariant;
- a metamorphic relation fails;
- judges disagree materially;
- activation, tools, truncation, or environment may have varied;
- the finding is considered for promotion.

Diagnostic escalation:

~~~text
A1 / B1
A2 / B2
A3 / B3
~~~

Three runs per arm can reveal:

- mixed material behavior;
- a singleton;
- recurrence under the tested configuration.

They cannot estimate a reliable failure rate, establish statistical significance, or prove determinism.

Use recurrent under configuration, not deterministic defect, unless deterministic replay or a static mechanical defect plus decisive intervention exists.

Meaning-preserving paraphrases test prompt robustness, not execution variance.

---

## 13. Blind Judgment and Adjudication

For the methodology-validation pilot, use two independent human judges for every packet.

Judges receive:

- opaque case and candidate IDs;
- complete user-visible task;
- complete candidate output;
- frozen contract and rubric version;
- truth type and modifiers;
- material facts, unknowns, and authority boundaries;
- semantic predicates and fatality;
- acceptable variation without a preferred exemplar.

Judges do not receive:

- baseline or skill identity;
- model name, commit age, or candidate recency;
- expected failure class;
- route or architecture hypothesis;
- prior judge results;
- preferred answer;
- execution traces during behavioral judgment.

Candidates are judged separately in counterbalanced order. Comparative or metamorphic judgment occurs only after individual records are locked.

### Criterion order

1. decision correctness or posture;
2. evidence fidelity;
3. uncertainty calibration;
4. material and resolved-state preservation;
5. authority/dependency correctness;
6. observable routing/composition appropriateness;
7. usefulness/actionability;
8. communication quality.

Criteria 1–5 contain fatal gates. Communication cannot compensate for wrong decision logic.

### Judge output

For each criterion:

- satisfied;
- violated;
- not assessable;
- not applicable.

Also record:

- output evidence span;
- controlling contract clause;
- short rationale;
- fatal violations;
- overall acceptable, unacceptable, or indeterminate;
- confidence and reason;
- blocking evaluator challenge where applicable.

### Mandatory adjudication

Adjudicate when:

- overall dispositions differ;
- any fatal predicate differs;
- either judge raises a blocking scenario/oracle challenge;
- one judge is indeterminate and another decisive;
- a material interpretation differs;
- a comparison or relation differs and would be reported;
- a low-confidence result would be promoted.

The third human adjudicator judges de novo before seeing prior rationales. Adjudication may return:

- confirmed disposition;
- judge error;
- rubric defect;
- scenario invalidity;
- legitimate indeterminacy.

Adjudication is not majority voting.

LLMs may check form completeness, extract passages, generate adversarial rubric anchors, and cluster rationales after decisions are locked. They may not serve as the decisive second judge or final adjudicator.

---

## 14. Run-Evidence Contract

The run-evidence contract enables privacy-safe attribution among F3–F6.

Observability means externally visible operational facts. It does not mean access to hidden reasoning.

### Tier 1 — Always recorded

Every run records:

1. run binding;
2. task delivery digests;
3. activation receipt;
4. knowledge requests;
5. knowledge-resolution and executor-access outcomes;
6. final result and sealed event-log completeness.

### Tier 2 — Diagnostic only

After a material failure or attribution dispute, record:

- expected-route hypothesis created after scenario/oracle lock;
- forced-route intervention;
- irrelevant-route negative control;
- frozen knowledge section when adequacy must be reviewed;
- neutral local-knowledge injection;
- placebo knowledge control;
- native boundary artifact if already exposed;
- controlled minimal state capsule;
- isolated upstream/downstream owner outputs;
- intervention and repeat-group manifests.

### Prohibited evidence

Never require:

- hidden chain-of-thought;
- model scratchpads;
- unrestricted internal token traces;
- internal attention or latent activations;
- model self-report about what it used;
- inferred reasoning paths reconstructed from prose;
- a universal runtime state ontology created for evaluation.

### Meaning of resource access

A resource-access event establishes only that the exact content was successfully made available to the executor.

It does not establish that the model:

- noticed it;
- understood it;
- retained it;
- applied it;
- complied with it.

This boundary is essential to avoid labeling generic noncompliance as routing failure.

---

## 15. Event Vocabulary

Every event contains:

- run ID;
- immutable event ID;
- strictly increasing sequence number;
- event-schema version;
- payload digest.

Wall-clock time is required for RUN_BOUND and RUN_SEALED. Sequence order is authoritative for intermediate events.

### RUN_BOUND — always

Purpose:

- bind intended task to actual execution.

Minimum fields:

- scenario/oracle/condition IDs and hashes;
- intended and delivered visible-input digests;
- common-scaffold digest;
- model/configuration digest;
- tools/permissions digest;
- external-evidence digest;
- fresh-context ID;
- start time.

Resolves:

- task-delivery failure versus downstream failure;
- unrelated host-context drift;
- invalid counterfactual matching.

### SKILL_ACTIVATION — always

Purpose:

- record whether the intended skill condition became active.

Minimum fields:

- intended condition;
- requested skill ID/version/hash;
- active skill ID/version/hash;
- outcome: activated, not-activated, error, fallback, or not-intended;
- activation error reference.

Resolves:

- F3 versus F4–F6;
- wrong skill/version versus correct activation.

### KNOWLEDGE_REQUEST — always when issued

Purpose:

- record externally observable logical-route or direct-resource requests.

Minimum fields:

- request ID;
- request kind: logical route, direct resource, or evidence source;
- requested logical/resource ID;
- initiator: normal execution or forced intervention.

Resolves:

- route never requested;
- wrong route requested;
- direct resource access without a logical-route request.

### KNOWLEDGE_ACCESS — always for each request

Purpose:

- record resolution and executor availability.

Minimum fields:

- request ID;
- route ID where applicable;
- resolution status;
- delivery status;
- resolver mode: helper, index, direct, or fallback;
- route-index hash;
- resource ID/hash;
- selector hash;
- extracted-content hash;
- fallback or error status.

Resolves:

- request omission versus resolver failure;
- wrong resource versus expected resource;
- resolution failure versus successful delivery;
- normal path versus fallback.

### BOUNDARY_TRANSFER — diagnostic H1 only

Purpose:

- compare state emitted and received at an already observable boundary.

Minimum fields:

- boundary ID;
- source/destination owner labels;
- upstream artifact hash/ref;
- downstream-received artifact hash/ref;
- scenario-specific critical-assertion IDs;
- transfer status.

Resolves:

- handoff loss versus inadequate upstream or downstream local reasoning.

No universal state schema is required.

### INTERVENTION_APPLIED — diagnostic only

Purpose:

- make the single causal delta explicit.

Minimum fields:

- intervention type;
- version/hash;
- target;
- delta manifest;
- held-constant manifest;
- control/intervention label;
- negative-control reference.

Resolves:

- selective repair versus broad context or prompt changes.

### RUN_SEALED — always

Purpose:

- close the run and make event absence interpretable.

Minimum fields:

- final-output hash;
- finish/error/truncation status;
- event count;
- ordered trace-root hash;
- telemetry-completeness status;
- end time.

Resolves:

- no event occurred versus telemetry was incomplete;
- valid failure versus incomplete operational evidence.

### Rejected separate events

- RUN_START and TASK_BOUND: merged into RUN_BOUND.
- ROUTE_RESOLVED and RESOURCE_ACCESSED: merged into KNOWLEDGE_ACCESS.
- universal boundary-state event: diagnostic-only.
- duplicate generic tool events: reference the host tool log by digest.

---

## 16. Failure Taxonomy

Use the taxonomy in layers:

1. evaluator validity: F0/F1;
2. execution stability: F2;
3. behavioral tags: F7/F8/F9;
4. supported mechanisms: F3–F6 and F10;
5. F11 as a family-level architecture-research status;
6. F12 when evidence cannot localize.

### F0 — Scenario invalid

Definition:

- contradictory, unrealistic, non-consequential, or hidden-world-dependent case.

Positive evidence:

- two compatible worlds require incompatible actions and no useful common policy exists.

Nearest confound:

- F1, where the scenario is valid but scoring is defective.

Minimal counterfactual:

- add the single discriminating fact or deliberately reclassify T3.

Escalation:

- quarantine; invalidate affected results; rewrite or reject.

### F1 — Rubric/oracle defect

Definition:

- the acceptance rule accepts a decision-wrong answer or rejects a defensible one.

Positive evidence:

- fluent-wrong anchor passes or noncanonical-good anchor fails.

Nearest confound:

- F0 or judge misapplication.

Minimal counterfactual:

- correct only the rubric and blindly rejudge unchanged outputs.

Escalation:

- new rubric version; rejudge every affected output.

### F2 — Execution/model variance

Definition:

- material dispositions differ across exact-configuration fresh runs.

Positive evidence:

- pass/fail or invariant-preservation flips after judge instability and activation drift are ruled out.

Nearest confound:

- judge/rubric instability or environment drift.

Minimal counterfactual:

- exact rerun with frozen input, configuration, and evidence.

Escalation:

- report mixed or recurrent behavior; do not infer mechanism or rates.

### F3 — Task-specification/activation failure

Definition:

- the validated task or intended skill condition did not reach the executor intact.

Positive evidence:

- material task/scaffold digest mismatch;
- explicit activation failure;
- wrong active skill hash;
- selective repair after correcting only delivery or activation.

Nearest confound:

- F0, F4, or generic noncompliance.

Minimal counterfactual:

- correct only delivery or force exact skill activation.

Escalation:

- fix harness/task delivery; do not edit marketing knowledge.

### F4 — Routing failure

Definition:

- exact skill activated; sufficient existing route was necessary; the route was omitted, misselected, or failed to resolve.

Positive evidence:

- complete request/access trace plus selective correct-route repair.

Nearest confound:

- F5, F6, or delivered-but-ignored guidance.

Minimal counterfactual:

- force unchanged existing route with an irrelevant-route negative control.

Escalation:

- routing correction only after selective repair and independent recurrence.

### F5 — Local knowledge failure

Definition:

- correct route reached, but owner-local content lacks, collapses, or materially misstates the required distinction.

Positive evidence:

- resource audit confirms the defect and neutral local injection selectively repairs it.

Nearest confound:

- F4, F6, F8, or salience-only improvement.

Minimal counterfactual:

- inject one neutral, reusable local distinction plus a placebo control.

Escalation:

- fix locally first; one-owner defects cannot become F11.

### F6 — Handoff/composition failure

Definition:

- local owners are adequate independently, but decision-relevant state is lost, changed, or omitted between them.

Positive evidence:

- native transfer shows loss, or state-only controlled injection selectively repairs ordinary composition.

Nearest confound:

- F5, F7, generic noncompliance, or F2.

Minimal counterfactual:

- pass the smallest existing decision-relevant state without adding knowledge.

Escalation:

- correct the named boundary; without observable/injectable state, use F12.

### F7 — Resolved-state failure

Definition:

- behavioral tag: output unnecessarily reopens, changes, or ignores valid fixed state.

Positive evidence:

- fixed state visible; reopening visible; no contradiction, staleness, unsupported claim, or insufficiency exception.

Nearest confound:

- invalid fixed state or F6.

Minimal counterfactual:

- fixed-versus-unresolved sensitivity pair.

Escalation:

- localize to F3–F6 or F12; do not double-count.

### F8 — Evidence/inference failure

Definition:

- behavioral tag: claim or action exceeds evidence, erases uncertainty, or invents provenance.

Positive evidence:

- exact output span violates a material evidence predicate.

Nearest confound:

- F1, F5, or F6.

Minimal counterfactual:

- add or remove only the identifying evidence and judge the relation.

Escalation:

- localize mechanism or retain F12.

### F9 — Authority/dependency failure

Definition:

- behavioral tag: output crosses authority, invents approval/facts, or stops before completing permitted marketing work.

Positive evidence:

- explicit authority state and visible boundary violation.

Nearest confound:

- F10 or generic F8.

Minimal counterfactual:

- approval/fact supplied versus pending/absent.

Escalation:

- localize mechanism; a correct bounded stop is no failure.

### F10 — Out-of-scope dependency

Definition:

- correct completion requires authoritative information, capability, or action outside Marketing Practitioner.

Positive evidence:

- missing dependency is material, non-inferable, and owned elsewhere.

Nearest confound:

- F9 or F0.

Minimal counterfactual:

- supply the external owner decision as fixed input.

Escalation:

- obtain the dependency or retain a bounded result; no architecture work.

### F11 — Possible shared representational gap

Definition:

- family-level hypothesis: independent, in-scope states requiring different behavior irreducibly collapse under all existing local, handoff, and composition representations.

Positive evidence:

- completed architecture-reopening dossier and constructive collapse witness.

Nearest confound:

- every cheaper class, especially F5, F6, and F10.

Minimal counterfactual:

- complete the repair ladder and simulate the shared candidate with a negative control.

Escalation:

- independent architecture research only; never direct implementation.

### F12 — Unresolved attribution

Definition:

- material failure confirmed, but available observations and safe counterfactuals cannot discriminate among plausible causes.

Positive evidence:

- missing trace, inconclusive intervention, unstable execution, or surviving nearest confounds.

Nearest confound:

- none; F12 is the refusal to manufacture localization.

Minimal counterfactual:

- obtain the smallest missing operational event or run the most discriminating safe intervention.

Escalation:

- retain visibly; never aggregate into F4–F6 or F11.

---

## 17. F3 Attribution Rule

### Positive evidence

F3 requires at least one:

- intended and delivered visible-input digests differ materially;
- common scaffold/configuration differs materially;
- activation receipt records not-activated, error, or unauthorized fallback;
- active skill ID/version/hash differs from the frozen target;
- correcting only delivery or activation selectively repairs the failure.

Receipt absence alone is not positive evidence unless RUN_SEALED guarantees complete activation-event capture and the host contract defines a missing required receipt as activation failure.

### False-positive attacks

Do not assign F3 when:

- prompt is invalid: F0;
- activation succeeded but output ignored guidance: F2 or behavioral failure plus F12;
- correct skill activated but wrong route selected: F4 candidate;
- unrelated host context changed;
- rubric expected unsupported behavior: F1.

### Minimum intervention

Rerun with identical:

- visible task;
- model/configuration;
- tools;
- evidence;
- host environment.

Change only:

- corrupted delivery; or
- exact v0.5.1 activation.

An explicit receipt is required.

Adding conceptual guidance to the user-visible prompt is not a clean F3 intervention.

### F12 boundary

Use F12 when activation telemetry is incomplete, the intervention changes more than activation/delivery, repaired behavior remains mixed, or host drift cannot be excluded.

---

## 18. F4 Attribution Rule

Before F4 require:

- valid scenario and oracle;
- intact delivery;
- confirmed exact-skill activation;
- post-lock evidence that a specific route was necessary;
- complete request/access telemetry;
- route-specific controlled intervention.

### Routing distinctions

- Route never requested: F4 candidate only; force route.
- Wrong route requested: F4 candidate if correct route omitted and wrong route inadequate.
- Correct route requested but resolution/access failed: F4 may be supported if replaying exact content repairs.
- Correct route resolved and delivered but answer wrong: not F4.
- Route not necessary: no routing failure.
- Task delivery/activation prevented routing: F3.

### Minimum negative control

Deliver one nearby but decision-irrelevant route using the same delivery mechanism and similar context burden.

F4 is supported only when:

- correct route selectively repairs material behavior; and
- irrelevant route does not.

### F12 boundary

Use F12 when route necessity is disputed, telemetry is incomplete, force-routing leaks the answer, or target and irrelevant routes both help.

---

## 19. F5 Attribution Rule

F5 requires:

1. exact skill activation;
2. correct route requested and delivered;
3. exact resource/section hash;
4. direct audit showing missing, wrong, or materially collapsed owner-local knowledge;
5. valid scenario and oracle;
6. no missing boundary state required;
7. selective repair from neutral knowledge injection.

### Neutral knowledge injection

The injection:

- states one reusable owner-local distinction;
- contains no scenario entities;
- supplies no recommended action or final answer;
- adds no scenario fact;
- leaves route, handoff, prompt, tools, and format unchanged;
- is content-addressed;
- has a matched irrelevant/placebo control.

Acceptable:

> Derivative summaries of the same root source do not become independent evidence.

Unacceptable:

> Do not prioritize mid-market; conduct ten more interviews.

### Supports F5 when

- local content demonstrably lacks the distinction;
- neutral injection repairs;
- placebo does not;
- no new state artifact is required;
- variance does not explain the difference.

### Remains inconclusive when

- equivalent guidance already exists;
- injection only increases salience;
- placebo also helps;
- injection supplies a missing scenario fact;
- wrong owner was selected;
- upstream state was unavailable;
- runs remain materially mixed.

Inconclusive outcomes return F12.

---

## 20. F6 Attribution Rule

F6 requires:

- adequate upstream local reasoning;
- adequate downstream local reasoning when given relevant state;
- ordinary composition loses or distorts that state;
- state-only injection repairs;
- no local knowledge rule is added;
- variance does not explain the repair.

### H1 — Native observable handoff

Use when the host already exposes a compact artifact.

Capture:

- upstream-emitted artifact;
- downstream-received artifact;
- boundary/owner identities;
- decision-critical assertion IDs;
- transfer outcome.

F6 is supported when a required assertion exists upstream, is missing or changed downstream, and restoring only that assertion repairs behavior.

### H2 — Controlled evaluation intervention

Use when no native artifact exists.

Procedure:

1. test upstream owner independently;
2. obtain or construct a compact explicit state capsule;
3. test downstream owner independently with the capsule;
4. confirm both local owners are adequate;
5. run ordinary composition;
6. inject only the capsule at the boundary;
7. compare with irrelevant-state or omitted-state control.

The capsule may contain only:

- established upstream conclusions;
- provenance;
- constraints;
- uncertainty;
- protected state.

It may not contain:

- downstream answer;
- new local rule;
- recommended method;
- unavailable fact.

### Distinguishing F6

- From F5: local knowledge is adequate; only state transfer repairs.
- From F4: both routes and resources were delivered.
- From generic noncompliance: state-only intervention selectively repairs; irrelevant state does not.
- From F2: matched repeats do not remain materially mixed.

### F12 boundary

Mandatory F12 when:

- no native artifact is observable;
- no privacy-safe capsule can be injected;
- owner adequacy is disputed;
- capsule supplies a rule or answer;
- ordinary/injected runs remain unstable;
- local-knowledge and handoff explanations cannot be separated.

---

## 21. Execution Variance and Generic Noncompliance

No new taxonomy class is required.

### Mixed exact runs

When exact-config fresh runs produce different material dispositions:

- assign F2;
- retain applicable F7/F8/F9 behavioral tags;
- do not infer F3–F6 without a separate selective intervention.

### Correct operational evidence but wrong answer

When:

- delivery is intact;
- exact skill activated;
- correct routes and adequate resources delivered;
- required state available;
- output still wrong;

record:

- confirmed behavioral failure;
- generic execution noncompliance observed;
- mechanism F12 unless an intervention localizes it.

Generic noncompliance is a descriptive observation, not a new causal class.

If exact repeats alternate between pass and fail, F2 controls the execution-stability claim. If failure recurs but no selective repair exists, report recurrent behavioral failure under configuration plus F12.

If changing only the rubric makes the original output acceptable, F1 preempts system attribution.

---

## 22. Controlled Intervention Ladder

Use the earliest successful explanation.

1. Confirm scenario, oracle, and behavioral judgment.
2. Confirm RUN_BOUND/RUN_SEALED integrity and telemetry completeness.
3. Verify intended versus delivered task and exact activation receipt.
4. Correct only delivery/activation if defective.
5. Inspect route request, resolution, resource, fallback, and error state.
6. Characterize exact-run variance when it remains a plausible explanation.
7. Force existing correct route and run irrelevant-route control.
8. Audit local knowledge; if missing/wrong, inject neutral distinction and placebo.
9. Test upstream and downstream owners independently.
10. Observe native boundary state or inject minimal state capsule.
11. Classify F3/F4/F5/F6 only when one intervention selectively discriminates.
12. Otherwise assign F12.

A later intervention must not be used when an earlier, cheaper intervention already explains the failure.

---

## 23. Immutability and Replay

Use collision-resistant content addressing for:

- scenario and contract;
- oracle/rubric;
- raw intended visible input;
- actually delivered visible input;
- common scaffold;
- frozen skill tree;
- routing index;
- relevant knowledge resources and selected sections;
- host/runtime and tool-schema configuration;
- tools/permissions manifest;
- external-evidence snapshot;
- intervention and injected artifact;
- final output;
- ordered event stream.

The event stream is append-only and sealed by an ordered trace-root hash.

Counterfactual reruns hold constant:

- scenario, oracle, prompt, and scaffold;
- skill tree except for a declared neutral injection;
- model deployment/snapshot where exposed;
- generation and reasoning configuration;
- tools and permissions;
- host/runtime;
- external evidence;
- fresh-context policy;
- output constraints.

The only allowed difference is the content-addressed intervention in INTERVENTION_APPLIED.

Use temporally blocked execution and matching seeds where supported. Do not require byte-identical model outputs.

If model, tools, evidence, or host state changes outside the declared intervention, the comparison is invalid or F12.

---

## 24. Privacy and Chain-of-Thought Boundary

Freeze this rule:

> OBSERVABILITY IS NOT CHAIN-OF-THOUGHT ACCESS.

No execution, validity, judgment, adjudication, or failure-attribution decision may depend on access to chain-of-thought or any equivalent private reasoning trace.

The protocol observes:

- task delivery;
- skill activation;
- externally visible knowledge/resource calls;
- content availability;
- resolution/fallback outcomes;
- explicit compact artifacts;
- controlled interventions;
- outputs and operational errors.

It does not observe:

- private deliberation;
- whether the model internally noticed or understood guidance;
- hidden reasoning steps;
- internal attention;
- scratchpads;
- private token traces;
- latent activations.

Resource and state bodies are retained only when already user-visible, repository content, or explicitly created for evaluation. Events otherwise retain hashes and access-controlled references.

If F4/F5/F6 cannot be distinguished without private reasoning, attribution is F12.

---

## 25. Architecture-Reopening Gate

F11 requires an irreducible representational-collapse witness:

> Two accepted world states require materially different behavior but remain indistinguishable after every applicable existing owner, route, local rule, handoff, resolved-state field, provenance, scope, history, authority, and composition is exercised.

Run this repair ladder. Any earlier successful repair defeats F11:

1. revalidate scenario;
2. repair rubric/judgment;
3. characterize execution variance;
4. repair task delivery/activation;
5. force existing route;
6. inject smallest local rule;
7. pass existing compact handoff state;
8. pin resolved state;
9. expose existing evidence/provenance distinction without supplying answer;
10. supply or stop at authoritative dependency;
11. supply out-of-scope owner decision;
12. explicitly orchestrate existing composition;
13. only then simulate a candidate shared representation.

A finding becomes a possible shared-architecture research question only if:

- realistic, consequential, in-scope decision;
- accepted scenario and robust oracle;
- fluent-wrong and noncanonical-good attacks pass;
- recurrent under tested configuration;
- at least two independent scenario lineages;
- at least two owners or boundaries affected;
- exact activation and route/resource access observed;
- F2 and judge instability do not explain pattern;
- minimal local repair attempted at each plausible owner;
- existing handoff and resolved-state repairs attempted;
- inference and authority alternatives defeated;
- explicit existing composition still collapses distinction;
- S1/S2 and required D1/D2 collapse documented;
- smallest shared candidate repairs all positive cases;
- irrelevant negative control remains stable;
- regression attack finds no new fast-path, over-routing, authority, or resolved-state damage;
- independent adjudicator agrees.

Passing the gate authorizes research, not implementation.

---

## 26. Failure Attribution Record

Every confirmed observation records:

- observation ID;
- scenario, contract, and rubric versions;
- run ID and condition;
- execution fingerprint;
- activation and route/resource evidence;
- violated invariant or relation;
- exact output evidence;
- decision consequence;
- scenario/oracle/judge validity status;
- behavioral tags;
- ranked mechanism candidates;
- positive evidence;
- strongest surviving confound;
- counterfactual performed and result;
- observability limitation;
- current disposition;
- behavior confidence;
- mechanism confidence;
- recurrence signature and lineage;
- next action.

Behavior confidence and mechanism confidence are separate.

High behavioral confidence may coexist with low mechanism confidence.

F4–F6 cannot receive high mechanism confidence without operational events and a selective intervention.

---

## 27. Recurrence and Promotion

Independent recurrence requires at least two scenario lineages with different root provenance.

Not independent:

- exact reruns;
- prompt paraphrases;
- paired mutations;
- renamed companies or platforms;
- derivative artifacts from one source;
- cases from one hidden template.

If the first two lineages share a material dependence such as author, generator, source, platform, or host behavior, require a third lineage.

Promotion ladder:

~~~text
one output
→ observation

validity survives
→ confirmed failure observation

reruns or pairs
→ stability characterized

independent lineages recur
→ candidate failure family

counterfactual mechanism aligns
→ credible failure family

consequential + reproducible + freezeable oracle
→ targeted frozen-evaluation candidate

architecture gate survives
→ possible architecture research candidate
~~~

A targeted-evaluation candidate must freeze the known behavior or relation. It does not inherit a broad performance claim from Pressure Discovery.

---

## 28. Lifecycle and Versioning

Use four lifecycle states:

~~~text
DRAFT
→ RUN-LOCKED FOR DISCOVERY
→ RUN RECORDED
→ DISPOSED
~~~

Validity attack, execution, judgment, adjudication, and attribution are versioned events, not lifecycle states.

Possible dispositions:

- retained;
- revised;
- rejected;
- no system failure;
- scenario/oracle defect;
- candidate mechanism;
- unresolved;
- promoted to targeted evaluation;
- proposed for architecture research.

### Version rules

- Prompt, artifacts, material visible facts, objective, hard predicate, truth type, or pair relation change → new material scenario/contract version.
- Rubric correction → new rubric version and rejudgment of every affected output.
- Judge-instruction change → new adjudication version and rejudgment where disposition may change.
- Typo or metadata-only correction → patch version after independent confirmation of immateriality.
- Rejected/invalid cases remain archived with provenance, rejection reason, attacks, and reusable mutation ideas.
- Outputs and old contracts are never overwritten.

Changing the Mode A population is allowed. Claiming frozen comparative performance after doing so is prohibited.

---

## 29. Discovery Reporting

The primary artifact is a finding ledger.

Report:

- source episodes considered;
- scenarios rejected before execution and reasons;
- accepted/run-locked scenarios by provenance;
- executed, judged, and adjudicated outputs;
- both-pass, skill-only-pass, baseline-only-pass, both-fail, and unresolved A/B patterns by decision family;
- sensitivity and invariance dispositions;
- scenario and rubric defects;
- first-pass judge disagreement;
- cases triggering repeats;
- within-A, within-B, judge, tool, and environment variance;
- F7/F8/F9 behavioral tags;
- supported F3–F6/F10 mechanisms;
- F12 unresolved attributions;
- recurrence signatures and lineage evidence;
- targeted-evaluation candidates;
- F11 gate status;
- no-action and negative findings.

Counts include denominators and provenance status.

Do not report:

- one aggregate score;
- baseline-versus-skill win rate;
- Elo;
- average rubric points;
- difficulty-weighted quality;
- percentages from an evolving non-random pool;
- architecture-gap counts without completed gate status;
- post-adjudication consensus as initial judge agreement.

Counts describe factory flow and diagnostic burden, not population performance.

---

## 30. Methodology-Validation Pilot

The pilot tests whether the evaluation system diagnoses its own failure modes. It does not test whether Marketing Practitioner receives a high score.

Use two segregated tracks totaling 14 visible scenario versions.

### Track I — Diagnostic injection deck

Eight bundles comprising 12 visible scenario versions.

#### Bundle 1 — F0 underspecification

- deliberately underspecified scenario;
- minimally repaired twin.

Visible scenarios: 2.

#### Bundle 2 — F1 oracle failure

One valid scenario judged under:

- defective rubric;
- corrected rubric;
- fluent-wrong anchor;
- noncanonical-good anchor.

Visible scenarios: 1.

#### Bundle 3 — F3/F4/F5/F6 mechanism ladder

One composition-capable visible scenario with internal condition packets:

- P0 clean control;
- P3 delivery/activation failure;
- P4 route omitted or resolution failed;
- P5 correct route with controlled owner-local omission;
- P6 adequate local owners with dropped handoff state;
- N4 correct route/resource delivered but output wrong;
- N6 handoff not observable or safely injectable;
- NV complete evidence with mixed exact runs.

Visible scenarios: 1.

P5 uses an evaluation overlay or injection; it does not modify repository files.

#### Bundle 4 — F7 resolved state

- fixed-state member;
- genuinely unresolved member.

Visible scenarios: 2.

#### Bundle 5 — F2 variance

One byte-identical repeat packet with three outputs per arm and mixed material dispositions.

Visible scenarios: 1.

#### Bundle 6 — F9/F10 boundary

- legitimate authority-boundary case;
- genuinely out-of-scope dependency case.

Visible scenarios: 2.

#### Bundle 7 — False F11

Two independently sourced, apparently recurrent cases that are both repaired by existing local, handoff, or composition interventions.

Visible scenarios: 2.

#### Bundle 8 — F12

One confirmed behavioral failure with deliberately insufficient or inconclusive mechanism evidence.

Visible scenarios: 1.

Track I total: 12.

### Track II — Clean-room independence mini-pool

- one case reconstructed from a contemporaneous operational artifact bundle;
- one case reconstructed from an independent practitioner critical incident.

At least one must remain unmapped or multiply mapped after story/oracle lock.

Track II total: 2.

Pilot total: 14 visible scenario versions.

### Pilot success criteria

- every planted evaluator defect detected;
- F3–F6 correctly separated or returned F12;
- mixed runs classified as F2 rather than determinism;
- authority and scope distinguished;
- zero false architecture promotion;
- noncanonical valid answers accepted;
- fluent decision-wrong answers rejected;
- clean-room cases survive leak audit;
- at least one unresolved attribution retained without forced classification.

The pilot does not estimate Marketing Practitioner performance or failure prevalence.

The pilot is not implemented by this protocol artifact.

---

## 31. Observability Freeze Tests

### O1 — Skill intended; activation receipt absent

Protocol result: pass.

Receipt absence alone does not prove F3. If sealed telemetry guarantees receipt completeness, apply the host’s explicit activation-failure rule. Otherwise use F12 until a forced exact-activation intervention discriminates.

### O2 — Activated; correct route exists; route never requested

Protocol result: pass.

Supports F4 candidate only after route necessity is established and correct-route injection selectively repairs while irrelevant-route control does not.

### O3 — Correct route requested and resource delivered; answer wrong

Protocol result: pass.

Not F4. Investigate F5, F6, F2, generic noncompliance, or F12.

### O4 — Correct route reached; neutral missing-distinction injection repairs

Protocol result: pass.

Supports F5 only when direct content audit confirms omission, injection supplies no answer, and placebo does not repair.

### O5 — Local owners adequate; ordinary composition fails; state injection repairs

Protocol result: pass.

Supports F6 when route/resource evidence is intact, local owners are independently adequate, state loss is demonstrated, and variance is controlled.

### O6 — Same appearance as O5; handoff cannot be observed or safely injected

Protocol result: pass.

Mandatory F12.

### O7 — Operational evidence correct; repeated runs mixed

Protocol result: pass.

F2 plus applicable behavioral tags. No invented F4/F5/F6 mechanism.

### O8 — Route and knowledge interventions fail; rubric correction accepts output

Protocol result: pass.

F1 preempts system attribution and invalidates judgments under the prior rubric.

---

## 32. Minimality and Anti-Creep Rules

For every evidence field ask:

> Which concrete F3/F4/F5/F6 ambiguity becomes irresolvable without it?

Retain only fields with a concrete answer:

- intended/delivered input digests → task-delivery failure;
- scaffold/config digest → delivery failure versus unrelated host change;
- activation receipt and skill hash → F3 versus downstream failure;
- route request → never requested versus resolution failure;
- access/fallback result → failed resolution versus delivered content;
- resource/selector/content hash → wrong or inadequate local content;
- boundary artifact/capsule → F6 versus F5/noncompliance;
- intervention delta → selective repair versus broad context change;
- execution/evidence digests → mechanism effect versus variance/drift;
- sealed completeness → absent event versus missing telemetry.

The protocol does not create:

- a general observability platform;
- a universal state schema;
- a new runtime ontology;
- mandatory production handoff objects;
- chain-of-thought logging;
- evaluation-only Marketing Practitioner architecture;
- a large always-on trace body.

Activation and resource hooks are host-level operational metadata. Boundary artifacts and injections are diagnostic escalation only.

If a host cannot provide the required evidence, the affected mechanism claim remains F12.

---

## 33. Methodological Basis and Limits

The protocol uses several transferable principles:

- validity attaches to a specified interpretation and use, not to a test in the abstract;
- authentic-looking tasks can still measure irrelevant variance;
- representative design favors real decision traces and natural covariation;
- exact oracles are often unavailable for open-ended tasks;
- metamorphic relations can test necessary behavioral properties;
- adaptive discovery and frozen evaluation must remain separate;
- repeated executions answer specific variance questions rather than automatically establishing reliability;
- human and LLM judges can exhibit anchoring, position, verbosity, and style bias;
- disagreement can expose evaluator defects or legitimate pluralism.

These principles do not establish:

- that any individual marketing scenario is realistic;
- that an invariant or relation is correct;
- that three runs estimate a failure rate;
- that human consensus equals truth;
- that an LLM judge is an independent domain adjudicator;
- that passing metamorphic cases proves general capability.

Every transferred principle remains bounded by scenario-specific validity evidence.

---

## 34. Prohibited Interpretations

This protocol does not justify:

- Marketing Practitioner equals a numeric score;
- one failure equals a failure family;
- repeated output equals independent recurrence;
- route availability equals route activation;
- resource delivery equals cognitive use;
- wrong answer equals routing failure;
- neutral injection repair automatically equals local-knowledge failure;
- final prose reveals a handoff;
- agreement equals oracle validity;
- public provenance means contamination is absent;
- baseline superiority means architecture failure;
- F11 means implement a shared abstraction.

Prefer:

- rejected scenario over manufactured confidence;
- oracle correction over executor blame;
- execution variance over deterministic language;
- local repair over shared expansion;
- F12 over unsupported mechanism attribution.

---

## 35. Freeze and Implementation Boundary

Pressure Discovery Protocol v1 is provisionally frozen as a methodology artifact.

The following remain outside this artifact:

- pilot implementation;
- scenario files;
- runner or harness code;
- judge code;
- event-schema implementation;
- runtime instrumentation;
- benchmark manifests;
- aggregate scoring;
- Marketing Practitioner runtime changes.

Before implementing the small methodology-validation pilot:

1. independently review this canonical protocol;
2. confirm the intended host can emit privacy-safe activation and resource-access events;
3. confirm H1 or H2 can be used for F6 without exposing private reasoning;
4. preserve F12 when those capabilities are unavailable;
5. implement only the reviewed pilot, not a mass scenario factory.

No implementation authorization is implied by this file.
