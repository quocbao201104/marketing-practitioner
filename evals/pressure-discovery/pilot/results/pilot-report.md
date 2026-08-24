# Pressure Discovery Methodology-Validation Pilot Report

This deterministic run validates evaluation plumbing only. It does not evaluate Marketing Practitioner capability or prevalence.

## Frozen input

- Protocol: `evals/pressure-discovery/protocol-v1.md`
- Protocol commit: `f12a331c5a2a92af05c84e7012216e01c895348a`
- Target: Marketing Practitioner v0.5.1 at `4278758a9bd31bde4278f634f58e3dcff3187fea`

## Scenario flow

- Visible scenario versions: 14
- Diagnostic injection lane: 12
- Clean-room independence lane: 2
- Rejected and preserved: PD-DI-001@1.0.0

## Scenario versions

- `PD-DI-001@1.0.0` — diagnostic_injection; scenario invalidity and underspecification; truth T2 candidate; modifiers none; planted diagnostic F0.
- `PD-DI-001@2.0.0` — diagnostic_injection; minimal visible repair of the underspecified twin; truth T2; modifiers none; planted diagnostic none.
- `PD-DI-002@1.0.0` — diagnostic_injection; defective rubric versus corrected rubric with both oracle attacks; truth T2; modifiers none; planted diagnostic F1.
- `PD-DI-003@1.0.0` — diagnostic_injection; task, activation, route, local-content, composition, negative-control, and mixed-run mechanism ladder; truth T2; modifiers R; planted diagnostic multiple internal packets.
- `PD-DI-004-A@1.0.0` — diagnostic_injection; resolved-state behavioral sensitivity member; truth T2; modifiers R; planted diagnostic F7.
- `PD-DI-004-B@1.0.0` — diagnostic_injection; genuinely unresolved sensitivity member; truth T3; modifiers none; planted diagnostic none.
- `PD-DI-005@1.0.0` — diagnostic_injection; byte-identical repeat variance; truth T2; modifiers none; planted diagnostic F2.
- `PD-DI-006@1.0.0` — diagnostic_injection; authority-boundary behavioral failure; truth T3; modifiers A; planted diagnostic F9.
- `PD-DI-007@1.0.0` — diagnostic_injection; authoritative out-of-scope dependency; truth T2; modifiers A; planted diagnostic F10.
- `PD-DI-008@1.0.0` — diagnostic_injection; apparent family recurrence defeated by owner-local repair; truth T2; modifiers none; planted diagnostic false F11.
- `PD-DI-009@1.0.0` — diagnostic_injection; apparent family recurrence defeated by state-only composition repair; truth T2; modifiers R; planted diagnostic false F11.
- `PD-DI-010@1.0.0` — diagnostic_injection; confirmed behavior with insufficient telemetry; truth T2; modifiers none; planted diagnostic F12.
- `PD-CR-001@1.0.0` — clean_room_independence; clean-room operational artifact bundle; truth T3; modifiers A; planted diagnostic none.
- `PD-CR-002@1.0.0` — clean_room_independence; clean-room practitioner critical incident; truth T3; modifiers none; planted diagnostic none.

## Validity

- Outcomes: ACCEPT=13, REJECT=1
- Rejected scenarios remain preserved as artifacts.

## Planted methodology recovery

- Detected condition packets: COND-001, COND-003, COND-005, COND-006, COND-007, COND-008, COND-009, COND-010, COND-011, COND-012, COND-014, COND-015, COND-016, COND-017, COND-018, COND-019
- Missed condition packets: none

## Taxonomy recovery

- F0: COND-001
- F1: COND-003
- F10: COND-016
- F12: COND-009, COND-010, COND-012, COND-015, COND-019
- F2: COND-011, COND-014
- F3: COND-005
- F4: COND-006
- F5: COND-007, COND-017
- F6: COND-008, COND-018
- F7: COND-005, COND-006, COND-007, COND-008, COND-009, COND-010, COND-011, COND-012, COND-018
- F8: COND-014, COND-017, COND-019
- F9: COND-015, COND-016

## Pair relations

- `PAIR-001`: passed=false; member_not_independently_acceptable.
- `PAIR-004`: passed=true; relation_satisfied.

## Run evidence

- Complete traces: COND-002, COND-003, COND-004, COND-005, COND-006, COND-007, COND-008, COND-009, COND-010, COND-011, COND-012, COND-013-CONTROL, COND-013, COND-014, COND-015, COND-016, COND-017, COND-018, COND-020, COND-021
- Intentionally incomplete traces: COND-019
- Rejected before execution: COND-001

## Finding ledger

- Full sealed condition records: 22.
- The JSON artifact retains executed outputs, judgments, traces, A/B repeats, counterfactual interventions, strongest confounds, and observation records.
- Explicit A/B disposition-pattern records: 2.

## Architecture-reopening gate

- All apparent cases rejected: true.
- Gate output authorizes research only and generated no architecture.

## Unresolved attribution

- Retained condition packets: COND-009, COND-010, COND-012, COND-015, COND-019

## Clean-room independence

- Status: fixture_independence_checks_passed
- Provenance roots: ROOT-IMPACT-DIALING-2011, ROOT-KFC-UK-2018
- Post-lock mapping statuses: multiply_mapped, unmapped
- Distinct pre-lock roles: clean-room-oracle-author-01, clean-room-scenario-editor-01, clean-room-source-curator-01
- Bound source snapshots: SOURCE-CR-001, SOURCE-CR-002
- Live human judgment was not executed; fixture judgment plumbing only.

## Implementation limitations

- Candidate semantics and judge records are deterministic fixtures, not live model or human judgments.
- Clean-room checks validate recorded provenance and access attestations; they do not establish population recurrence.
- The run exercises evaluation plumbing only and authorizes no Marketing Practitioner capability conclusion.
