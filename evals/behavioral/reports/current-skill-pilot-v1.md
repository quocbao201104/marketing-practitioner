# Current-skill behavioral pilot v1

Executed: 2026-08-25  
Status: sealed local pilot; not a benchmark

## Configuration

The frozen corpus contained 12 cases across six decision families. Each case ran twice under a no-skill baseline and twice with the exact current skill copy, for 48 runs total. Both conditions used `gpt-5.6-terra`, `medium` reasoning, isolated ephemeral Git workspaces, and `codex-cli 0.144.3`.

The evaluated current-skill tree hash was:

```text
e15916a1d792516d1434a7605bc1fa5b51774f7580d2870cd006921dda6b20c1
```

Raw run bundles, outputs, events, hashes, blind mappings, and judgments remain ignored local artifacts. This checked-in report contains only reviewed aggregate evidence.

## Operational result

| Arm | Runs | Completed | Operationally invalid |
| --- | ---: | ---: | ---: |
| Baseline | 24 | 24 | 0 |
| Current skill | 24 | 21 | 3 |
| Total | 48 | 45 | 3 |

All three invalid runs were `activation_unverified`: the executor returned an answer, but the event stream did not prove that the current skill had activated. They are excluded from answer-failure counts. No run timed out, crashed, or changed model/effort.

## Condition-blind review

The 45 answer-bearing packets were reviewed in opaque `blind_id` order. Packets omitted profile/arm identity, expected route, and proposed failure class. Objective predicates were applied separately from semantic criteria.

The reviewer was the Codex assistant that implemented the harness, not an independent human. The review is therefore suitable for repository decision support but must not be represented as benchmark-grade or independently adjudicated evidence.

| Answer disposition | Baseline | Current skill | Total |
| --- | ---: | ---: | ---: |
| Pass | 21 | 19 | 40 |
| Fail | 3 | 2 | 5 |
| Operationally invalid | 0 | 3 | 3 |

Two failures were objective 150-character-limit violations in the narrow meta-description case. Three were semantic: two baseline Shopee answers lost material variation/time scope and over-strengthened provider-specific explanations; one current-skill attribution answer preserved the attribution/causality boundary but omitted the required causal-design dependency.

## Paired result

| Paired disposition | Cases |
| --- | ---: |
| Both pass | 8 |
| Skill only pass | 0 |
| Baseline only pass | 0 |
| Both fail | 0 |
| Unresolved | 1 |
| Operationally invalid | 3 |

Two pairs showed repeat instability. One was unresolved because the current-skill repeats split pass/fail; the other occurred inside an operationally invalid pair. No single aggregate score, win rate, or Elo was calculated.

## Decision

This run does not demonstrate a paired quality advantage for the current skill: eight cases were both-pass, three could not be compared operationally, and one was unresolved. It also does not demonstrate that the skill has no value; the sample is small, three skill conditions lack activation evidence, and the review is not independent.

The defensible repository decision is to keep v0.9.0 behavior authoritative, improve activation observability and repeat stability, and avoid capability or reliability claims that outrun this pilot.
