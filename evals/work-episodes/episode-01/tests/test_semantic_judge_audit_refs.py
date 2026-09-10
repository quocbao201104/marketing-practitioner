from __future__ import annotations

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
)


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

    def test_any_packet_terminal_evidence_can_ground_audit_update(self):
        temp, state = self._state()
        try:
            packet = build_packet(state, JudgeTarget.AUDIT_UPDATE)
            exposure = next(
                ref for ref in packet.evidence_refs if ref.startswith("exposure:R2_EXPOSURE:")
            )
            terminal_refs = sorted(
                ref for ref in packet.evidence_refs if ref.startswith("terminal:")
            )
            self.assertGreaterEqual(len(terminal_refs), 2)

            for terminal_ref in (terminal_refs[0], terminal_refs[-1]):
                adapter = SemanticJudgeAdapter(
                    JudgeIdentity("test-provider", "test-model"),
                    lambda _packet, ref=terminal_ref: JudgeDecision(
                        "applicable",
                        "satisfied",
                        (exposure, ref),
                        "audit plus terminal evidence",
                    ),
                )
                record = adapter._judge(state, JudgeTarget.AUDIT_UPDATE)
                self.assertTrue(record.accepted, record.rejection_reason)
                self.assertEqual("satisfied", record.assessment.outcome)
        finally:
            temp.cleanup()

    def test_audit_update_without_terminal_evidence_fails_closed(self):
        temp, state = self._state()
        try:
            packet = build_packet(state, JudgeTarget.AUDIT_UPDATE)
            exposure = next(
                ref for ref in packet.evidence_refs if ref.startswith("exposure:R2_EXPOSURE:")
            )
            adapter = SemanticJudgeAdapter(
                JudgeIdentity("test-provider", "test-model"),
                lambda _packet: JudgeDecision(
                    "applicable", "satisfied", (exposure,), "audit only"
                ),
            )
            record = adapter._judge(state, JudgeTarget.AUDIT_UPDATE)
            self.assertFalse(record.accepted)
            self.assertEqual(
                "audit_update_requires_terminal_evidence", record.rejection_reason
            )
            self.assertEqual("unknown", record.assessment.applicability)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
