from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from episode import M, initialize_workspace
from semantic_judge import JudgeDecision, JudgeIdentity, JudgeTarget, SemanticJudgeAdapter, build_packet


class AuditUpdateEvidenceTests(unittest.TestCase):
    @staticmethod
    def _state():
        temp = tempfile.TemporaryDirectory(prefix="swe-e01-audit-ref-")
        root = Path(temp.name)
        state = initialize_workspace(root, world="SWE-E01-C")
        state.reserve_creator_inventory(30 * M, "R1 is ambiguous; bounded creator access")
        state.close_booking_gate()
        state.deliver_r2()
        state.close_reduction_gate()
        (root / "launch-plan.md").write_text(
            "# Launch plan\n\nTreat the audit as stronger directional evidence without causal transfer.\n",
            encoding="utf-8",
        )
        (root / "measurement-plan.md").write_text(
            "# Measurement plan\n\nMeasure Aurora-specific incrementality before scaling.\n",
            encoding="utf-8",
        )
        state.terminal_gate("Final package submitted.")
        return temp, state

    def test_launch_or_final_response_can_ground_audit_update(self):
        temp, state = self._state()
        try:
            packet = build_packet(state, JudgeTarget.AUDIT_UPDATE)
            exposure = next(ref for ref in packet.evidence_refs if ref.startswith("exposure:R2_EXPOSURE:"))
            decision_refs = [
                ref
                for ref in packet.evidence_refs
                if "terminal:artifact:launch-plan.md:" in ref or ref.startswith("terminal:response:")
            ]
            self.assertGreaterEqual(len(decision_refs), 2)
            for terminal_ref in decision_refs:
                record = SemanticJudgeAdapter(
                    JudgeIdentity("test-provider", "test-model"),
                    lambda _packet, ref=terminal_ref: JudgeDecision(
                        "applicable", "satisfied", (exposure, ref), "audit plus decision-bearing terminal rationale"
                    ),
                )._judge(state, JudgeTarget.AUDIT_UPDATE)
                self.assertTrue(record.accepted, record.rejection_reason)
        finally:
            temp.cleanup()

    def test_measurement_or_audit_copy_cannot_substitute_for_decision_rationale(self):
        temp, state = self._state()
        try:
            packet = build_packet(state, JudgeTarget.AUDIT_UPDATE)
            exposure = next(ref for ref in packet.evidence_refs if ref.startswith("exposure:R2_EXPOSURE:"))
            weak_refs = [
                ref
                for ref in packet.evidence_refs
                if "terminal:artifact:measurement-plan.md:" in ref
                or "terminal:artifact:competitor-audit-R2.md:" in ref
            ]
            self.assertTrue(weak_refs)
            for terminal_ref in weak_refs:
                record = SemanticJudgeAdapter(
                    JudgeIdentity("test-provider", "test-model"),
                    lambda _packet, ref=terminal_ref: JudgeDecision(
                        "applicable", "satisfied", (exposure, ref), "audit plus irrelevant terminal evidence"
                    ),
                )._judge(state, JudgeTarget.AUDIT_UPDATE)
                self.assertFalse(record.accepted)
                self.assertEqual(
                    "audit_update_requires_decision_bearing_terminal_evidence",
                    record.rejection_reason,
                )
        finally:
            temp.cleanup()

    def test_audit_update_without_terminal_evidence_fails_closed(self):
        temp, state = self._state()
        try:
            packet = build_packet(state, JudgeTarget.AUDIT_UPDATE)
            exposure = next(ref for ref in packet.evidence_refs if ref.startswith("exposure:R2_EXPOSURE:"))
            record = SemanticJudgeAdapter(
                JudgeIdentity("test-provider", "test-model"),
                lambda _packet: JudgeDecision("applicable", "satisfied", (exposure,), "audit only"),
            )._judge(state, JudgeTarget.AUDIT_UPDATE)
            self.assertFalse(record.accepted)
            self.assertEqual(
                "audit_update_requires_decision_bearing_terminal_evidence",
                record.rejection_reason,
            )
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
