# Episode 01 implementation preflight status

Status: **FINAL LOCAL PROVENANCE REPAIR APPLIED — CLOSURE VERIFICATION REQUIRED — NO LIVE AGENT EVIDENCE**

Frozen design source: `research/stateful-work-episode-evaluation/06-episode-01-design.md` and `07-episode-01-evaluator-fixtures.md` at repaired design candidate `e2731dd897a043cdbecff2f37e850f72c9dc086b`.

The independent implementation/preflight review of `54877829195858230037db6eb1fbdd8e45d0ad10` identified nine defects `E01-IPR-01` through `E01-IPR-09`.

The first repaired implementation target `7efb2e0a730863c9b5cf7854ab655547731fb9ab` received `IMPLEMENTATION_REPAIR_INCOMPLETE`, with `E01-IPR-05` and `E01-IPR-08` still open.

The second repaired target `6f30bdb76c793ba4b90d5c12c808fc4527b2d190` then received another bounded closure result:

```text
IMPLEMENTATION_REPAIR_INCOMPLETE
```

with:

```text
E01-IPR-08 — CLOSED
E01-IPR-05 — OPEN
```

The sole remaining defect was malformed judge provenance: valid evidence refs combined with `judge_id=""`, whitespace-only text, or a non-string runtime value could still be treated as valid provenance.

The final bounded repair is intentionally local:

- semantic judge provenance now requires `judge_id` to be a string;
- `judge_id.strip()` must be non-empty;
- the normalized identity must not equal `unavailable`;
- evidence refs must still be valid sealed refs;
- blank or whitespace-only judge identity therefore fails closed to `NOT_ASSESSABLE`;
- P01 non-reliance with blank judge identity also fails closed instead of making P01 `NOT_APPLICABLE`;
- dedicated regressions cover empty judge ID, whitespace-only judge ID, and P01 `does_not_rely` with blank judge ID.

The prior semantic-applicability repair remains intact:

- H04/H05/H07 `NOT_APPLICABLE` requires grounded provenance;
- P01 activation remains separate from P01 satisfaction through `p01_reliance`;
- FX-07 exercises that activation seam rather than planting applicability;
- C01 remains mandatory after valid control R2 exposure;
- Episode 01 tests and `preflight.py` are wired into normal repository verification.

Interpretation boundary remains unchanged:

```text
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

This is still only a deterministic reference implementation and planted-fixture preflight. It does not establish arbitrary-output semantic-judge validity, Marketing Practitioner efficacy, treatment isolation, mechanism causality, or real-world marketing impact.

No live no-skill / skill-present model execution has been performed or authorized.

If independent closure verification now closes the remaining `E01-IPR-05`, the reference implementation may be merged/frozen. The next separate gate is then an evidence-grounded semantic-judge adapter with its own adversarial preflight and independent review before any live paired execution.
