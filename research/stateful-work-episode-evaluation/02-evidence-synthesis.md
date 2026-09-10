# Stateful Work-Episode Evaluation — Evidence Synthesis

Status: **RESEARCH SYNTHESIS — NOT RUNTIME INSTRUCTIONS**

This artifact records the smallest mechanisms recovered from the research passes. It does not claim that any single external benchmark provides the complete methodology adopted by this project.

## External source families inspected

The landscape included:

- **τ-bench / τ²-bench** — stateful interaction, final world-state verification, repeated reliability, and shared user/agent environment control;
- **ToolSandbox** — state dependencies, arbitrary trajectories, milestone/minefield evaluation, and bounded user-simulator knowledge;
- **TheAgentCompany** — realistic workplace environments, result-oriented task evaluation, and the cost of constructing validated long-horizon tasks;
- **AgentDojo** — normal utility separated from adversarial robustness and environment-state utility checks;
- **SkillsBench / SWE-Skills-Bench** — paired skill/no-skill evaluation, frozen repositories/tasks, treatment overhead, and heterogeneous skill effects;
- **Anthropic agent-evaluation guidance** — outcome versus trajectory, multiple valid solution paths, grader design, repeated trials, and evaluator failure modes;
- **OpenAI third-party evaluation guidance** — harness validity, tested-system boundaries, budget/tool reporting, contamination and reward-hacking hazards;
- **micro-randomized trial / JITAI methodology** — decision points, applicability/availability, and evaluating effects only where an intervention opportunity actually applies;
- **causal inference on treatment assignment, non-adherence, and mediation** — treatment-as-assigned versus treatment-as-received and the limits of causal claims from post-treatment mediators;
- **compensating transaction / event-sourcing patterns** — recovery does not erase consequential history and some committed actions require compensation rather than literal undo.

These sources are used for mechanisms and methodological boundaries, not as proof that marketing work has the same ontology as customer support, software engineering, clinical intervention, or distributed systems.

## What survives external triangulation

### 1. Outcome/state first

A work verdict should be grounded in observable world state, committed actions, final artifacts, and task obligations. Agent self-report is not sufficient evidence that work was completed correctly.

### 2. Path pluralism

A valid noncanonical solution must be allowed to pass when the task does not require a specific path. Tool/route/read traces are usually diagnostic or mechanism evidence, not work correctness.

### 3. Explicit mutable state

A long task becomes a genuine episode only when prior actions/events alter later decision conditions. More turns or files alone do not establish long-horizon behavior.

### 4. Constrained actors

When a simulated founder, teammate, customer, or platform affects oracle-relevant facts, the environment must control that actor's knowledge, authority, and action affordances. Free-form roleplay must not invent material world truth.

### 5. Clean competence before adversarial pressure

Robustness must be interpreted alongside normal task utility. A benchmark that contains only traps can reward generic skepticism, refusal, or endless questioning rather than competent practice.

### 6. Paired skill/no-skill comparison

The primary comparative question is the effect of making the frozen skill available under a frozen execution regime. Activation failure, extra context, extra questions, extra tool use, and latency naturally caused by skill availability remain part of the treatment result.

### 7. Evaluator validity is part of the experiment

Before a live agent is blamed, the oracle must reject fluent-but-wrong work and accept defensible noncanonical work. Broken or underspecified scorers can masquerade as model failure.

### 8. Consequential history may matter independently of terminal state

A private error corrected before any material action is not equivalent to an external hard violation followed by a later correction. Recovery can coexist with a historical violation.

### 9. Behavioral denominators must be predeclared

Turns and events are not meaningful denominators. A behavior should be judged only when a prelocked activation/applicability condition becomes true.

### 10. Post-treatment telemetry does not establish causal mechanism

A chapter being read, a route being traversed, or a state being loaded after treatment assignment does not by itself prove that mechanism caused the outcome. Strong mechanism attribution needs a discriminating intervention/control contract; otherwise attribution remains descriptive or unresolved.

## Project-specific synthesis

The project adapts those findings into the existing repository architecture rather than copying a foreign benchmark.

```text
Pressure Discovery
→ oracle semantics
→ validity
→ pressure/control relations
→ attribution

Behavioral Harness
→ paired execution
→ workspace regime
→ sealing
→ blinding
→ profiles
→ run telemetry

Work-Episode Extension
→ dynamic world state
→ observable action/event history
→ bounded actors
→ event delivery
→ cross-time predicates
→ comparative episode validity
```

The exact work-episode representation, event-comparability contract, and comparative-validity rules are project synthesis. They must therefore survive project-specific adversarial review rather than being presented as externally standardized doctrine.

## Research finding: skill efficacy is conditional

The external skill benchmarks do not support treating skill quality as an intrinsic scalar property. Reported effects vary materially across task distribution, model/harness, skill version, repository/version context, and resource regime.

Therefore future claims must remain bounded to the exact frozen evaluation regime. The methodology does not license claims that Marketing Practitioner is generally superior at marketing or that a particular chapter caused an improvement merely because it appeared in a successful trajectory.
