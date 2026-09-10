# SWE-XCI-01 reference implementation

This directory is the deterministic reference implementation and evaluator-preflight scaffold for the frozen synthetic targeted episode:

`SWE-XCI-01 — Cross-artifact Decision Change & Repair`

Frozen design head:

`274a41b60600638b0bb59410a0633c72130e0525`

The implementation intentionally reuses the existing Stateful Work-Episode evaluation semantics:

- explicit mutable world state;
- 09:00 authoritative baseline, 10:30 accepted QA-candidate seal, and 15:00 terminal state;
- exogenous 11:00 R2 exposure;
- pressure/control siblings;
- prelocked proposition-level relation ledger;
- `SATISFIED / VIOLATED / NOT_ASSESSABLE / NOT_APPLICABLE`;
- non-compensatory work verdict aggregation;
- fail-closed semantic-assessment provenance;
- path pluralism;
- comparative exposure validation.

The 13 fixtures are planted evaluator tests. They are not Marketing Practitioner behavioral evidence.

Run the deterministic preflight from this directory:

```powershell
python -B preflight.py
```

Run tests:

```powershell
python -B -m unittest discover -s tests -p "test_*.py"
```

A passing preflight does **not** validate a live semantic judge and does **not** authorize live no-skill / skill-present claims. Those remain separate gates.
