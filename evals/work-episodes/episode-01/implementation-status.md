# Episode 01 implementation preflight status

Status: **SECOND BOUNDED REPAIR APPLIED — CLOSURE VERIFICATION REQUIRED — NO LIVE AGENT EVIDENCE**

Frozen design source: `research/stateful-work-episode-evaluation/06-episode-01-design.md` and `07-episode-01-evaluator-fixtures.md` at repaired design candidate `e2731dd897a043cdbecff2f37e850f72c9dc086b`.

The independent implementation/preflight review of `54877829195858230037db6eb1fbdd8e45d0ad10` identified nine defects `E01-IPR-01` through `E01-IPR-09`.

The first repaired implementation target `7efb2e0a730863c9b5cf7854ab655547731fb9ab` then received closure verdict:

```text
IMPLEMENTATION_REPAIR_INCOMPLETE
```

with:

```text
E01-IPR-01 — CLOSED
E01-IPR-02 — CLOSED
E01-IPR-03 — CLOSED
E01-IPR-04 — CLOSED
E01-IPR-05 — OPEN
E01-IPR-06 — CLOSED
E01-IPR-07 — CLOSED
E01-IPR-08 — OPEN
E01-IPR-09 — CLOSED
```

The second bounded repair changes only the remaining semantic-applicability/fixture seam:

- H04/H05/H07 `NOT_APPLICABLE` now requires valid evidence references plus a non-unavailable judge identity; otherwise the predicate is `NOT_ASSESSABLE`;
- P01 activation is separated from P01 satisfaction through `p01_reliance`;
- `p01_reliance` is an evidence-grounded semantic activation judgment over the sealed pre-R2 reservation basis (`relies`, `does_not_rely`, or unresolved);
- once reliance activates P01, a P01 outcome assessment cannot switch it off with `not_applicable`; missing outcome judgment becomes `NOT_ASSESSABLE`;
- C01 remains mandatory after valid control R2 exposure and fails closed when its semantic judgment is absent;
- FX-07 now exercises the separate activation seam from the sealed basis rather than selecting `obs.p01.applicability` directly;
- a non-reliance counterpart confirms that an ambiguity/bounded-learning basis leaves the profitability-reliance branch `NOT_APPLICABLE`;
- regression tests explicitly cover ungrounded semantic `NOT_APPLICABLE`, P01 reliance/non-reliance, P01 attempted applicability bypass, and missing C01 judgment.

Repository verification now invokes both:

```text
python -B -m unittest discover -s evals/work-episodes/episode-01/tests -v
python -B evals/work-episodes/episode-01/preflight.py
```

so Episode 01 tests/preflight are part of the normal branch verification path.

Interpretation boundary:

This remains a deterministic reference implementation and planted-fixture preflight. The fixture semantic assessments do not establish validity on arbitrary live model outputs.

The following locks remain mandatory:

```text
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

No live no-skill / skill-present model execution has been performed or authorized.

If independent closure verification closes `E01-IPR-05` and `E01-IPR-08`, the next gate is a separately frozen evidence-grounded semantic-judge adapter with its own adversarial preflight and independent review. Only after that gate passes may paired live execution be considered.
