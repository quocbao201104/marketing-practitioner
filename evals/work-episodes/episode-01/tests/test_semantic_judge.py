from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from episode import M, initialize_workspace
from semantic_judge import (
    JudgeDecision,
    JudgeIdentity,
    JudgeTarget,
    SemanticJudgeAdapter,
    build_packet,
    packet_is_blinded,
)
from semantic_judge_protocol import parse_judge_decision, render_judge_prompt


class SemanticJudgeTests(unittest.TestCase):
    @staticmethod
    def _terminal_state(world: str, basis: str):
        temp = tempfile.TemporaryDirectory(prefix="swe-e01-sj-test-")
        root = Path(temp.name)
        state = initialize_workspace(root, world=world)
        state.reserve_creator_inventory(30 * M, basis)
        state.close_booking_gate()
        state.deliver_r2()
        state.close_reduction_gate()
        (root / "launch-plan.md").write_text(
            "# Launch plan\n\nBounded executable plan; do not treat competitor evidence as causal proof.\n",
            encoding="utf-8",
        )
        (root / "measurement-plan.md").write_text(
            "# Measurement plan\n\nMeasure Aurora-specific realized contribution and incrementality.\n",
            encoding="utf-8",
        )
        state.terminal_gate("Final package submitted.")
        return temp, state

    @staticmethod
    def _decision_for(packet, *, reliance: str = "does_not_rely"):
        refs = set(packet.evidence_refs)
        if packet.target is JudgeTarget.PRE_R2_RELIANCE:
            basis = next(ref for ref in refs if ref.endswith(":basis"))
            return JudgeDecision("applicable", reliance, (basis,), "sealed pre-audit basis")
        if packet.target is JudgeTarget.POST_R2_REVISION:
            basis = next(ref for ref in refs if ref.endswith(":basis") and ":A001:" in ref)
            exposure = next(ref for ref in refs if ref.startswith("exposure:R2_EXPOSURE:"))
            return JudgeDecision(
                "applicable", "satisfied", (basis, exposure), "basis revised after audit"
            )
        if packet.target is JudgeTarget.AUDIT_UPDATE:
            exposure = next(ref for ref in refs if ref.startswith("exposure:R2_EXPOSURE:"))
            terminal = next(ref for ref in refs if ref.startswith("terminal:"))
            return JudgeDecision(
                "applicable", "satisfied", (exposure, terminal), "audit incorporated"
            )
        if packet.target is JudgeTarget.TERMINAL_COHERENCE:
            launch = next(ref for ref in refs if "terminal:artifact:launch-plan.md:" in ref)
            measurement = next(
                ref for ref in refs if "terminal:artifact:measurement-plan.md:" in ref
            )
            return JudgeDecision(
                "applicable", "satisfied", (launch, measurement), "terminal package coherent"
            )
        first = next(iter(packet.evidence_refs))
        return JudgeDecision("applicable", "satisfied", (first,), "grounded")

    def test_packets_hide_sibling_and_treatment_labels(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        try:
            for target in JudgeTarget:
                packet = build_packet(state, target)
                payload = json.dumps(packet.to_dict(), ensure_ascii=False)
                self.assertTrue(packet_is_blinded(packet))
                self.assertNotIn("SWE-E01-P", payload)
                self.assertNotIn("SWE-E01-C", payload)
                self.assertNotIn("skill-present", payload)
                self.assertNotIn("no-skill", payload)
                self.assertNotIn("expected_verdict", payload)
        finally:
            temp.cleanup()

    def test_pre_r2_reliance_packet_excludes_later_evidence(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "5x proves creator profitability"
        )
        try:
            packet = build_packet(state, JudgeTarget.PRE_R2_RELIANCE)
            self.assertTrue(packet.evidence)
            self.assertTrue(all(item.logical_time == "09:00" for item in packet.evidence))
            self.assertTrue(all(item.source_kind != "analytics_audit" for item in packet.evidence))
            self.assertTrue(all(not item.source_kind.startswith("terminal_") for item in packet.evidence))
        finally:
            temp.cleanup()

    def test_adapter_injects_frozen_identity(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        try:
            identity = JudgeIdentity("provider-x", "model-y")
            adapter = SemanticJudgeAdapter(identity, self._decision_for)
            record = adapter._judge(state, JudgeTarget.EVIDENCE_SCOPE)
            self.assertTrue(record.accepted)
            self.assertEqual(identity.judge_id, record.assessment.judge_id)
            self.assertNotEqual("unavailable", record.assessment.judge_id)
        finally:
            temp.cleanup()

    def test_invalid_identity_fails_closed(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        try:
            adapter = SemanticJudgeAdapter(JudgeIdentity(" ", "model-y"), self._decision_for)
            record = adapter._judge(state, JudgeTarget.EVIDENCE_SCOPE)
            self.assertFalse(record.accepted)
            self.assertEqual("unavailable", record.assessment.judge_id)
            self.assertEqual("unknown", record.assessment.applicability)
        finally:
            temp.cleanup()

    def test_out_of_packet_evidence_fails_closed(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        try:
            def bad_backend(packet):
                return JudgeDecision(
                    "applicable",
                    "satisfied",
                    ("terminal:artifact:invented:deadbeef",),
                    "invented citation",
                )

            adapter = SemanticJudgeAdapter(JudgeIdentity("p", "m"), bad_backend)
            record = adapter._judge(state, JudgeTarget.EVIDENCE_SCOPE)
            self.assertFalse(record.accepted)
            self.assertEqual("out_of_packet_evidence_ref", record.rejection_reason)
            self.assertEqual("unknown", record.assessment.applicability)
        finally:
            temp.cleanup()

    def test_terminal_coherence_requires_both_deliverable_refs(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        try:
            def incomplete_backend(packet):
                launch = next(
                    ref
                    for ref in packet.evidence_refs
                    if "terminal:artifact:launch-plan.md:" in ref
                )
                return JudgeDecision("applicable", "satisfied", (launch,), "one file only")

            adapter = SemanticJudgeAdapter(JudgeIdentity("p", "m"), incomplete_backend)
            record = adapter._judge(state, JudgeTarget.TERMINAL_COHERENCE)
            self.assertFalse(record.accepted)
            self.assertEqual("required_evidence_not_cited", record.rejection_reason)
        finally:
            temp.cleanup()

    def test_non_reliance_skips_post_r2_revision_judgment(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        calls: list[JudgeTarget] = []
        try:
            def backend(packet):
                calls.append(packet.target)
                return self._decision_for(packet, reliance="does_not_rely")

            adapter = SemanticJudgeAdapter(JudgeIdentity("p", "m"), backend)
            run = adapter.run(state)
            self.assertIn(JudgeTarget.PRE_R2_RELIANCE, calls)
            self.assertNotIn(JudgeTarget.POST_R2_REVISION, calls)
            self.assertEqual("does_not_rely", run.observations.p01_reliance.outcome)
        finally:
            temp.cleanup()

    def test_reliance_requires_post_r2_revision_judgment(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "5x proves creator profitability"
        )
        calls: list[JudgeTarget] = []
        try:
            def backend(packet):
                calls.append(packet.target)
                return self._decision_for(packet, reliance="relies")

            adapter = SemanticJudgeAdapter(JudgeIdentity("p", "m"), backend)
            run = adapter.run(state)
            self.assertIn(JudgeTarget.PRE_R2_RELIANCE, calls)
            self.assertIn(JudgeTarget.POST_R2_REVISION, calls)
            self.assertEqual("relies", run.observations.p01_reliance.outcome)
            self.assertEqual("satisfied", run.observations.p01.outcome)
        finally:
            temp.cleanup()

    def test_other_sibling_routes_to_audit_update_only(self):
        temp, state = self._terminal_state(
            "SWE-E01-C", "Bounded access under initial ambiguity"
        )
        calls: list[JudgeTarget] = []
        try:
            def backend(packet):
                calls.append(packet.target)
                return self._decision_for(packet)

            adapter = SemanticJudgeAdapter(JudgeIdentity("p", "m"), backend)
            run = adapter.run(state)
            self.assertIn(JudgeTarget.AUDIT_UPDATE, calls)
            self.assertNotIn(JudgeTarget.PRE_R2_RELIANCE, calls)
            self.assertNotIn(JudgeTarget.POST_R2_REVISION, calls)
            self.assertEqual("satisfied", run.observations.c01.outcome)
        finally:
            temp.cleanup()

    def test_protocol_is_json_only_and_exact_schema(self):
        temp, state = self._terminal_state(
            "SWE-E01-P", "R1 is ambiguous; bounded learning only"
        )
        try:
            packet = build_packet(state, JudgeTarget.EVIDENCE_SCOPE)
            prompt = render_judge_prompt(packet)
            self.assertIn(packet.packet_id, prompt)
            self.assertNotIn("SWE-E01-P", prompt)
            decision = parse_judge_decision(
                json.dumps(
                    {
                        "applicability": "applicable",
                        "outcome": "satisfied",
                        "evidence_refs": [packet.evidence_refs[0]],
                        "rationale": "grounded",
                    }
                )
            )
            self.assertEqual("satisfied", decision.outcome)
            with self.assertRaises(ValueError):
                parse_judge_decision(
                    json.dumps(
                        {
                            "applicability": "applicable",
                            "outcome": "satisfied",
                            "evidence_refs": [],
                            "rationale": "x",
                            "expected": "PASS",
                        }
                    )
                )
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
