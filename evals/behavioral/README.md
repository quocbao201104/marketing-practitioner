# Behavioral evaluation harness

This harness compares an isolated no-skill baseline with an exact workspace copy of `marketing-practitioner`. It separates executor and isolation failures from answer quality, seals raw run records, and produces condition-blind review packets. It intentionally does not calculate a single quality score.

## Validate the frozen contracts

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate --cases evals\behavioral\cases\pilot-v1.json --profiles evals\behavioral\profiles
```

The pilot has 12 cases and two repetitions per arm. The committed profiles pin the model and reasoning effort. Change them deliberately and treat the result as a different executor condition.

## Exercise infrastructure with fixtures

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run --adapter fixture --results evals\behavioral\results\fixture-smoke
```

Fixture answers test orchestration, isolation, sealing, and report plumbing only. They are not behavioral evidence.

For a bounded preflight, add one or more `--case-id BEH-...` selectors and `--repeat-limit 1`. These selectors do not modify the frozen case or profile contracts; the effective subset is recorded in the manifest.

## Run the live paired pilot

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run --adapter codex-cli --profile-id baseline --profile-id current-skill --results evals\behavioral\results\pilot-v1
```

Every case/profile/repetition runs in a fresh temporary Git workspace. The baseline workspace contains no `marketing-practitioner` skill. The skill arm copies the repository skill to `.agents/skills/marketing-practitioner` and binds its tree hash before execution. Existing result directories are never overwritten.

Review `blind-packets.json` without opening the manifest or run records. Save judgments as:

```json
{
  "judgments": [
    {"blind_id": "5a19...", "disposition": "pass"}
  ]
}
```

Allowed answer dispositions are `pass`, `fail`, and `unresolved`. Then build the paired report:

`blind-index.json` is the sealed mapping used by the report command. Keep it away from reviewers until their judgments are frozen.

```powershell
python -B -m evals.behavioral.behavioral_eval.cli report --results evals\behavioral\results\pilot-v1 --judgments judgments.json --output paired-report.json
```

Generated result bundles are ignored by Git. Preserve only redacted aggregate evidence that has been deliberately audited for release.
