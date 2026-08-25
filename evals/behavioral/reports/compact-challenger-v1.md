# Compact-controller challenger v1

Executed: 2026-08-25  
Outcome: rejected; retained as an experiment

The challenger reduced the initial controller from 6,768 to 1,692 words (75%) and from 52,003 to 13,229 UTF-8 bytes. Integrity tests retained the eight-step controller, six universal invariants, all logical namespaces, key state handoffs, the complete resource tree, and current package validation.

It then ran the same 12 frozen cases twice with `gpt-5.6-terra` and `medium` reasoning. Of 24 challenger runs, 17 completed and seven were `activation_unverified`. The current-skill arm had 21 completed and three activation-unverified runs under the same case/model/effort configuration.

The promotion gate forbids increased activation or routing failure. Because activation-unverified runs increased from 3/24 to 7/24, the challenger was rejected before semantic scoring. No answer-quality claim is made from its 17 answer-bearing outputs.

The installed [SKILL.md](../../../skills/marketing-practitioner/SKILL.md) remains unchanged. The challenger stays under `evals/behavioral/challengers/` for future activation/description experiments; it is not release behavior.
